Lai palaistu kodu biežāk sastopamo vārdu iegūšanai ar noteiktiem sākumburtiem konkrētā teksta korpusā, jāizpilda komanda

_python Text_predictor.py arg1 arg2 arg3_

kur python - interpretators programmas koda palaišanai/n
    Text_predictor.py - programmas koda datnes nosaukums
    arg1 - teksta korpusa nosaukums
    arg2 - meklējamie sākumburti
    arg3 - pilna vai nepilna teksa korpusa izmantošanas indikators

Piemēram:

_python Text_predictor.py blogs.txt jo full_

kas attiecīgi izmantos blogs.txt datni, meklēs vārdus, kas sākas ar burtiem "jo", un izmantos pilnu datnē esošo tekstu.

Ja netiek ievadīti argumenti, tad programma izpildīsies ar noklusētajiem parametriem, t.i. izmantos datni tweets.txt, sākumburtus "no" un daļēju teksta apjomu - pirmās 2000 rindas.
