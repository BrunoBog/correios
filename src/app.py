from time import strftime, gmtime, time
import time
from flask.app import Flask
from win10toast import ToastNotifier
from encomenda import Encomentda

app = Flask(__name__)


@app.route('/')
def busca():
    growth = Encomentda('Growth', 'PO499320057BR')
    monitor = Encomentda('Monitor', 'OA516793289BR')

    while True:
        print("Iniciando as buscas... " + strftime ("%Y-%m-%d %H:%M:%S", gmtime()))
        print("Buscando encomenda da Growth")
        element = growth.buscaSoup()
        growth = hunting(element,growth)
        print("Buscando encomenda do monitor")
        element = monitor.buscaSoup()
        monitor = hunting(element, monitor)
        time.sleep(60 * 30)


def hunting(element, encomenda):
    toaster = ToastNotifier()

    if not encomenda.ishaveStatus((element[0].text.replace("\t", "")).replace("\n", "")):
        encomenda.addStatus((element[0].text.replace("\t", "")).replace("\n", ""))
        print("Nova movimentação: \n " + (element[1].text.replace("\t", "")).replace("\n", "") )
        toaster.show_toast(encomenda.nome, element[0].text + " " + element[1].text, duration=10)

    return encomenda

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # app.run(debug=True)

