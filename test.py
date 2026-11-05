def fun(id, name, age):
    print(f'아이디: {id}')
    print(f'이름: {name}')
    print(f'나이: {age}')

# 매개변수명과 딕셔너리의 키가 같아야함
# 딕셔너리의 키는 반드시 문자열 형태
dic = {'age':25, 'id':'banana', 'name':'반하나'}
fun(**dic)

# *의 데이터를 보낼 경우 키가 저장
fun(*dic)
