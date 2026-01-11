# Dada uma tupla de anos (ex: 1990, 2024), diga quais são do século XXI.

anos = (1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999,
        2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009)

for ano in anos:
    if ano >= 2001:
        print(f'O ano {ano} pertence ao século 21!')