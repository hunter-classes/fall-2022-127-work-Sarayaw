#capitalization extra
pirate_lang={
"hello": "ahoy",
"guys": "scurvy dogs",
"before": "afore",
"earlier": "afore",
"the": "th",
"are": "be",
"yes": "aye",
"friend": "matey",
"my": "me",
"your": "yer",
"you":"ye",
"is":"be",
"there":"yonder",
"captain":"cap'n",
"story":"tale",
"stories":"tales"
}

fresh_w=[]

with open("input.txt") as text:
    bar = text.readlines()
    new_bars=' '.join(bar)
    eng_lang = new_bars.split() #splits text into a list of different words
    for term in eng_lang:
        if term[0].isupper() and term.lower() in pirate_lang: #capitalizes the words (extra)
          new_term= pirate_lang [term.lower()]
          fresh_w.append(new_term.capitalize())
        elif term in pirate_lang: #gets back original statements
          fresh_w.append(pirate_lang[term])
        else:
          fresh_w.append(term)
    text = ' '.join(fresh_w) #joins from fresh_w and makes new string
print(text)
