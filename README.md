http://localhost:8000/user/api/registration - registration User_Acc
http://localhost:8080/user/api/user-list - list of all User_Acc

All opportunities for authentication:

http://localhost:8000/+

auth/users/

auth/users/me/

auth/users/confirm/

auth/users/change_username/

auth/password/

auth/password/reset/

auth/password/reset/confirm/

auth/token/login/ (Token Based Authentication)

auth/token/logout/ (Token Based Authentication)

auth/jwt/create/ (JSON Web Token Authentication)

auth/jwt/refresh/ (JSON Web Token Authentication)

auth/jwt/verify/ (JSON Web Token Authentication)


curl -X POST http://127.0.0.1:8000/auth/token/login/ --data 'username=username&password=password'
{"auth_token": "b704c9fc3655635646356ac2950269f352ea1139"}

for Token:
$ curl -X GET http://127.0.0.1:8000/auth/users/me/ -H 'Authorization: Token <your_token>'
{"email": "", "username": "djoser", "id": 1}

for JWT:
$ curl -X GET http://127.0.0.1:8000/auth/users/me/ -H 'Authorization: JWT <your_token>'
{"email": "", "username": "djoser", "id": 1}
