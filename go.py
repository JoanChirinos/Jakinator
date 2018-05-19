#! /usr/bin/python

import cgi, cgitb

cgitb.enable()

print 'Content-type: text/html\n\n'

def go():
    fs = cgi.FieldStorage()
    toAdd = [fs.getvalue("newCharacter", "help"), fs.getvalue("question", "help pls"), fs.getValue("oldCharacter", "help pl0x")]
##
##    straw = open("qa.txt", "rU")
##    oldFile = straw.read()
##    straw.close()

    goingToAdd = "\n" + toAdd[1] + "\n" + toAdd[2] + "\n" + toAdd[0]

    print "<html><body><p>" + goingToAdd + "</p></body></html>"
    
##
##    oldFile += goingToAdd
##
##    straw = open("qa.txt", "w+")
##    straw.write(oldFile)
##    straw.close()
##    print """
##                <html>
##                    
##                    <head>
##                        <title>College Trip Playlist</title>
##                        <script type="text/javascript">
##                            window.location.replace("thanks.html");
##                        </script>
##                        <link href="style.css" type="text/css" rel="stylesheet">
##                    </head>
##                    
##                    <body>
##                    </body>
##                    
##                </html>"""

go()
