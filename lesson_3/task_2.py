def format_person(name='John', surname='Doe', year=18, city='', mail='', phone=''):
    """ Возвращает форматированную строку с данными пользователя.

        Именованные параметры:
        name -- Имя
        surname -- Фамилия
        year -- Год рождения
        city -- Город проживания
        mail -- E-mail
        phone -- Номер телефона

    """
    return f"Пользователь:\n{name} {surname} {year}г.р.\nПроживает в г.{city}\nE-mail: {mail}\nТелефон: {phone}"


print(format_person(name='Артем', surname='Ситдиков', year=1985, city='Екатеринбург',
                    mail='safhunter@mail.ru', phone='+79655287545'))
