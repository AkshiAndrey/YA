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
    data = {
        "The Magic Staff": "story1, story2, story3, story4",
        "Staff and hat": "topic1, topic2",
        "How to treat sheep": "introduction, part1, part2",
        "How to distinguish a wizard from a staff": "story1, story2, story3",
        "A tutorial on simple and fast charms": "part1, part2, part3",
        "Why does a wizard need a hat": "hat1, hat2, hat3, hat4"
    }

    server = Server('127.0.0.1', 8080, data)
    with server.run():
        while (row := input('Р’РІРµРґРёС‚Рµ "stop" РґР»СЏ Р·Р°РІРµСЂС€РµРЅРёСЏ СЂР°Р±РѕС‚С‹ СЃРµСЂРІРµСЂР°: ')) != 'stop':
            ...