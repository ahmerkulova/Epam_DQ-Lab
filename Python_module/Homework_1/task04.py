# Напишите программу, которая генерирует текст песенки Im Radio ist ein Kuken
# Здесь может потребоваться подстановка строк. Действительно, не всегда бывает удобно собирать строку из кусочков,
# а тем более, выводить строку по кусочкам. Для этого используйте любой способ для форматирования строк, который
# вам удобен. Также уделите внимание вот какому аспекту - эта народная потешка имеет много вариаций, начиная
# со списка участников, и заканчивая языком (русским, немецким, каким угодно). Поэтому ваша задача - написать такой код,
# который как можно проще переделывается под новую вариацию.
# Вынесите все данные в отдельное место в программе, чтобы при изменениях текста песни не пришлось выискивать строки,
# разбросанные по коду. Что должна вывести ваша программа:
#     Бабушка, бабушка, купим курочку!
#     Бабушка, бабушка, купим курочку!
#     Курочка по зёрнышку кудах-тах-тах.
#     Бабушка, бабушка, купим уточку!
#     Бабушка, бабушка, купим уточку!
#     Уточка та-ти-та-та,
#     Курочка по зёрнышку кудах-тах-тах.
#     Бабушка, бабушка, купим индюшонка!
#     Бабушка, бабушка, купим индюшонка!
#     Индюшонок фалды-балды,
#     Уточка та-ти-та-та,
#     Курочка по зёрнышку кудах-тах-тах.
#     Бабушка, бабушка, купим кисоньку!
#     Бабушка, бабушка, купим кисоньку!
#     А кисуня мяу-мяу,
#     Индюшонок фалды-балды,
#     Уточка та-ти-та-та,
#     Курочка по зёрнышку кудах-тах-тах.
#     Бабушка, бабушка, купим собачонку!
#     Бабушка, бабушка, купим собачонку!
#     Собачонка гав-гав,
#     А кисуня мяу-мяу,
#     Индюшонок фалды-балды,
#     Уточка та-ти-та-та,
#     Курочка по зёрнышку кудах-тах-тах.
#     Бабушка, бабушка, купим коровёнку!
#     Бабушка, бабушка, купим коровёнку!
#     Коровёнка муки-муки,
#     Собачонка гав-гав,
#     А кисуня мяу-мяу,
#     Индюшонок фалды-балды,
#     Уточка та-ти-та-та,
#     Курочка по зёрнышку кудах-тах-тах.
#     Бабушка, бабушка, купим поросёнка!
#     Бабушка, бабушка, купим поросёнка!
#     Поросёнок хрюки-хрюки,
#     Коровёнка муки-муки,
#     Собачонка гав-гав,
#     А кисуня мяу-мяу,
#     Индюшонок фалды-балды,
#     Уточка та-ти-та-та,
#     Курочка по зёрнышку кудах-тах-тах.
#     Бабушка, бабушка, купим телевизор!
#     Бабушка, бабушка, купим телевизор!
#     Телевизор надо, надо, ведь у нас такое стадо!

intro = 'Бабушка, бабушка, купим'
characters = [('курочку', 'Курочка по зёрнышку кудах-тах-тах'), ('уточку', 'Уточка та-ти-та-та'), ('индюшонка', 'Индюшонок фалды-балды'), ('кисоньку', 'А кисуня мяу-мяу'), ('собачонку', 'Собачонка гав-гав'), ('коровёнку', 'Коровёнка муки-муки'), ('поросёнка', 'Поросёнок хрюки-хрюки'), ('телевизор', 'Телевизор надо, надо, ведь у нас такое стадо')]
for idx, current in enumerate(characters):
    if current[0] == characters[-1][0]:
        break
    else:
        print(f'{intro} {current[0]}!\n{intro} {current[0]}!')
    for item in characters[0: idx+1][::-1]:
        if item[0] == characters[0][0]:
            print(item[1], end='.\n')
        else:
            print(item[1], end=',\n')
    print()
print(f'{intro} {characters[-1][0]}!\n{intro} {characters[-1][0]}!\n{characters[-1][1]}!')