prod_A = 'Product A'
prod_B = 'Product B'
prod_C = 'Product C'

price_A = 20
price_B = 40
price_C = 50

discount_name1 = 'flat_10_discount'
discount_name2 = 'bulk_5_discount'
discount_name3 = 'bulk_10_discount'
discount_name4 = 'tiered_50_discount'

discount_amt1 = 0
discount_amt2 = 0
discount_amt3 = 0
discount_amt4 = 0

discount_A = 0
discount_B = 0
discount_C = 0

print("Enter the quantity of each product")
qnt_A = int(input('Product A : '))
qnt_B = int(input('Product B : '))
qnt_C = int(input('Product C : '))

print("\nWhether the product Should be wrapped with gift wrap?(Enter y/n)")
ch = input()

total_qnt = qnt_A + qnt_B + qnt_C

total_A = qnt_A * price_A
total_B = qnt_B * price_B
total_C = qnt_C * price_C

print('\nProduct Name :',prod_A,'\tQuantity:',qnt_A,'\tAmount:',total_A)
print('Product Name :',prod_B,'\tQuantity:',qnt_B,'\tAmount:',total_B)
print('Product Name :',prod_C,'\tQuantity:',qnt_C,'\tAmount:',total_C)

sub_total = total_A + total_B + total_C

print('\nSubtotal Amount(total amount of each product) :',sub_total,'\n')

if(sub_total>200):
    discount_amt1 = 10

if(qnt_A>10 or qnt_B>10 or qnt_C>10):
    if(qnt_A>10):
        discount_A = total_A*0.05
    if(qnt_B>10):
        discount_B = total_B*0.05
    if(qnt_C>10):
        discount_C = total_C*0.05
    discount_amt2 = discount_A+discount_B+discount_C

if(total_qnt>20):
    discount_amt3 = sub_total*0.10

if(total_qnt>30 and (qnt_A>15 or qnt_B>15 or qnt_C>15)):
    if(qnt_A>15):
        discount_A = (qnt_A - 15)*0.50

    if(qnt_B>15):
        discount_B = (qnt_B - 15)*0.50

    if(qnt_C>15):
        discount_C = (qnt_C - 15)*0.50
    
    discount_amt4 = discount_A+discount_B+discount_C

    if((discount_amt1>discount_amt2) and (discount_amt1>discount_amt3) and (discount_amt1>discount_amt4)):
        print('Discount Name :',discount_name1,'\tDiscount Amount :',discount_amt1)
        discount_amt = discount_amt1
    elif((discount_amt2>discount_amt1) and (discount_amt2>discount_amt3) and (discount_amt2>discount_amt4)):
        print('Discount Name :',discount_name2,'\tDiscount Amount :',discount_amt2)
        discount_amt = discount_amt2
    elif((discount_amt3>discount_amt1) and (discount_amt3>discount_amt2) and (discount_amt3>discount_amt4)):
        print('Discount Name :',discount_name3,'\tDiscount Amount :',discount_amt3)
        discount_amt = discount_amt3
    else:
        print('Discount Name :',discount_name4,'\tDiscount Amount :',discount_amt4)
        discount_amt = discount_amt4
    
gift_fee = 0
if ch == 'y':
    gift_fee = qnt_A + qnt_B + qnt_C

pack = 10
ship = 5
ship_fee = 0
while(total_qnt>0):
    ship_fee += ship
    total_qnt-=pack

print('\nGift Wrap fee :',gift_fee)

print('\nShipping fee :',ship_fee)

total_amt = sub_total + gift_fee + ship_fee - discount_amt
print('\nTotal Amount(including discount, gift wrap fee and shipping fee) :',total_amt)
