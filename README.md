# Generátor písemek

Tento program byl vytvořen pro generování zadání písemných prací pro studenty VŠE. Ve složce `data` jsou uloženy soubory se seznamy jmen studentů ve formátu csv. Po spuštění `generator.py` se ve složce `pdf` vytvoří ke každému studentovi TeXový soubor se zadáním a následně se sám zkompiluje do formátu pdf.

---

V současné podobě funguje pouze na operačním systému LINUX.

---

### Použití:

- Do složky `data` nahrajte soubory s příjmeními studentů ve tvaru `seznam-{skupina}.csv`.
- Spusťte program `generator.py`. Ve složce `pdf` se budou vytvářet pdf soubory se zadáním.