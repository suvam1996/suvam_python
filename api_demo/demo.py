import requests

url= 'https://jsonplaceholder.typicode.com/todos'
response= requests.get(url)
j_son= response.json()
a=[]
count=0
for d in j_son:
    # print(d)
    for k,v in d.items():
        # print(k,v)
        if k=='userId' and v==1:
            # print(d)
            a.append(d)

for di in a:
    for k,v in di.items():
        if k=='completed' and v==True:
            print(di)
            count=count+1


print('total true and false data',len(a))
print('True:',count)
print('False:',len(a)-count)




a=str(input('enter something: '))
print(a)
print(type(a))
