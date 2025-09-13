from rich.console import Console

console = Console()

def main():
    
    names = [] 
    print("Ism kiriting (to'xtatish uchun (stop) yozing):")
    
    while True:
        name = input("Ism kiriting: ")

        if name.lower() == "stop":  
            break

        names.append(name) 

    console.print(f"Kiritilgan ismlar ro`yxati: {names}", style="bold green")
    console.print(f"Jami kiritilgan ismlar soni: {len(names)}", style="bold red")


main()
