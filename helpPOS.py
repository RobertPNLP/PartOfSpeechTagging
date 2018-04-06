import nltk

def POS_info(POS):
    info = nltk.help.upenn_tagset(POS)
    try:
        print(POS + ' ' + info)
    except:
        pass
