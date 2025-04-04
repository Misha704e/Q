with open("hello.txt", "r") as r:
    c = r.readlines()
r_name = "hello.txt"
m_con = [line + f" цей текст із файлика ({r_name})" for line in c]
for line in m_con:
    print(line)