from flask import request, Blueprint

from flask_restful import Resource
from app.api.V1.models import Sale


salesList = []
