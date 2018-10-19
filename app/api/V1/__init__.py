from flask import Blueprint
from flask_restful import Api

from .views.products import PostProduct, GetAllProducts, GetEachProduct
from .views.sales import PostSale, GetAllSales, GetEachSale
