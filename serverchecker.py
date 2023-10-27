import sys
import json

def naar_Json():
    with open("keuzes.json", "a") as f2:
        f2.write(json.dumps({"keuze": sys.argv[1], "server address": sys.argv[2]}, sort_keys = True))

def naar_Json2(letter, server):
    with open("keuzes.json", "a") as f2:
        f2.write(json.dumps({"keuze": letter, "server address": server}, sort_keys = True))

servers = []
if __name__=='__main__':
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case "a":
                print ("u heef gekozen om een server toe te voegen")
                servers.append(sys.argv[1])
            case "b":
                print ("u heeft gekozen om een server te verwijderen")
                servers.remove(sys.argv[1])
            case "c":
                print ("u heef gekozen om de server lijst te laten zien")
            case _:
                print ("dit is geen geldige optie")
        naar_Json()

    else:
        ant = input("wil je servers toevoegen, verwijderen of een lijst laten zien? (a/b/c)")
        match ant:
            case "a":
                print ("u heef gekozen om een server toe te voegen")
                server = input("geef een server")
                servers.append(server)
            case "b":
                print ("u heeft gekozen om een server te verwijderen")
                server = input("geef een server")
                servers.remove(server)
            case "c":
                print ("u heef gekozen om de server lijst te laten zien")
            case _:
                print ("dit is geen geldige optie")
        naar_Json2(ant, server)