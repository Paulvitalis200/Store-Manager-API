import re


def validation_check(password, username, email, payload):
    data = request.get_json()
    args = UserRegistration.parser.parse_args()
    raw_password = args.get('password').strip()
    username = args.get('username').strip()  # remove all whitespaces from input
    email = args.get('email').strip()  # remove all whitespaces from input
    payload = ['username', 'password', 'email']
    # User input validations
    email_format = re.compile(r"(^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[.a-zA-Z-]+$)")
    username_format = re.compile(r"(^[A-Za-z0-9-]+$)")

    if not email:
        return {'message': 'Email cannot be empty'}, 400
    elif not raw_password:
        return {'message': 'Password cannot be empty'}, 400
    elif not username:
        return {'message': 'Username cannot be empty'}, 400
    elif len(raw_password) < 6:
        return {'message': "incorrect"}
    elif not (re.match(email_format, email)):
        return {'message': 'Invalid email'}, 400
    elif not (re.match(username_format, username)):
        return {'message': 'Please input only characters and numbers'}, 400
    else:
        # Check if the item is not required
        for item in data.keys():
            if item not in payload:
                return {"message": "The field '{}' is not required for registration".format(item)}, 400
