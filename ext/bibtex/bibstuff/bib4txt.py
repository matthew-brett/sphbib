#!/usr/bin/env python
# bib4txt.py
"""
Creates formatted references for a text document.
Uuseful for reStructuredText documents.
Interacts with a Bibtex style database file
(without using LaTeX or bibtex).

Dependencies:

- Python 2.4 or higher
- SimpleParse (binaries available!)
- BibStuff (which you should have if you have this)

The source text file should include citation references in reStructuredText format:
http://docutils.sourceforge.net/docs/user/rst/quickref.html#citations
Roughly: a citation key enclosed in brackets, followed by an underscore.
Citation keys cannot be all digits.

The source document can be output with formatted citation references substituted for the citation keys.
In this case, the reference list is added to the end of the file.   

A slight modification of the reStructuredText ``cite`` directive is currently allowed:

- Most characters are permitted.
  E.g., ``[Schwilk+Isaac:2006]_`` is not currently (2006) legal in reST but will be recognized by bib4txt.
  Comment: it is expected that this will become legal reST in the near future.
- Comma separted multiple keys are permitted in a cite:  e.g., ``[Schwilk1999,Isaac2000]_``
  This is not legal reST.

The intent is for the formatted references to be written to a separate file.
You can then include this in your reST document with an ``include`` directive.

How it works:

- Uses SimpleParse_ to convert an EBNF_ grammar into an object for scanning reST files for citation references.
- Uses SimpleParse_ to convert an EBNF_ grammar into an object for scanning .bib files.  (See Bibstuff's bibgrammar.py.)
- Extracts the citation references from the input document.
- Outputs a sorted list of citation definitions, to be used in the References section of your documents.

:author: Alan G. Isaac
:date: 2006-07-27
:contact: http://www.american.edu/cas/econ/faculty/isaac/isaac1.htm
:copyright: 2006 by Alan G. Isaac
:license: MIT (see `license.txt`_)
:note: bib4txt is an extensive refactoring and enhancement of addrefs.py, by Dylan Schwilk
:note: Python 2.4 dependencies: sets, sorted
:TODO: address the TODOs in the associate BibStuff files, especially in bibstyles/shared.py
:TODO: allow multiple bibfiles
:TODO: when assuming 2.5 is finally OK, use 'with' for file handling

.. _EBNF: http://www.garshol.priv.no/download/text/bnf.html
.. _SimpleParse: http://simpleparse.sourceforge.net/
.. _license.txt: ./license.txt
"""
__docformat__ = "restructuredtext en"
__version__ = "1.1.1"
__needs__ = '2.4'


###################  IMPORTS  ##################################################
#import from standard library
import os,sys
import logging
logging.basicConfig(format='\n%(levelname)s:\n%(message)s\n')
bib4txt_logger = logging.getLogger('bibstuff_logger')

#import dependencies
import simpleparse

#local imports
import bibfile, bibgrammar, bibstyles
import ebnf_sp
################################################################################


###################  GLOBALS  ##################################################
# some globals are set when this file is run as a script
#	style
#	bibfile_processor



# note that the standard separator for multiple keys in one citation reference is a comma
# CITATION_SEP = ','
# set in styles/shared.py






def make_text_output(src_as_string,
                     src_parser,
                     parsed_bibfile,
                     style,
                     citations_only=True):
	"""Create intext citations and the bibliography"""
	#first: create a citation manager to handle the bibfile(s)
	citation_manager = style.CitationManager([parsed_bibfile], keys=None, citation_template=style.CITATION_TEMPLATE)
	#second: create CiteRefProcessor object to process cites during src parsing
	#        (associate with the citation_manager)
	cite_processor = bibstyles.shared.CiteRefProcessor(citation_manager)
	#third: parse the text (taglist is a dummy container)
	taglist = src_parser.parse(src_as_string,processor=cite_processor)
	"""The cite_processor now holds the cite keys and
	is associated with citation_manager which holds the bibliography,
	so we can make a sorted entry list.  To do so need:
		- the keys for the citations referenced
		- a sort-key on which to base the sorting
	:note: Sorting is style dependent---e.g., might sort entries on citation_rank.
	"""
	#set the citation manager citekeys to all found keys (an ordered list)
	#citation_manager.citekeys = cite_processor.all_citekeys
	#make the citation definitions for a list of References
	result = citation_manager.make_citations()
	#lastly, prepend the entire document, if desired
	if not citations_only:
		result = cite_processor.__repr__() + result
	return result

