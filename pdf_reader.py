from collections import namedtuple
import tabula
import numpy as np

list_of_dataframes = tabula.read_pdf(
    "test_pdf.pdf", 
    pages=1,
    pandas_options={"header": [0]},
    guess=False
)
dataframe = list_of_dataframes[0]

Good = namedtuple('Good', ['name', 'count', 'product_price', 'total'])
goods = []
print('Goods\n')
for num, name, _, count, _, product_price, total in dataframe.to_records():
    if name == 'Электронный платеж': 
        print(f'Total: {total}')
        break
    if num >= 4 and name is not np.nan:
        goods.append(
            Good(name=name, count=count, product_price=product_price, total=total))
        print(f'name: {name},\tcount: {count},\tprice: {total} rub.')

print('\n'.join(list(map(str, goods))))
# TODO: не факт что это условие 'Электронный платеж' будет везде одинаковым
# TODO: поддержать парсинг чека с сайта nalog.ru
# TODO: добавить возможность подилить чек на всех поровну

# TODO: второстепенные фичи - сделать выгрузку в excel
