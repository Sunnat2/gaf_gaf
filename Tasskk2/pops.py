import pandas as pd
import random

# Создаем исходный DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразуем в one-hot вид
one_hot = pd.DataFrame(data['whoAmI'].apply(lambda x: [1, 0] if x == 'robot' else [0, 1]).tolist(), columns=['robot', 'human'])

# Объединяем с исходным DataFrame, если нужно
result = pd.concat([data, one_hot], axis=1)

# Выводим результат
print(result.head())