import sys
import json

def update_json():
    with open("keuzes.json", "w") as f:
        f.write(json.dumps(servers))


def list_servers(servers):
    for index, server in enumerate(servers):
        print(f"{index}: {server}")

def keuze():
    if len(sys.argv) > 3:
        if sys.argv[3] == "man":
            cli()
        elif sys.argv[3] == "checks":
            checks()
    elif len(sys.argv) == 2:
        if sys.argv[1] == "man":
            menu()
        elif sys.argv[1] == "checks":
            checks()
    elif len(sys.argv) == 1:
        menu()

def menu():
    blijven = True
    while blijven:
        ant = input("wil je servers toevoegen, verwijderen of een lijst laten zien? (a/b/c) (stoppen = 0): ")
        match ant:
            case "a":
                print ("u heef gekozen om een server toe te voegen")
                server = input("geef een server: ")
                servers.append(server)
                update_json()
            case "b":
                print ("u heeft gekozen om een server te verwijderen")
                server = input("geef een server: ")
                servers.remove(server)
                update_json()
            case "c":
                print ("u heef gekozen om de server lijst te laten zien")
                list_servers(servers)
            case "0":
                blijven = False
            case _:
                print ("dit is geen geldige optie")

def cli():
    match sys.argv[1]:
        case "a":
            print ("u heef gekozen om een server toe te voegen")
            servers.append(sys.argv[2])
            update_json()
        case "b":
            print ("u heeft gekozen om een server te verwijderen")
            del servers[-1]
        case "c":
            print ("u heef gekozen om de server lijst te laten zien")
            list_servers(servers)
        case _:
            print ("dit is geen geldige optie")
    menu()

def checks():
    print("checks optie zal later komen")

if __name__=='__main__':
    servers = []
    try:
        with open ("keuzes.json", "r") as f:
            servers = json.loads(f.read())
        keuze()
    except IOError:
        servers = []
        if len(sys.argv) > 1:
            cli()
        else:
            menu()
        