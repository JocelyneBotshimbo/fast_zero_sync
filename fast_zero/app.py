# def read_root():
#     return {'message': 'Hello world'}

# print(read_root())

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Hello World!'}


# @app.post('/batata')
# def root(): return {'message': 'Bonjour Joyce'}
