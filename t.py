# from models.task import Task

# def t():
#     form = {}
#     id = 1
#     Model = Task
#     t = Model.query.get(id)
#     c = t.status_list
#     t.status_list = {'2018-07-01': '2', '2018-07-02': '4', '2018-07-04': '1', '2018-07-03': '2', }
#     t.save()
# def tt():
#     t = {'2018-07-01': '2', '2018-07-02': '4', '2018-07-04': '1', '2018-07-03': '2', }
#     print(t.keys())
# tt()
import re
m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
r = m.groups()
print(r)
# print(r.group())

# if:
#     print('ok')
# else:
#     print('failed')

t = re.match(r"(?<=《)[^》]+(?=》)", "《fff》")
print(t)
rr = t.groups() if t else None
print(rr) 