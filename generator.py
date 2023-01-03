#!/usr/bin/env python

"""Tento program generuje pdf soubory se zadáním čtyř úloh do písemky pomocí LaTeXu. 
Jména studentů načítá z csv souborů ve složce data.
Studenti jsou rozděleni do čtyř skupin."""

import glob
from producePDF import *


def main():
    print("Generátor písemek")
    print("Created by Miroslav Burýšek, 2021")
    
    print("Načítání seznamu studentů...")
    skupiny = glob.glob("./data/*.csv")
    seznam_studentu = []

    for cviceni in skupiny:
        with open(cviceni, "r") as r:
            for line in r:
                seznam_studentu.append((cviceni[14:17], line[:-1]))
    print("Seznam studentů vytvořen.")
    
    
    rm_in_pdf()
    for student in seznam_studentu:
        cv, jmeno = student
        create_pdf(cv, jmeno)


if __name__ == "__main__":
    main()

# V TERMINÁLU: for soubor in *pisemka.tex do pdflatex $soubor;done # zkompiluje tex
