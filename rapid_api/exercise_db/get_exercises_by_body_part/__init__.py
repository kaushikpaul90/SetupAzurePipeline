import logging
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    body_part = req.params.get('body_part')
    if body_part:
        url = "https://exercisedb.p.rapidapi.com/exercises/bodyPart/chest"

        querystring = {"limit":"10"}

        headers = {
            "X-RapidAPI-Key": "7a17ecd123msh1aa9a12e1ce81abp150bc3jsn4057487891a0",
            "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        print(response.json())
        
        return func.HttpResponse(f"Hello, {body_part}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a body_part in the query string or in the request body for a personalized response.",
             status_code=200
        )
