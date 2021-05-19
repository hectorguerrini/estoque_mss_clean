
from src.adapters.controllers.ports.http import HttpResponse


def ok(data) -> HttpResponse:
    return HttpResponse(statusCode=200, body=data)


def badRequest(msg: str) -> HttpResponse:
    return HttpResponse(statusCode=400, body={"err": msg})


def serverError(data: str) -> HttpResponse:
    return HttpResponse(statusCode=500, body={"err": data})
