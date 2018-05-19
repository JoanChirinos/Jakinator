#! /usr/bin/python

import cgi, cgitb

cgitb.enable()

print 'Content-type: text/html\n\n'

def go():
    fs = cgi.FieldStorage()
    toAdd = []
    
    for i in fs.keys():
        toAdd += [fs.getvalue(i)]

    #opens the question/answer storage
    #ID1,Q<question>
    #ID2,A<answer>
    #ID3,Q<question>
    #...
    straw = open("../qa.txt", "rU")
    oldFile = straw.read()
    straw.close()

    #formats what it's going to add
    goingToAdd = "\n" + toAdd[1] + "\n" + toAdd[2] + "\n" + toAdd[0]

    #splits the old questions and answers and the IDs
    #[[ID1, Q<question>], [ID2, A<answer>], [ID3, Q<question>], ...]
    oldFile = [i.split(",") for i in oldFile.split("\n")]

    #creates a dictionary to make finding the ID we need to change easier (for me)
    #why change an ID? when the program guesses the wrong character, it needs
    #to change the "node" from an answer "node" to a question "node". So it
    #changed the data stored in the ID from A<answer> to Q<question>
    #
    #The IDs are in the form 01001 (in the sense that it's like binary) because
    #the program is kinda like a binary tree (each question has a yes or no).
    #After the user answers a question, if the answer is yes, it looks at the
    #node with the question's ID + "1". If the answer if no, it looks at the
    #node with the question's ID + "0".
    d = {}
    for i in oldFile:
        if len(i) == 2:
            d[i[0]] = i[1]

    #this adds the new info into the dictionary, replacing the data at the old
    #answer's ID with the new question, then adding the new answer and the old
    #answer (both with new IDs)
    for x in toAdd:
        t = x.split(",")
        d[t[0]] = t[1]

    #now just fixing up formatting...
    newFile = [i + ',' + d[i] for i in d.keys()]
    newFile = '\n'.join(newFile)
    #and writing the file
    straw = open("qa.txt", "w+")
    straw.write(newFile)
    straw.close()

    #now we print the html to redirect to thanks.html, which just has another
    #script that closes the window in 5 seconds. This redirect is so the user
    #doesn't have time to mess around with the address bar and input weird info
    #and I'm pretty sure the history of even opening the go.py page is deleted
    #from the browser history
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

#go!
go()
