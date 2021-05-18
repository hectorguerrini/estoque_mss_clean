
from src.adapters.controllers.ports.http import HttpResponse

def ok(data) -> HttpResponse:
    return HttpResponse(statusCode=200, body=data)

def badRequest(data) -> HttpResponse:
    return HttpResponse(statusCode=400, body=data)

def serverError(data: str) -> HttpResponse:
    return HttpResponse(statusCode=500, body={"msg": data})