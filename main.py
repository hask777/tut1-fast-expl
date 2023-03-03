from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':'blog_list'}



@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all published blogs'}



@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}



@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1','2'}}
    
     