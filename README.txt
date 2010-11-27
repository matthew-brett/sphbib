===========================
bibtex extension for sphinx
===========================

This is a version of the bibtex sphinx extension put up on the sphinx
bugtracker - see `Issue 63
<http://bitbucket.org/birkenfeld/sphinx/issue/63/make-sphinx-read-bibtex-files-for>`_. 

The files here are from the ``test_bibtex.zip`` file put up as an attachment to
that issue.  The author is Tim Michelsen, and he's using code from the
`bibstuff package <http://code.google.com/p/bibstuff>`_.  I (MB) have a more
accessible mirror of bibstuff at
http://gitorious.org/google-code-svn-clones/bibstuff

Purpose
========

Collect all citations within the source docs and 
docstrings.
Assesmble a document with the used references from
a bibtex data base file.

Status
=========
* works on documents in source
* references also citations in docstrings

ToDo
========
* parse docstrings in order to compile references only
of the used citations
* Reformat the citation links:
    * assign a title instead of the bibtex key
    * example: [smith54]_ =>
       `Smith et al. (1954) <smith>`_
