def chiffrer_avec_cle(text, key):
    encrypted_text = []
    for char in text:
        if char in key:
            encrypted_text.append(key[char])
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

# Clé de substitution
update = {'t': 'i','i':'s','.':'q','s':'t'}

# Texte à chiffrer
text ='en mq cgarlei francoti btenvenu myrtel esats eve.ue de dthneqc esats un vtetllard d envtron iotxanse.utnze ani tl occupats le itehede dthne deputi q.uot.ue ce desatl ne soucge en aucune mantere au fond meme de ce .uenoui avoni a raconser tl n eis peusesre pai tnustle ne fusce .uepour esre exacs en sous d tndt.uer tct lei brutsi es lei propoi .utavatens couru iur ion compse au momens ou tl esats arrtve dani ledtoceieq vrat ou faux ce .u on dts dei gommei stens iouvens ausans deplace dani leur vte es iursous dani leur deistnee .ue ce .u tli fonsq mqmyrtel esats ftli d un conietller au parlemens d atx nobleiie de robeqon consats de lut .ue ion pere le reiervans pour gertser de ia cgarhe l avats marte de fors bonne geure a dtxguts ou vtnhs ani iutvans unuiahe aiiez repandu dani lei famtllei parlemensatreiq cgarlei myrtel nonobisans ce martahe avats dtiatson beaucoup fats parler de lutq tlesats bten fats de ia perionne .uot.ue d aiiez pestse satlle elehans hracteux iptrtsuel souse la premtere parste de ia vte avats ese donneeau monde es aux halanserteiq la revoluston iurvtns lei evenemensi ieprectptserens lei famtllei parlemensatrei dectmeei cgaiieei sra.ueei ie dtiperierensq mq cgarlei myrtel dei lei premteri jouri de larevoluston emthra en tsalteq ia femme y mourus d une maladte depotsrtne dons elle esats assetnse deputi lonhsempiq tli n avatens potnsd enfansiq .ue ie paiiastl'
# Chiffrement du texte
encrypted_text = chiffrer_avec_cle(text, update)
print(encrypted_text)
