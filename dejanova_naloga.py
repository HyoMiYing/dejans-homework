#1

def v_pot(niz):
    seznam_premikov = niz.split(' ')
    seznam_premikov_v_terkah = []
    for premik in seznam_premikov:
        seznam_premikov_v_terkah.append((premik[0], int(premik[1:])))
    return seznam_premikov_v_terkah

#2 Točka

slovar_smeri = {
    '<' : (-1, 0),
    '>' : (1, 0),
    '^' : (0, 1),
    'v' : (0, -1),
}


def odsek(x_koordinata, y_koordinata, smerni_znak, razdalja_potovanja):
    seznam_terk = [(x_koordinata, y_koordinata)]
    for korak in range(int(razdalja_potovanja)):
        for index, element_terke in enumerate(slovar_smeri[smerni_znak]):
            if index == 0:
               x_koordinata = x_koordinata + element_terke
            elif index == 1:
               y_koordinata = y_koordinata + element_terke
        seznam_terk.append((x_koordinata, y_koordinata))
    return seznam_terk

#3 Odsek


def tocke(seznam_terk):
    rezultat = []
    zacetna_x_koordinata = 0
    zacetna_y_koordinata = 0
    for terka in seznam_terk:
        pot_odseka = odsek(zacetna_x_koordinata, zacetna_y_koordinata, terka[0], terka[1])
        zacetna_x_koordinata = pot_odseka[-1][0]
        zacetna_y_koordinata = pot_odseka[-1][1]
        rezultat.append(pot_odseka)
    return rezultat

#4 Presečišče

def presecisce(s, t):
    s_premiki = v_pot(s)
    t_premiki = v_pot(t)

    s_tocke = tocke(s_premiki)

    t_tocke = tocke(t_premiki)


    s_prave_tocke = []
    for nested_seznam in s_tocke:
        for tocka in nested_seznam:
            s_prave_tocke.append(tocka)

    t_prave_tocke = []
    for nested_seznam in t_tocke:
        for tocka in nested_seznam:
            t_prave_tocke.append(tocka)

    presecisca = []
    for tocka in s_prave_tocke:
        if tocka in t_prave_tocke:
            presecisca.append(tocka)
    
    return presecisca
