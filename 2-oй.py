frukt=['Вишня', 'Малина', 'Яблоко', 'Груша', 'Черешня', 'Абрикос']
frukt.append('Голубика')
frukt.pop(2)
frukt.pop(2)
frukt.insert(2,'Слива')


for fg in range (len(frukt)):
    print(frukt[fg])
