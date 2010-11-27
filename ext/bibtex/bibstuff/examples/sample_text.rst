*********************************************************************
Example Text to test literature
*********************************************************************

While you can create and save documents in the OpenDocument format using OpenOffice.org, KWord, or AbiWord, there are other ways to generate ODF files. odtwriter, for example, can help you quickly convert plain text files formatted using reStructured Text markup into ODT (OpenOffice.org Writer-compatible ODF) documents. Using odtwriter, you can generate ODF files on machines that don't have ODF-compatible word processors installed, such as those running lightweight Linux distros, or simply compose documents in a text editor and leave the task of properly formatting them to odtwriter. [colu92]_

odtwriter is part of docutils, a set of tools for converting plain text files into other formats, such as HTML, XML, and LaTeX. This means that you can output the formatted text file into other formats besides ODF. This is a more efficient approach than creating an ODT document in Writer and then jumping through hoops to turn it into, for example, a clean HTML file. [isaac.schwilk-2010]_

odtwriter has a few features that are not available in OpenOffice.org. For example, OpenOffice.org doesn't support syntax highlighting, so making code blocks in a Writer document more legible and pretty is a non-trivial task. odtwriter, however, can apply syntax highlighting to the code blocks in the final ODT document. [smit54]_