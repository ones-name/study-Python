car = 'bmw'
print(car == 'bmw')
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
int='in'
#rint("is int=='in'? i predict True")
print(int=="in")
#print("is int=='k'? i predict False")
print(int=='k')
kk="Kai"
uu="kai"
kk_1=kk.lower()==uu
print(kk_1)
p=5
o=11
# print(p==5 and o==11)
# print(p!=5 and o!=11)
# print(p<6 and o<12)
# print(p>4 and o>10)
# print(p<=10 and o<=10)
# print(p>=10 and o<=10)
# print(p==5 or o==11)
# print(p!=5 or o!=11)
# print(p<6 or o<12)
# print(p>4 or o>10)
# print(p<=10 or o<=10)
# print(p>=10 or o<=10)
j=["int","kun"]
print("int" in j)
print("int" not in j)
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
age = 12
if age <4:
    print("Your admission cost is $0.")
elif age <18:
    print("Your admission cost is $25.")
elif age <60:
    print("Your admission cost is $50.")
else:
    print("Your admission cost is $0.")
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
alien_color="red"
if alien_color=="green":
    print("就获得5分")
if alien_color=="red":
    print("就获得10分")
if alien_color=="green":
    print("就获得5分")
else:
    print("就获得10分")
    #为绿色时
if alien_color=="green":
    print("就获得5分")
elif alien_color=="green":
    print("就获得5分")
else:
    print("就获得10分")
    #为黄色时
alien_color="red"
if alien_color=="green":
    print("就获得5分")
elif alien_color=="yellow":
    print("就获得10分")
elif alien_color=="red":
    print("就获得15分")
age=70
if age<2:
    print("这是婴儿")
elif age<4:
    print("这是幼儿")
elif age<13:
    print("这是儿童")
elif age<18:
    print("这是少年")
elif age<65:
    print("这是中青年")
else:
    print("这是老年")
fruits=["banana","plum","apple"]
if "banana" in fruits:
    print("banana")
if "banan" in fruits:
    print("banan")
favorite_fruits=fruits
if "banana" in favorite_fruits:
    print(f"You really like bananas!")
if "banan" in favorite_fruits:
    print(f"You really like bananas!")
if "apple" in favorite_fruits:
    print(f"You really like apples!")
# bb=["admin","jaden","banned","hasat","jkkkk"]
# if bb:
#     print("We need to find some users!")
# for bbb in bb:
#     if bbb=="admin":
#         print("Hello admin, would you like to see a status report?")
#     else:
#         print(f"Hello {bbb}, thank you for logging in again.")
bb=[]
if not bb:
    print("We need to find some users!")
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
        print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
current_users=["张三","李四","王五","朱六","赵七"]
new_users=["三张","李四","王五","朱六","七赵"]
for new_user in new_users:
    if new_user in current_users:
        print("需要输入其他用户名")
    else:
        print("这个用户名未被使用。")
numbers=[1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number==1:
        print(f"{number}st")
    elif number==2:
        print(f"{number}nd")
    elif number==3:
        print(f"{number}rd")
    else:
        print(f"{number}th")

    