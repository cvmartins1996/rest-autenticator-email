import hashlib

class Usuario:
    id = ""
    nome = ""
    email = ""
    hashEmail = ""
    
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email
        idEmail = int(hashlib.md5(self.email.encode('utf-8')).hexdigest(), 16)
        self.hashEmail = idEmail
    
    def getId(self):
        return self.id
    
    def getNome(self):
        return self.nome

    def getEmail(self):
        return self.email
    
    def getHashEmail(self):
        return self.hashEmail
