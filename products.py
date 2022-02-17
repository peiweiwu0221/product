products =[]
sum_= 0
while True:
    print('按q結束紀錄')
    name = input('請輸入商品名稱:')
    if name == 'q':
        break
    price = int(input('請輸入商品價格:'))
    products.append([ name, price])
    sum_ = sum_ + price
print ( '您總購買',len(products), '件商品')
print('總共', sum_,'元')
print('商品清單')

for p in products: #p 小清單
    print(p[0] , '的價格是', p[1])