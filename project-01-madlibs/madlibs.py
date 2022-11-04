from random import randint
import copy 

madlib = (   
  "<hero> is a {} superhero dedicated to \n" +
    "{} germs and {}. He has a \n" +
    "{} costume made of {} and it \n" +
    "protects him against {} {}. \n" +
    "One day, <hero> got a call from his friend {} \n" +
    "who told him that a {} villain had taken \n" +
    "over the town. When <hero> {} to the scene,\n" +
    "he found {} <villain>! The \n" +
    "<villian> was {} by germs and disease \n" +
    "everywhere, touching every {}. \n" +
    "{} , <hero>  and his gleam team went after \n" +
     "<villain> and his army of {} germs. \n" +
    "In the end,  <hero> won the {} battles with \n"
    "<villain> and saved the {} from disease. \n" 
)


word_lib = {
    'adjective':['brave','dangerous','crazy','cheerful','beautiful','charming','juicy','thick','holy','hostile','jinxed', 'impressive',],
    'verb':['slide','followed','haunted','tampered','swallowed','beaten','behaved','fried','consider','closed','greeted','slowed',],
    'noun':['charity','cat','planet','lawyer','monkey','eggplant','rose','horse','school', 'babies','rats','grapes','socks','trees'],
    'color':['blue','pink','purple','green','brown','black','cyan','navy', 'red','teal','coral','gold','black','silver'],
    'name':['Jazmin','David','Artur','Sam','Eva','Jayden','Kai','Melissa','Samaria','Jhoanna'],
    'adverb':['quickly','slowly','rarely','yesterday','last month'],
    'number':['10','40,000','21','54','23','890,239','1,000,000'],
    'plural noun': ['geese','teeth','feet','children','women','nuclei', 'fungi'],

}

def have_words(type,madlib_words):
    words = madlib_words[type]
    count = len(words)-1
    index = randint (0,count)
    return madlib_words[type].pop(index)

def create_madlib():
    local_dict = copy.deepcopy(word_lib)
    return madlib.format(
        have_words('adjective',word_lib),
        have_words('verb', word_lib),
        have_words('noun', word_lib),
        have_words('color',word_lib),
        have_words('noun',word_lib),
        have_words('adjective',word_lib),
        have_words('noun', word_lib),
        have_words('name',word_lib),
        have_words('adjective',word_lib),
        have_words('verb',word_lib),
        have_words('adjective',word_lib),
        have_words('verb',word_lib),
        have_words ('noun',word_lib),
        have_words('adverb',word_lib),
        have_words ('number',word_lib),
        have_words('adjective',word_lib),
        have_words('plural noun',word_lib)
    )

print("MADLIB: ")
print(create_madlib())
