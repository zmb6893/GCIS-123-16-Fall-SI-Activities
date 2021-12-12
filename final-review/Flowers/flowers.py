from flower_pictures import draw_flower
import csv

class Flower:
    __slots__ = ["__name__", "__color__", "__size__", "__layers__"]
    def __init__(self, name, color, size, layers):
        self.__name__ = name
        self.__color__ = color
        self.__size__ = size
        self.__layers__ = layers

    def get_name(self):
        return self.__name__
    
    def get_color(self):
        return self.__color__
    
    def get_size(self):
        return self.__size__
    
    def get_layers(self):
        return self.__layers__

    def preview_flower(self):
        """
        Draws the flower
        """
        draw_flower(self.__size__,self.__layers__, self.__color__)

    def __repr__(self):
        return "A(n) %s %s:"%(self.__color__, self.__name__)

class FlowerShop:
    __slots__ = ["__name__", "__catalog__", "__rating__"]

    def __init__(self, name, catalog, rating):
        self.__name__ = name
        self.__catalog__ = catalog  # dictionary
        self.__rating__ = rating

    def get_name(self):
        return self.__name__
    
    def get_catalog(self):
        return self.__catalog__
    
    def get_rating(self):
        return self.__rating__

    def __repr__(self):
        return "%s %s Stars"%(self.__name__, self.__rating__)

def read_flowers(filename):
    """
    Reads input from a csv for flowers. format as follows: flower id, name, color, size, number of layers
    """
    flowers = dict()

    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        for record in reader:
            flowers[record[0]] = Flower(record[1], record[2],record[3],record[4])
    return flowers

def read_shops(filename, flower_selection):
    """
    Reads input from a csv for shops. format as follows: name, catalog ids, rating
    """

    shops = dict()

    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        for record in reader:
            ids = record[1].split(' ')
            catalog = dict()
            for id in ids:
                catalog[id]=flower_selection.get(id) 
            shops[record[0]] = FlowerShop(record[0], catalog, record[2]) 
    
    return shops

def main():
    print(flower_selection:=read_flowers("final-review/flowers.csv"))
    print("\n\n")
    print(shops:=read_shops("final-review/flower_shops.csv",flower_selection))
main()