################################################################################



		
		

def main():
	"""Command-line tool.  See bib4txt.py -h for help.
	"""

	#set default input and output
	input = sys.stdin
	output = sys.stdout
	
	from optparse import OptionParser
	
	usage = """
	usage: %prog [options] BIB_DATABASE
	standard usage: %prog -i reST_FILE  -n -o refs_FILE BIB_DATABASE
	"""

	parser = OptionParser(usage=usage, version ="%prog " + __version__)

	parser.add_option("-i", "--infile", action="store", type="string", dest="infile",
					  help="Parse FILE for citation references.", metavar="FILE")
	parser.add_option("-o", "--outfile", action="store", type="string", dest="outfile",
					  help="Write formatted references to FILE", metavar="FILE")
	parser.add_option("-n", "--nuke", action="store_true", dest="overwrite", default=False,
					  help="silently overwrite outfile, default=%default")
	parser.add_option("-s", "--stylefile", action="store", dest="stylefile", default="default.py",
					  help="Specify user-chosen style file",metavar="FILE")
	parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False,
					  help="Print INFO messages to stdout, default=%default")
	parser.add_option("-V", "--very_verbose", action="store_true", dest="very_verbose", default=False,
					  help="Print DEBUG messages to stdout, default=%default")
	parser.add_option("-a", "--all", action="store_true", dest="entire_doc",
		              default=False, help="Output entire document, making citation reference substitutions, default=%default")
	parser.add_option("-x", "--xp", action="store_true", dest="xp_parse",
		              default=False, help="Use experimental document parser, default=%default")

	(options, args) = parser.parse_args()
	if options.verbose:
		bib4txt_logger.setLevel(logging.INFO)
	if options.very_verbose:
		bib4txt_logger.setLevel(logging.DEBUG)
	bib4txt_logger.info("Script running.\nargs=%s\ninfile=%s\noutfile=%s\nstyle file=%s"
	             %(args, options.infile, options.outfile,options.stylefile)
	            )
	exec("import bibstyles.%s as style"%os.path.splitext(options.stylefile)[0])

	# open output file for writing (default: stdout)
	if options.outfile:
		if os.path.exists(options.outfile) and not options.overwrite:
			print "File %s exists:  use -n option to nuke (overwrite) this file."%(options.outfile)
			sys.exit(1)
		output = open(options.outfile,'w')

	# read database (.bib) file
	if len(args) != 1:
		print "Wrong number of arguments>"
		sys.exit(1)
	bibfile_name = args[-1]
	if (os.path.splitext(bibfile_name)[-1]).lower() != ".bib":
		bib4txt_logger.warning(bibfile_name + " does not appear to be a .bib file")
	try :
		bibfile_as_string = open(bibfile_name,'r').read()
	except :
		print "Database file not found."
		sys.exit(1)


	# read input file (default: stdin)
	if options.infile:
		try:
			input = open(options.infile,'r')
		except:
			print "Cannot open: "+options.infile
			sys.exit(1)
		
		
	if options.entire_doc:
		ebnf_dec = ebnf_sp.cites_rest
	else:
		ebnf_dec = ebnf_sp.cites_only_rest
	if options.xp_parse:
		ebnf_dec = ebnf_sp.cites_xp
	# Create a simpleparse.parser Parser based on the chosen grammar
	cite_parser = simpleparse.parser.Parser(ebnf_dec, root='src')

	# create object to store parsed .bib file
	bibfile_processor = bibfile.BibFile()
	#store parsed .bib file in the bibfile_processor
	#  TODO: allow multiple .bib files
	bibgrammar.Parse(bibfile_as_string, bibfile_processor)


	result = make_text_output(input.read(),
									cite_parser,
									bibfile_processor,
									style,
									citations_only = not options.entire_doc)

	output.write(result)        
	output.close()
	input.close()



if __name__ == '__main__':
	main()
