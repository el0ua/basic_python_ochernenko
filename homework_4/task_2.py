general_data = input('Введіть дані людини відповідно формату "Ім\'я Прізвище*Дата народження(рррр-мм-дд)*Дата смерті(рррр-мм-дд)": ')

name_data, birth_data, death_data = general_data.split('*')

birth_data_list = birth_data.split('-')
birth_year = int(birth_data.split('-')[0])

death_data_list = death_data.split('-')
death_year = int(death_data_list[0])

age = death_year - birth_year

print(f'Name: {name_data}\nAge: {age} years')