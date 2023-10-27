ant = input("wil je servers toevoegen, verwijderen of een lijst laten zien? (a/b/c)")
match ant:
    case "a":
        print ("u heef gekozen om een server toe te voegen")
    case "b":
        print ("u heeft gekozen om een server te verwijderen")
    case "c":
        print ("u heef gekozen om de server lijst te laten zien")