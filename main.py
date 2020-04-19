from zoo import Zoo

def main():
    lviv_zoo = Zoo(4387, "Lev", 59, "Lviv")
    kyiv_zoo = Zoo()
    new_york_zoo = Zoo(920295, "NY zoo", 950, "New York", 2000.0, 9.37)
    print(lviv_zoo)
    print(kyiv_zoo)
    print(new_york_zoo)

if __name__ == "__main__": main()