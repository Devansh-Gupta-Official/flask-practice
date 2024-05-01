from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash,check_password_hash

# bcrypt=Bcrypt()

# password='supersecretpassword'
# hashed_password=bcrypt.generate_password_hash(password=password)
# print(hashed_password)

# check=bcrypt.check_password_hash(hashed_password,'wrongpassword')
# print(check)

# check=bcrypt.check_password_hash(hashed_password,'supersecretpassword')
# print(check)


hashed_password=generate_password_hash('mypassword')
print(hashed_password)
check = check_password_hash(hashed_password,'mypassword')
print(check)


