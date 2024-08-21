PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

lines = PRICE_LIST.strip().split('\n')
names = [line.split()[0] for line in lines]
prices = [int(line.split()[1].replace('р', '')) for line in lines]
price_dict = dict(zip(names, prices))
print(price_dict)
