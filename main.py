# Dice sum probability calculator
# Författare: Leonard Wiidh
# Datum:2024-08-21
from collections import Counter

def main():
    first_die = int(input("hur många sidor ska första tärning ha?: "))
    second_die = int(input("hur många sidor ska andra tärning ha?: "))

    lista=[]
    while True:
        for tärning1 in range(1, first_die + 1):
            print(f"tabell {tärning1}")
            for tärning2 in range(1, second_die + 1):
                print(f"{tärning1} + {tärning2} = {str(tärning1+tärning2)}")
                lista.append(str(tärning1+tärning2))
        break
    print(lista)
    most_common = Counter(lista).most_common(len(lista))
    print(most_common)
    print("mest trolig summa av båda tärningarna")
    for i in range(len(most_common)):
        if int(most_common[0][1])== int(most_common[i][1]):
            print(most_common[i][0])


if __name__ == "__main__":
    main()
