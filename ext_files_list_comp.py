from obj_var_fun import foo4

imported_function = foo4(19, 12)
print(f'Imported function result = {imported_function}')

with open('book.txt', 'w') as file:
    file.write('Hello There!\n\n')

content = '''Siobhan said that I should write something I would want to read myself.
Mostly I read books about science and maths.
I do not like proper novels.
In proper novels people say things like, ‘I am veined with iron, with silver and with streaks of common mud.
I cannot contract into the firm fist which those clench who do not depend on stimulus’ . 
What does this mean? I do not know. Nor does Father. Nor do Siobhan or Mr Jeavons. I have asked them.
'''

with open('book.txt', 'a') as file:
    file.write(content)
    # 'a' = append | Otherwise 'w' write would overwrite what is in place 

with open('book.txt', 'r') as file:
    content = file.read()
print(content)

with open('weather.txt', 'w') as file:
    file.writelines(['Clouds\n', 'Sun\n', 'Rain\n', 'Wind\n'])

try: 
    with open('wether.txt', 'r') as file:
        content = file.readlines()
    # clean_content = [item.strip('\n') for item in content]
    clean_content = [item[:-1] for item in content]
    print(clean_content)
except Exception as e:
    print(f"Failed to process weather file, error: {e}")
