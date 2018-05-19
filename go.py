#! /usr/bin/python

import cgi, cgitb

cgitb.enable()

print 'Content-type: text/html\n\n'

def go():
    fs = cgi.FieldStorage()

    toAdd = []
    
    #print "<html><body>"
    for i in fs.keys():
        toAdd += [fs.getvalue(i)]

    #print "</body></html>"

    #toAdd = [fs.getvalue("newCharacter"), fs.getvalue("question"), fs.getValue("oldCharacter")]

    straw = open("qa.txt", "rU")
    oldFile = straw.read()
    straw.close()

    goingToAdd = "\n" + toAdd[1] + "\n" + toAdd[2] + "\n" + toAdd[0]

    print "<html><body><p>" + goingToAdd + "</p></body></html>"

    

    oldFile = [i.split(",") for i in oldFile.split("\n")]

    d = {}
    for i in oldFile:
        if len(i) == 2:
            d[i[0]] = i[1]

    for x in toAdd:
        t = x.split(",")
        d[t[0]] = t[1]

    newFile = [i + ',' + d[i] for i in d.keys()]
    newFile = '\n'.join(newFile)

    straw = open("qa.txt", "w+")
    straw.write(newFile)
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

go()
