[![Build Status](https://travis-ci.org/Paulstar200/Store-Manager-API.svg?branch=ch-code-refactor-161366157)](https://travis-ci.org/Paulstar200/Store-Manager-API)

[![Coverage Status](https://coveralls.io/repos/github/Paulstar200/Store-Manager-API/badge.svg?branch=ch-badges-161335057)](https://coveralls.io/github/Paulstar200/Store-Manager-API?branch=ch-badges-161335057)


# Store-Manager-API

Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store.


# API Design

The api is constructed using python flask and flask restful

Testing is done using unittest

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
Method | URL | DESCRIPTION
-------|-----|------------
GET /products| http://127.0.0.1:5000/api/v1/products | Fetch all products
GET /products/productId |http://127.0.0.1:5000/api/v1/products/<int: productId>| Fetch a single product record
GET /sales |http://127.0.0.1:5000/api/v1/sales|Fetch all sale records Get all sale records.
GET /sales/saleId | http://127.0.0.1:5000/api/v1/sales/<int: salesId> | Fetch a single sale record
POST /products| http://127.0.0.1:5000/api/v1/products | Create a product
POST /sales | http://127.0.0.1:5000/api/v1/sales | Create a sale order

#TESTING THE APP

Test using Postman

