import sys
import json

# def naar_Json():
#     with open("keuzes.json", "a") as f2:
#         f2.write(json.dumps({"keuze": sys.argv[1], "server address": sys.argv[2]}, sort_keys = True))

# def naar_Json2(letter, server):
#     with open("keuzes.json", "a") as f2:
#         f2.write(json.dumps({"keuze": letter, "server address": server}, sort_keys = True))

def update_json():
    with open("keuzes.json", "w") as f:
        f.write(json.dumps(servers))


def list_servers(servers):
    for index, server in enumerate(servers):
        print(f"{index}: {server}")

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
                # naar_Json2(ant, server)
            case "b":
                print ("u heeft gekozen om een server te verwijderen")
                server = input("geef een server: ")
                servers.remove(server)
                update_json()
                # naar_Json2(ant, server)
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
            # naar_Json()
        case "b":
            print ("u heeft gekozen om een server te verwijderen")
            del servers[-1]
            # naar_Json()
        case "c":
            print ("u heef gekozen om de server lijst te laten zien")
            list_servers(servers)
        case _:
            print ("dit is geen geldige optie")
    menu()

if __name__=='__main__':
    servers = []
    try:
        with open ("keuzes.json", "r") as f:
            servers = json.loads(f.read())
        if len(sys.argv) > 1:
            cli()
        else:
            menu()
    except IOError:
        servers = []
        if len(sys.argv) > 1:
            cli()
        else:
            menu()
        