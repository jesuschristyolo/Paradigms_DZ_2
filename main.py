# мой выбор пал на процедурную парадигму программирования в связи с тем что нам потребуется много раз вызывать
# таблицу умножения из разных уголков программы, а это будет намного проще если это делать через процедурную парадигму,
# обернув в функцию


def multiply_table(number):
    multi_matrix = [[i * j for i in range(1, number + 1)] for j in range(1, 10)]
    print('Таблица умножения: ')
    for i in multi_matrix:
        for j in i:
            print(f'{str(i.index(j) + 1).rjust(3)} * {str(multi_matrix.index(i) + 1).rjust(3)} = {str(j).rjust(3)}',
                  end=" || ")
        print()


matrix = multiply_table(int(input('Введите искомое число \n')))
