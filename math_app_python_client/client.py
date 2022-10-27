from suds import Client

math_client = Client("http://localhost:8000/maths/?wsdl")
print(math_client)
x = input("x=")
y = input("y=")
maxx = math_client.service.max(x, y)
minn = math_client.service.min(x, y)
coss = math_client.service.cos(x)
sinn = math_client.service.sin(x)
print(f'max({x},{y})={maxx}')
print(f'min({x},{y})={minn}')
print(f'sin({x})={sinn}')
print(f'cos({x})={coss}')

