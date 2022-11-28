import logging

import azure.functions as func
from . import SelfServiceReportingBody

__version__ = "v20221115.02"

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(f'{__version__} Python HTTP trigger function processed a request. SelfServiceReporting2022')
    try:
            
        req_body = req.get_json()
        logging.info("req_body: {}".format(req_body))

        SelfServiceReportingBody.Parsebody(req_body)
        return func.HttpResponse(f"This HTTP triggered function executed successfully. {__version__}")
    except Exception as ex:
        logging.exception("error parsing body")
        return func.HttpResponse(
             f"This HTTP triggered function executed unsuccessfully. {__version__} Error: {ex}",
             status_code=500
        )
   
       