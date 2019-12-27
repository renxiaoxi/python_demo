import requests
from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer as ss
import sys

#LLIE
# if len(sys.argv) > 2 :
#     for argv in sys.argv:
        
#         if argv == '--a' :
#             print('1')
#             exit(-1)
#         else:
#             print('2')
#             exit(-1)
        # elif argv == '--b' :
        #     print('2')
        #     exit(-1)
        # else:
        #     print('3')
        #     exit(-1)

url = "https://dictionary.cambridge.org/dictionary/english-chinese-simplified/"

if len(sys.argv) > 1 and sys.argv[1] == '--help':
        print('''
if you wanna quit, please enter "qt"
        ''')

word = input('> ')

while word != 'qt':
    
    # try:
    #     word = input('> ')
    #     # word = sys.argv[1]    
    # except:
    #     print("Specify the word!")
    #     exit(-1)
    
        

    url = url + word

    print('please wait ...')

    try:
        r = requests.get(url)
        soup = bs(r.content,"lxml")
    
    except:
        print("Not connect to the internet")
        exit(-1)





    # check there is a result
    isExistResults = len(soup.find_all("div", {"class":"entry-body"}))
    # print(soup_word_block.select(".di-title")[0].text)
    if not isExistResults:
        exit(-1)
        print('there is no such a word here! please check it and enter again')
    # is a word or a phrase
    # isAWord = len(soup.find_all("div",{"rel":word})) 
    print('*'*32,'\n') 
    print("--" + word + "--")



    try:
    
        blocks = soup.select(".pr.entry-body__el")
        blockobj = {}
        for block in blocks:
            
            pos = block.select('.posgram.dpos-g')[0].text
            blockobj[pos]={}
            ipa_uk = block.select("span.uk.dpron-i span.pron.dpron")[0].text
            ipa_us = block.select("span.us.dpron-i span.pron.dpron")[0].text        
            blockobj[pos]['ipa'] = ipa_uk

            definitions = []
            if len(block.select(".pos-body .def-block")):
                define_block = block.select(".pos-body .def-block")
                for definition in define_block:
                    __obj={}
                    __obj['En'] = definition.select(".def.ddef_d.db")[0].text
                    __obj['Cn'] = definition.select(".def-body.ddef_b > span")[0].text
                    definitions.append(__obj)

            blockobj[pos]['definition'] = definitions
            
            

            if len(sys.argv) > 2 and sys.argv[2] == '--p':
                phrases = []
                if len(block.select(".phrase-block")):
                    phrase_block = block.select(".phrase-block")
                    for phrase in phrase_block:
                        __obj={}
                        __obj['title'] = phrase.select('span.phrase-title')[0].text
                        __obj['En'] = phrase.select(".def.ddef_d.db")[0].text
                        __obj['Cn'] = phrase.select(".def-body.ddef_b > span")[0].text
                        phrases.append(__obj)
                blockobj[pos]['phrases'] = phrases

            if len(sys.argv) > 2 and sys.argv[2] == '--i':
                idioms = []
                if len(block.select(".xref.idioms")):
                    idiom_block = block.select(".xref.idioms")
                    for idiom in idiom_block:
                        __obj={}
                        __src = idiom.select('.item > a')[0]['href']
                        __r = requests.get(__src)
                        __soup = bs(__r.content,'lxml')
                        cn = __soup.select('.idiom-block span.trans')[0].text
                        __obj['src'] = idiom.select('.item > a')[0]['href']
                        __obj['Cn'] = cn
                        __obj['title'] = idiom.select(".item ")[0].text
                        idioms.append(__obj)

                blockobj[pos]['idioms'] = idioms

            # if len(block.select(".xref.idioms")):
            #     idioms = block.select(".xref.idioms .item")
            # else:
            #     idioms = []
            # blockobj[pos]['idioms'] = idioms
            
        print(blockobj)
        res = {}    
        for sub in blockobj: 
            for key, val in sub.items():  
                res.setdefault(key, []).append(val) 
        print(str(res))

    except:
        print('there is something wrong') 

    print('\n')
    print('*'*32,'\n') 


