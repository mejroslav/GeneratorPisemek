
import os
from ulohy import *


def rm_in_pdf():
    """Remove all files in 'pdf' folder."""
    os.system("rm pdf/*")




def create_pdf(cv: str, jmeno: str):
    """Given group and student's name, create pdf file with the exam sheet."""

    def LaTeX_to_pdf(filename: str):
        os.chdir("./pdf")
        """Compile LaTeX and remove obsolete files."""
        print("Probíhá kompilace LaTeX -> pdf...")

        try:
            os.system(f"pdflatex {filename} {filename[:-4]}.pdf")  # kompilace LaTeX
            print(f"Soubor {filename[:-4]}.pdf úspěšně vytvořen.")

            print("Odstraňování zbytečných souborů...")
            os.system(f"rm {filename1}")
            os.system(f"rm {filename2}")
            os.system(f"rm {filename3}")
            os.system(f"rm {filename4}")
            os.system(f"rm {filename_hlavicka}")
            os.system(f"rm {filename} {filename[:-4]}.aux")
            os.system(f"rm {filename} {filename[:-4]}.log")
            os.system(f"rm {filename} {filename[:-4]}.out")
            os.system(f"rm {filename} {filename[:-4]}.fls")
            print("Odstraňování dokončeno.")
        except OSError as err:
            print("Došlo k chybě: ", err)
            
        os.chdir("..")

    
    filename1 = f"{cv}_{jmeno}_u1.tex"
    filename2 = f"{cv}_{jmeno}_u2.tex"
    filename3 = f"{cv}_{jmeno}_u3.tex"
    filename4 = f"{cv}_{jmeno}_u4.tex"
    filename_hlavicka = f"{cv}_{jmeno}_head.tex"
    filename_total = f"{cv}_{jmeno}.tex"

    uloha1("./pdf/" + filename1)
    uloha2("./pdf/" + filename2)
    uloha3("./pdf/" + filename3)
    uloha4("./pdf/" + filename4)
    hlavicka("./pdf/" + filename_hlavicka, jmeno)

    text_pisemky = f"""
\\documentclass{{article}}
\\usepackage[
nochapters, % Turn off chapters since this is an article        
beramono, % Use the Bera Mono font for page numbers in the table of contents
]{{classicthesis}} % The layout is based on the Classic Thesis style
\\usepackage{{arsclassica}} % Modifies the Classic Thesis package
\\usepackage[T1]{{fontenc}} % Use 8-bit encoding that has 256 glyphs
\\usepackage[utf8]{{inputenc}} % Required for including letters with accents
%--------------------------------------------------------------
% Fonts and languages
\\usepackage{{libertinus}} % The Libertinus font

\\usepackage[czech]{{babel}} % Český jazyk
\\usepackage{{graphicx}} % Required for including images
\\usepackage{{enumitem}} % Required for manipulating the whitespace between and within lists
\\usepackage{{amsmath,amssymb,amsthm,amsfonts}} % For including math equations, theorems, symbols, etc
\\usepackage[top =3 cm, bottom = 3.5 cm, left = 1.5 cm, right = 1.5 cm]{{geometry}}
\\usepackage{{mathtools}}
\\usepackage{{float}}
\\usepackage{{caption}}
\\usepackage{{color}}
\\usepackage{{hyperref}}

\\newcommand{{\\arctg}}{{\\mathrm{{arctg}}\\,}}

\\title{{Průběžný test z matematiky}}
\\date{{}}

\\begin{{document}}
    \\maketitle
    ~
    \\input{{{filename_hlavicka}}}
    

    \\textbf{{Úloha 1. (3 body)}}
    \\input{{{filename1}}}
    
    \\textbf{{Úloha 2. (2 body)}}
    \\input{{{filename2}}}
    
    \\textbf{{Úloha 3. (3 body)}}
    \\input{{{filename3}}}

    \\textbf{{Úloha 4. (4 body)}}
    \\input{{{filename4}}}
\\end{{document}}
        """

    with open("./pdf/" + filename_total, "w") as cela_pisemka:
        print(text_pisemky, file=cela_pisemka)

    LaTeX_to_pdf(filename_total)
