from numpy import random

# Generování souborů s úlohami

def uloha1(filename: str):
    with open(filename, "w") as file_u1:
        # prvni dve kvuli slozene zavorce, posledni kvuli nazvu promenne

        zadani1 = f"""  Nalezněte řešení soustavy rovnic a zapište ho ve vektorovém tvaru.
    {rnd_uloha1()}
        """
        print(zadani1, file=file_u1)


def uloha2(filename: str):
    zadani2 = f"""
    Vypočítejte determinant:
    {rnd_uloha2()}
        """
        
    with open(filename, "w") as file_u2:
        print(zadani2, file=file_u2)   

    

def uloha3(filename: str):
    m,n,p,r = rnd_uloha3()
    
    zadani3 = f"""
    Vypočítejte limitu:
    \\begin{{align*}}
    \\lim_{{ x \\rightarrow -\\infty }} \\arctg \\left( \\frac{{ x^{{ {2*m} }} + 2x^{{ {m} }} - 1 }}{{ {r} x^{{ {2*n} }} + x^{{ {n} }} + 1  }} \\right) \\cdot e^{{ x^{{{p}}} }}
    \\end{{align*}}
    """
    
    with open(filename, "w") as file_u3:
        print(zadani3, file=file_u3)


def uloha4(filename: str):
    u,v = rnd_uloha4()

    zadani4 = f"""Mějme funkci danou předpisem
\\begin{{align*}}
    f(x)= \\frac{{ {v} }}{{x}} - \\frac{{ {u*v} }}{{ x^2 }} \\:.
\\end{{align*}}
\\begin{{itemize}}
    \\item Určete $D_f$, $f'(x)$ a $f''(x)$.
    \\item Určete, na jakých intervalech je funkce rostoucí a klesající.
    \\item Nalezněte minimum a maximum funkce na uzavřeném intervalu $[1,{3*u}]$.
    \\item Řešením rovnice $f''(x)=0$ nalezněte inflexní bod funkce.
\\end{{itemize}}
    """
    
    with open(filename, "w") as file_u4:
        print(zadani4, file=file_u4)


def hlavicka(filename: str, jmeno: str):
    text = f"""\\textbf{{Příjmení: {jmeno} }}\\\\
\\textbf{{Cvičení: }}\\\\
\\textbf{{Datum: }}\\\\
\\textbf{{Počet bodů: }}\\\\
    """
    
    with open(filename, "w") as w: 
        print(text, file=w)




# Tvorba náhodných proměnných do jednotlivých příkladů

def rnd_uloha1():
        # Vytvořím 5 různých soustav
    sou1 = f"""
    \\begin{{align*}}
        x+y-2u&=3 \\\\
        y+z&=1 \\\\
        x+2y+z+u&=4\\\\
        x-z-2u&=2\\\\
        3x+y-2z-6u&=7
    \\end{{align*}}
    """

    sou2 = f"""
    \\begin{{align*}}
        x+y-z-u&=5 \\\\
        2x-y+z+2u &= 3 \\\\
        -7x+7y+7z-7u&=-7\\\\
        x+2y-z+u&=4\\\\
    \\end{{align*}}
    """

    sou3 = f"""
    \\begin{{align*}}
        x-y-z-v-w&=1 \\\\
        x+y+z+v-w&=2 \\\\
        y-w&=-1
    \\end{{align*}}
    """

    u1 = [sou1, sou2, sou3]
    return random.choice(u1)
    
def rnd_uloha2():
    mat1 = f"""
    \\begin{{align*}}
        \\begin{{vmatrix}}
            3 & -2 & 4 & 5\\\\
            0 & -1 & 0 & -2\\\\
            1 & -3 & 1 & 2\\\\
            2 & 4 & 3 & 0
        \\end{{vmatrix}}
    \\end{{align*}}
    """

    mat2 = f"""
    \\begin{{align*}}
        \\begin{{vmatrix}}
            2 & 2 & 2 & 1\\\\
            1 & 0 & 4 & -3\\\\
            1 & -1 & -1 & 0\\\\
            1 & -1 & 3 & 0
        \\end{{vmatrix}}
    \\end{{align*}}
    """

    mat3 = f"""
    \\begin{{align*}}
        \\begin{{vmatrix}}
            2 & 5 & 0 & -1\\\\
            -1 & 2 & 1 & 4\\\\
            1 & 1 & -3 & 1\\\\
            1 & 2 & 0 & -1
        \\end{{vmatrix}}
    \\end{{align*}}
    """

    mat4 = f"""
    \\begin{{align*}}
        \\begin{{vmatrix}}
            -5 & 0 & -2	& 1 \\\\
            1 &	1 & 3 & -5 \\\\
            -2 & 0 &-1 & 2 \\\\
            2 &	-1 & 0 & 1
        \\end{{vmatrix}}
    \\end{{align*}}
    """

    mat5 = f"""
    \\begin{{align*}}
        \\begin{{vmatrix}}
            1 & -2 & 0 & 1 \\\\
            1 & 4 & -3 & 4 \\\\
            0 & 2 & -2 & 0 \\\\
            1 &	1 & -1 & 1
        \\end{{vmatrix}}
    \\end{{align*}}
    """
    
    return random.choice([mat1, mat2, mat3, mat4, mat5])

def rnd_uloha3():
    m = random.randint(4, 7)
    n = random.randint(2, 3)
    p = random.randint(3, 8)
    r = random.randint(-9, 9)
    if (r == 0):
        r = -3
    if (r == 1):
        r = ""
    if (r == -1):
        r = "-"
    return (str(m),str(n),str(p),str(r))

def rnd_uloha4():
    u = random.randint(1, 4)
    v = random.randint(1, 4)
    return (u,v)



