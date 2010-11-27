import os,sys
import logging
logging.basicConfig(format='\n%(levelname)s:\n%(message)s\n')
bib4txt_logger = logging.getLogger('bibstuff_logger')

#import dependencies
import simpleparse

#local imports
import bibfile, bibgrammar, bibstyles
import bibstyles.default as style
import ebnf_sp

bibfile_processor = bibfile.BibFile()
bibfile_as_string = open('examples/sample.bib','r').read()
bibgrammar.Parse(bibfile_as_string, bibfile_processor)
entries = bibfile_processor.entries

parsed_bibfile=bibfile_processor
citation_manager = style.CitationManager([parsed_bibfile], keys=None, citation_template=style.CITATION_TEMPLATE)
citation_manager.make_citations(entries)
myres = citation_manager.make_citations(entries)
out = open('examples\sample_rst.txt', 'w')
out.write(myres)
out.close()