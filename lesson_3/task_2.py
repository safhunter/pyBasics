def format_person(name, surname, year, city, mail, phone):
    return f"Пользователь:\n{name} {surname} {year}г.р.\nПроживает в г.{city}\nE-mail: {mail}\nТелефон: {phone}"


print(format_person(name='Артем', surname='Ситдиков', year=1985, city='Екатеринбург',
                    mail='safhunter@mail.ru', phone='+79655287545'))
