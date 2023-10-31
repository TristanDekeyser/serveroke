import sys
import json
from ping3 import ping
import time
from jinja2 import Template

def update_json():
    with open("keuzes.json", "w") as f:
        f.write(json.dumps(servers))

def update_checks_json():
    with open("checks.json", "w") as f:
        f.write(json.dumps(checkers))


def list_servers(servers):
    for index, server in enumerate(servers):
        print(f"{index}: {server}")

def keuze():
    if len(sys.argv) > 3:
        if sys.argv[3] == "man":
            cli()
        elif sys.argv[3] == "checks":
            checks()
        else:
            keus = input("wil je checks uitvoeren of naar het menu gaan (checks/menu)")
            if keus == "checks":
                checks()
            else:
                menu()
    elif len(sys.argv) == 2:
        if sys.argv[1] == "man":
            menu()
        elif sys.argv[1] == "checks":
            checks()
    elif len(sys.argv) == 1:
        keus = input("wil je checks uitvoeren of naar het menu gaan (checks/menu)")
        if keus == "checks":
            checks()
        else:
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
    doorgaan = True
    print("de checks blijven hethalen (elke 2 minuten) tot u het programma verlaat")
    with open('template.html', 'r') as template_file:
        template = Template(template_file.read())
    while doorgaan:
        checkers = []
        for server in servers:
            resp = ping(server)
            if resp == False:
                print(f"{server} kon niet worden bereikt")
                checkers.append(False)
                update_checks_json()
            else:
                print(f"{server} is up and running")
                checkers.append(True)
                update_checks_json()
        data = list(zip(servers, checkers))
        html = template.render(data=data)
        with open('server_checks.html', 'w') as html_file:
            html_file.write(html)
        time.sleep(120)

if __name__=='__main__':
    servers = []
    checkers = []
    try:
        with open ("keuzes.json", "r") as f:
            servers = json.loads(f.read())
        with open ("checks.json", "r") as f:
            checkers = json.loads(f.read())
        keuze()
    except IOError:
        servers = []
        checkers = []
        if len(sys.argv) > 1:
            cli()
        else:
            menu()
        