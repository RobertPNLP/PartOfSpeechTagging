import nltk

def POS_info(POS_setList):
    info = nltk.help.upenn_tagset(POS_setList)
    try:
        print(POS_setList + ' ' + info)
    except:
        pass
