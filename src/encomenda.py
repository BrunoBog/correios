import requests
from bs4 import BeautifulSoup


class Encomentda(object):

    status = []
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

    def addStatus(self, status):
        self.status.append(status)
        return

    def ishaveStatus(self,novoStatus):
        if self.status.__contains__(novoStatus):
            return True
        else:
            return False

    def buscaSoup(self):
        request = requests.get("http://www.linkcorreios.com.br/" + self.codigo)
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find_all("td", {})
        return element
