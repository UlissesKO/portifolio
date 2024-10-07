from crypto import *
from database import *

from tkinter import filedialog, Tk
import os

class Gerenciador():
    def __init__(self) -> None:
        self.password = self.getPassword()
        self.getDb(self.password)
        self.system()
    
    def getPassword(self) -> str:
        print("----Gerenciador de senhas----")

        password = input("Digite sua senha (Não avisarei caso a senha esteja incorreta): ")
        while password == "" or len(password) <= 2:
            os.system("cls")
            password = input("Senha Inválida\nDigite sua senha (Não avisarei caso a senha esteja incorreta): ")

        return password

    def getDb(self, password) -> None:
        option = input("Criar banco novo[1]\nAbrir já existente[2]\n")

        while option != "1" and option != "2":
            os.system("cls")
            option = input("Opção inválida\nCriar banco novo[1]\nAbrir já existente[2]\n")
        
        match option:
            case "1":
                self.Database = Database("db.sql", password)
                self.system()

            case "2":
                window = Tk()
                window.withdraw()

                window.attributes('-topmost', True)

                self.path = filedialog.askopenfilename(
                    title="Selecione a base de dados",
                    filetypes=[("Arquivos SQL", "*.sql")]
                )
                
                window.destroy()

                if not self.path:
                    return
                else:
                    self.Database = Database("db.sql", password)
    
    def system(self) -> None:
        
        os.system("cls")

        option = input("Digite sua opção\n[1]Gerar nova senha\n[2]Ver as senhas\n")

        while option != "1" and option != "2":
            os.system("cls")
            option = input("Opção inválida\nDigite sua opção\n[1]Gerar nova senha\n[2]Ver as senhas\n")

        match option:
            case "1":
                os.system("cls")
                print("----Gerador de senhas----")
                Generator.encrypt(self.password)
                
            case "2":
                os.system("cls")
                print("----Visualizador de senhas----")

                self.Database.showPass()

if __name__ == "__main__":
    Gerenciador()