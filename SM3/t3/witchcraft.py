import io
import logging
from json import dumps
from time import sleep

from flask import Flask
from multiprocessing import Process
from contextlib import contextmanager, redirect_stdout

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


class Server:
    def __init__(self, host, port, data):
        self.__host__ = host
        self.__port__ = port
        self.__data__ = data

    @contextmanager
    def run(self):
        p = Process(target=self.server)
        p.start()
        sleep(1)
        yield
        p.kill()

    def server(self):
        _ = io.StringIO()
        with redirect_stdout(_):
            app = Flask(__name__)

            @app.route('/')
            def index():
                return dumps(self.__data__)

            app.run(self.__host__, self.__port__)


if __name__ == '__main__':
    data = [
        {
            'scare': [152, 51, -66],
            'enchant': [70, -103, 131, 17, -30, 182, -111],
            'repair': [207, -38, -45, 172, 96],
            'create': [197, 156, -6, 16, 255, -284]
        },
        {
            'transform': [7, -99, 3, -21, 7, -2, -9, 12],
            'enchant': [-52, 177, 164],
            'fly': [-156, -53, 33, 255],
            'repair': [-98, 285, 75, 290, 90, 212]
        }
    ]

    index = 0
    while (index := int(input('Р’РІРµРґРёС‚Рµ РЅРѕРјРµСЂ РїСЂРёРјРµСЂР°: '))) not in (1, 2):
        ...
    server = Server('127.0.0.1', 5000, data[index - 1])
    with server.run():
        while (row := input('Р’РІРµРґРёС‚Рµ "stop" РґР»СЏ Р·Р°РІРµСЂС€РµРЅРёСЏ СЂР°Р±РѕС‚С‹ СЃРµСЂРІРµСЂР°: ')) != 'stop':
            ...