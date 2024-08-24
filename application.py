from fastapi import FastAPI, Request                #  Import FastAPI and Request from fastapi 
from fastapi.templating import Jinja2Templates      # Import Jinja2 template from fastapi.templating
import uvicorn                                      # Import uvicorn

app = FastAPI()                                     #  Create an instance of fastapi
template = Jinja2Templates(directory="templates")   # defining the template folder path
                
@app.get("/")                                       # Create a decorater along with fastapi instance and HTTP.get
def htmlpage(req:Request):                          # Define a function name 'htmlpage' with the request parameter
    return template.TemplateResponse(               # Returning TemplateResponse
        name="index.html",                          # Defining the name of the html page inside the templates folder
        context={"request": req}                    # Defining a context dictionary with a key value pair
    )

if __name__ == "__main__":                   # It defines under what condition the main method should be execute
    uvicorn.run("application:app")            