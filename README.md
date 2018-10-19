# Store-Manager-API

Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store.


# API Design

The api is constructed using python flask and flask restful

Testing is done using pytest

Test coverage is done using pytest-cov

# Installation

Clone the repo to your local machine.

open using python run.py

open localhost

# Features

Store attendant can search and add products to buyer’s cart.
Store attendant can see his/her sale records but can’t modify them.
App should show available products, quantity and price.
Store owner can see sales and can filter by attendants.
Store owner can add, modify and delete products.
Store owner can give admin rights to a store attendant.


# EndPoint Functionality
GET /products - Fetch all products Get all available products.
GET /products/productId - Fetch a single product record
GET /sales - Fetch all sale records Get all sale records.
GET /sales/saleId - Fetch a single sale record
POST /products - Create a product
POST /sales - Create a sale order
