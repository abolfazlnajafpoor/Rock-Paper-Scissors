import random

choices = ["سنگ", "کاغذ", "قیچی"]

computer = random.choice(choices)
player = input("سنگ، کاغذ یا قیچی را وارد کنید:")

if player not in choices:
    print("ورودی نامعتبر است!")
else:
    print("انتخاب کامپیوتر:", computer)

if player == computer:
    print("مساوی!")
elif (player == "سنگ" and computer == "قیچی"):
    print("شما برنده شدید!")
elif (player == "کاغذ" and computer == "سنگ"):
    print("شما برنده شدید!")
elif (player == "قیچی" and computer == "کاغذ"):
    print("شما برنده شدید!")
else:
    print("کامپیوتر برنده شد")
