def inverter(string):
    invert = []
    indice = len(string)
    while indice > 0:
        invert += string[indice-1]
        indice = indice - 1
    print(invert)

if __name__ == "__main__":
    inverter("Vamo Santos")