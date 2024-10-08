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
                    self.Database = Database(self.path, password)
    
    def system(self) -> None:
        
        os.system("cls")

        option = input("Digite sua opção\n[1]Gerar nova senha\n[2]Ver as senhas\n")

        while option != "1" and option != "2":
            os.system("cls")
            option = input("Opção inválida\nDigite sua opção\n[1]Gerar nova senha\n[2]Ver as senhas\n")

        match option:
            case "1":
                self.getOpts()
 
            case "2":
                os.system("cls")
                print("----Visualizador de senhas----")

                passwords = self.Database.showPass()
                for i in passwords:
                    print(i)
    
    def getOpts(self):
        os.system("cls")
        print("----Gerador de senhas----")
        dict = {
            'site' : '',
            'login' : '',
            'qntd' : 0,
            'number' : 0,
            'specialChar' : 0,
            'mixLowHigh' : 0,
        }
        opt = input("Digite o site: ")
        while opt == "":
            opt = input("Inválido\nDigite o site: ")
        dict['site'] = opt

        opt = input("Digite o login: ")
        while opt == "":
            opt = input("Inválido\nDigite o login: ")
        dict["login"] = opt
        while True:
            while True:
                try:
                    opt = input("Quantos caracteres? (Escreva em número de 4 à  24)\n")
                    opt = int(opt)
                    while opt < 4 or opt > 24:
                        raise Exception

                    dict['qntd'] = opt

                    break
                except:
                    print("Inválido")

            while True:
                try:
                    opt = input("Senha com números? [1=Sim][2=Não]\n")
                    opt = int(opt)
                    while opt != 1 and opt != 2:
                        raise Exception

                    dict['number'] = opt

                    break
                except:
                    print("Inválido")
            while True:
                try:
                    opt = input("Caracteres especiais? [1=Sim][2=Não]\n")
                    opt = int(opt)
                    while opt != 1 and opt != 2:
                        raise Exception

                    dict["specialChar"] = opt

                    break
                except:
                    print("Inválido")
            while True:
                try:
                    opt = input("Misturar maiúsculo e minúsculo? [1=Sim][2=Não]\n")
                    opt = int(opt)
                    while opt != 1 and opt != 2:
                        raise Exception

                    dict["mixLowHigh"] = opt

                    break
                except:
                    print("Inválido")

            while True:
                opt = input("Continuar? [1=Sim][2=Não]\n")
                while opt != "1" and opt != "2":
                    opt = input("Inválido\nContinuar? [1=Sim][2=Não]\n")
                break
            if opt == "1":
                break
            else:
                pass
        Generator().encrypt(self.password, dict)

if __name__ == "__main__":
    Gerenciador()