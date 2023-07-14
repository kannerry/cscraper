# works for "https://www.mobafire.com/league-of-legends/skins"
 
def main(soup):
    skins = soup.find_all(class_="champ-skins__item__meta")
    for item in skins:
        i = item.find("h3")
        print(i)