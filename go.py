#! /usr/bin/python

import cgi, cgitb

cgitb.enable()

print 'Content-type: text/html\n\n'

def go():
    fs = cgi.FieldStorage()
    toAdd = [fs.getvalue("newCharacter"), fs.getvalue("question"), fs.getValue("oldCharacter")]

    straw = open("qa.txt", "rU")
    oldFile = straw.read()
    straw.close()

    oldFile += "\n" + toAdd[1] + "\n" + toAdd[2] + "\n" + toAdd[0]

    straw = open("qa.txt", "w+")
    straw.write(oldFile)
    straw.close()

    print """
                <html>
                    
                    <head>
                        <title>College Trip Playlist</title>
                        <script type="text/javascript">
                            window.location.replace("thanks.html");
                        </script>
                        <link href="style.css" type="text/css" rel="stylesheet">
                    </head>
                    
                    <body>
                    </body>
                    
                </html>"""