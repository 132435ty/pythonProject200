list = [
    "<li>Hello</li>",
    "<li>I</li>",
    "<li>Am</li>",
    "<li>A</li>",
    "<li>Robot</li>",
    "<li>Привет</li>",
    "<li>Это</li>",
    "<li>статья</li>",
    "<li>пуста</li>",
    "<li>извини</li>",
    "<li>пожалуста</li>"
]

cleanedlist = [x.replace("<li>", "").replace("</li>", "")
               for x in list]

print(cleanedlist)
