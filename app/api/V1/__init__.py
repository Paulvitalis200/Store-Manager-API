from flask import Blueprint
from flask_restful import Api

from .views.products import PostProduct, GetAllProducts, GetEachProduct
from .views.sales import PostSale, GetAllSales, GetEachSale
from .views.users import UserRegistration, UserLogin, GetAllUsers, GetEachUser


productsale_api = Blueprint('resources.products', __name__, url_prefix="/api/v1")
api = Api(productsale_api)

api.add_resource(
    PostProduct,
    "/products",
    endpoint="product"
)

api.add_resource(
    GetAllProducts,
    '/products',
    endpoint="products"
)

api.add_resource(
    GetEachProduct,
    '/products/<int:id>',
    endpoint="each")

api.add_resource(
    PostSale,
    '/sales',
    endpoint="sales"
)

api.add_resource(
    GetAllSales,
    '/sales',
    endpoint='sale'
)

api.add_resource(
    GetEachSale,
    '/sales/<int:id>',
    endpoint='eachsale'
)

api.add_resource(
    UserRegistration,
    '/register',
    endpoint='register'
)

api.add_resource(
    UserLogin,
    '/login',
    endpoint='login'
)

api.add_resource(
    GetAllUsers,
    '/users',
    endpoint='users'
)

api.add_resource(
    GetEachUser,
    '/users/<int:id>',
    endpoint='user'
)
