ENGLISH VERSION BELOW
------------------------------------------------------------------------
Lai palaistu kodu biežāk sastopamo vārdu iegūšanai ar noteiktiem sākumburtiem konkrētā teksta korpusā, jāizpilda komanda:

_python Text_predictor.py arg1 arg2 arg3_

kur \
    python - interpretators programmas koda palaišanai,\
    Text_predictor.py - programmas koda datnes nosaukums,\
    arg1 - teksta korpusa nosaukums,\
    arg2 - meklējamie sākumburti,\
    arg3 - pilna vai nepilna teksa korpusa izmantošanas indikators.

Piemēram:

_python Text_predictor.py blogs.txt jo full_

kas attiecīgi izmantos blogs.txt datni, meklēs vārdus, kas sākas ar burtiem "jo", un izmantos pilnu datnē esošo tekstu.

Ja netiek ievadīti argumenti, tad programma izpildīsies ar noklusētajiem parametriem, t.i. izmantos datni tweets.txt, sākumburtus "no" un daļēju teksta apjomu - pirmās 2000 rindas.

------------------------------------------------------------------------
To run the code for extracting the most frequent words with specific starting letters in a given text corpus, execute the command:

_python Text_predictor.py arg1 arg2 arg3_

where:\
    python - the interpreter for running the program code,\
    Text_predictor.py - the name of the program's code file,\
    arg1 - the name of the text corpus,\
    arg2 - the starting letters to search for,\
    arg3 - an indicator for using the full or partial text corpus.

For example:

_python Text_predictor.py blogs.txt jo full_

This will use the file blogs.txt, search for words starting with the letters "jo", and process the entire text in the file.

If no arguments are provided, the program will run with default parameters, i.e., it will use the file tweets.txt, the starting letters "no", and a partial text amount — the first 2000 lines.
