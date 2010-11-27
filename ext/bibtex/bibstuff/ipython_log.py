#log# Automatic Logger file. *** THIS MUST BE THE FIRST LINE ***
#log# DO NOT CHANGE THIS LINE OR THE TWO BELOW
#log# opts = Struct({'__allownew': True,
 'editor': 'notepad++.exe',
 'logfile': 'ipython_log.py',
 'profile': 'sh',
 'q4thread': 1})
#log# args = []
#log# It is safe to make manual edits below here.
#log#-----------------------------------------------------------------------
_ip.magic("logstart ")

import bib4txt.py
import bib4txt
from bibstyles import default
bibstyles.default as style
import bibstyles.default as style
import bibfile, bibgrammar, bibstyles
bibfile_processor = bibfile.BibFile()
bibfile_as_string = open('examples/sample.bib','r').read()
bibfile_as_string
bibgrammar.Parse(bibfile_as_string, bibfile_processor)
bibfile_processor()
bibfile_processor()
parsed_bibfile=bibfile_processor
citation_manager = style.CitationManager([parsed_bibfile], keys=None, citation_template=style.CITATION_TEMPLATE)
citation_manager()
citation_manager
result = citation_manager.make_citations()
#?citation_manager.biblist
citation_manager.biblist
citation_manager.biblist()
citation_manager.citekeys
#?citation_manager.citekeys
_ip.magic("whos ")
citation_manager.get_entries()
#?citation_manager.get_entries
parsed_bibfile()
parsed_bibfile.name()
#?parsed_bibfile.name
bibfile_as_string
#?citation_manager.format_citation
result = citation_manager.make_citations()
cite_processor = bibstyles.shared.CiteRefProcessor(citation_manager)
taglist = src_parser.parse(src_as_string,processor=cite_processor)
#?citation_manager.get_citation_label
citation_manager.get_citation_label('smit54')
bibfile_processor.get_entrylist()
bibfile_processor.get_entrylist()
#?bibfile_processor.get_entrylist
bibfile_processor.get_entrylist(['smit54'])
bibfile_processor.get_entrylist([])
bibfile_processor.get_entrylist([:])
bibfile_processor.get_entrylist()
#?bibfile_processor.search_entries
bibfile_processor.search_entries(*)
#?bibfile_processor.name
#?bibfile_processor.entries
bibfile_processor.entries()
bibfile_processor.entries
entries 
entries = bibfile_processor.entries
#?bibgrammar.Parse
bibgrammar.Parse(bibfile_as_string, bibfile_processor)
bibgrammar.Parse(bibfile_as_string, bibfile_processor)
bibfile_processor.get_entrylist()
#?bibfile_processor.get_entrylist
bibfile_processor.entry()
#?bibfile_processor.entry
bibfile_processor.entries
cite_processor = bibstyles.shared.CiteRefProcessor(citation_manager)
citation_manager.make_citations()
citation_manager.make_citations()
citation_manager.make_citations('smit54')
#?citation_manager.make_citations
citation_manager.make_citations(['smit54'])
citation_manager.make_citations([smit54])
#?citation_manager.make_citations
citation_manager.make_citations([smit54])
cite_processor.all_citekeys
cite_processor.all_citekeys()
cite_processor = bibstyles.shared.CiteRefProcessor(citation_manager)
citation_manager = style.CitationManager([parsed_bibfile], keys=None, citation_template=style.CITATION_TEMPLATE)
citation_manager._keys
citation_manager._keys()
#?citation_manager
#?citation_manager._keys
citation_manager.biblist
#?citation_manager.biblist
citation_manager.biblist
citation_manager.biblist.count()
citation_manager.biblist.count()
#?citation_manager.citekeys
citation_manager.citekeys('smit54')
citation_manager.make_citations()
import bibfile, bibgrammar, bibstyles
cite_processor = bibstyles.shared.CiteRefProcessor(citation_manager)
input = open('examples/rst_input.txt','r')
src_as_string = input.read()
taglist = src_parser.parse(src_as_string,processor=cite_processor)
ebnf_dec = ebnf_sp.cites_rest
import ebnf_sp
ebnf_dec = ebnf_sp.cites_rest
taglist = src_parser.parse(src_as_string,processor=cite_processor)
ebnf_dec = ebnf_sp.cites_rest
cite_parser = simpleparse.parser.Parser(ebnf_dec, root='src')
import simpleparse
cite_parser = simpleparse.parser.Parser(ebnf_dec, root='src')
taglist = src_parser.parse(src_as_string,processor=cite_processor)
src_parser=cite_parser = simpleparse.parser.Parser(ebnf_dec, root='src')
taglist = src_parser.parse(src_as_string,processor=cite_processor)
taglist
result = citation_manager.make_citations()
entries
#?result = citation_manager.make_citations
#?citation_manager.make_citations
citation_manager.make_citations(entries)
myres = citation_manager.make_citations(entries)
_ip.system("dir /on ")
out = open('examples\sample_rst.txt', 'w')
out.write(myres)
out.close()
_ip.magic("hist ")
entries
entries.sort()
#?entries.sort
entries
#?sys.path.append
import sys
#?sys.path.append
#?sys.path
import os
#?os.walk
import os
from os.path import join, getsize
for root, dirs, files in os.walk('python/Lib/email'):
    print root, "consumes",
    print sum(getsize(join(root, name)) for name in files),
    print "bytes in", len(files), "non-directory files"
    if 'CVS' in dirs:
   	
    pass
for root, dirs, files in os.walk('python/Lib/email'):
    print root, "consumes",
    print "bytes in", len(files), "non-directory files"
    
#?os.walk
os.walk(.)
os.walk('.')
for files in os.walk('.'):
    print files
    
    print files
for files in os.walk('.'):
    print files[0]
    
#?os.walk
for files in os.walk('.'):
    print files[0]
    
_ip.magic("pwd ")
r = open('bib4txt.py', 'r')
l = open('./bibname.py', 'r')
f = []
r.read()
r.read()+l.read()
result
_ip.magic("whos ")
