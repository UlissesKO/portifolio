import cryptocode
import random
import string

from database import *

class Generator():
    def __init__(self) -> None:
        pass

    def setOpt(self, dict) -> tuple[list, dict]:
        _list = []
        match dict['number']:
            case 0:
                pass
            case 1:
                for i in range(10):
                    i = str(i)
                    _list.append(i)
        
        match dict['specialChar']:
            case 0:
                pass
            case 1:
                char = [
                        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
                        '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '<', '>', '.', 
                        '/', '?', '~', '`'
                        ]
                _list = char + _list

        match dict['lowHighCase']:
            case 1:
                _list = list(string.ascii_letters) + _list

            case 'M':
                _list = list(string.ascii_uppercase) + _list

            case 'm':
                _list = list(string.ascii_lowercase) + _list
        return _list, dict['qntd']

    def createPassword(self, dict) -> str:
        _list, qntd = self.setOpt(dict)
        newPassword = random.sample(_list, qntd)

        newPassword = ''.join(map(str, newPassword))
        return newPassword
    
    def encrypt(self, dict, database) -> str:
        newPassword = self.createPassword(dict=dict)

        cryptPassword = cryptocode.encrypt(newPassword, database.password)
        cryptSite = cryptocode.encrypt(dict['site'], database.password)
        cryptUser = cryptocode.encrypt(dict['login'], database.password)

        database.storePass()

    def decrypt(self, encPassword) -> str:
        pass