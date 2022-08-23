import jwt

token = jwt.encode({"sub": "","channels":["channel","news"]}, "fdcc9ab3-d7d9-406d-b62a-acb6c3ce2623", algorithm="HS256")

print(token)