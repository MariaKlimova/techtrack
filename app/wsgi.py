#!home/maria/quack/venv/bin/python
import time

def wsgi_application(environ, start_response):
    # бизнес-логика
    status = b'200 OK'
    headers = [
    ('Content-Type', 'text/plain')
    ]
    body = 'time:'.encode('utf-8') + str(time.clock()).encode('utf-8') + " url:".encode('utf-8')
    start_response(status, headers)
    return ([ body ])
                     
