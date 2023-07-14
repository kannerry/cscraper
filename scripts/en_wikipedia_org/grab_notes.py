def main(soup):
    references = soup.find(class_="references")
    list_items = references.find_all("li")
    for item in list_items: 
        print(item.text)
        modular()

def modular():
    print("modular!")