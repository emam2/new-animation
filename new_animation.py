import turtle
import time

# স্ক্রিন সেটআপ
screen = turtle.Screen()
screen.setup(width=600, height=600)  # স্ক্রীন সাইজ সেট করা হয়েছে
screen.bgcolor("black")

# টার্টল সেটআপ
t = turtle.Turtle()
t.speed(2)

# হৃদয়ের আকৃতি আঁকার ফাংশন (বড় আকৃতি)
def draw_heart(color):
    t.color(color)
    t.begin_fill()
    t.left(50)
    t.forward(180)  # আকৃতির জন্য সামঞ্জস্য করা হয়েছে
    t.circle(70, 200)  # আকৃতির জন্য সামঞ্জস্য করা হয়েছে
    t.right(140)
    t.circle(70, 200)  # আকৃতির জন্য সামঞ্জস্য করা হয়েছে
    t.forward(180)  # আকৃতির জন্য সামঞ্জস্য করা হয়েছে
    t.end_fill()
    t.setheading(0)

# রঙের তালিকা
colors = ["red", "purple", "pink", "orange", "yellow"]

# হৃদয়ের এনিমেশন তৈরি
for color in colors:
    t.penup()
    t.goto(0, -50)  # হৃদয়ের অবস্থান ঠিক করা হয়েছে
    t.pendown()
    t.clear()
    draw_heart(color)
    
    # "I LOVE YOU RANI" লেখাটি ২ সেকেন্ড ধরে থাকবে
    t.penup()
    t.goto(-80, 70)  # লেখাটি উপরে এবং ডান দিকে সরানো হয়েছে
    t.pendown()
    t.color("#FF1493")
    t.write("I LOVE YOU RANI", font=("Arial", 18, "bold"))
    
    time.sleep(2)  # ২ সেকেন্ড অপেক্ষা

# সাদা বক্স আঁকার জন্য ফাংশন
def draw_box():
    t.penup()
    t.goto(-250, -100)  # বক্সের নতুন অবস্থান
    t.pendown()
    t.color("white")
    t.begin_fill()
    for _ in range(2):
        t.forward(500)
        t.left(90)
        t.forward(180)  # বক্সের উচ্চতা কমানো হয়েছে
        t.left(90)
    t.end_fill()

# বক্সের মধ্যে কবিতা লেখার ফাংশন
def write_poem():
    t.penup()
    t.goto(0, 10)  # কবিতার অবস্থান মাঝের দিকে সেন্টার করা
    t.pendown()
    t.color("#FF1493")
    poem = """তোমার সাথে কাটুক আমার সারাটি জীবন,
তোমাকে ভালোবাসবো প্রতিক্ষণ, প্রতিদিন।
তুমি যে আছো আমার হৃদয়ের গহীনে,
সারা জীবন চাই তোমাকে পাশে এই জীবনভর বাঁধনে।
তুমি কি থাকবে আমার পাশে আজীবন???"""
    
    # কবিতার লেখাগুলো মাঝখানে বসানোর জন্য 
    for line in poem.split('\n'):
        t.write(line, align="center", font=("Arial", 10, "bold"))  # লেখার সাইজ সামান্য কমানো হয়েছে
        t.penup()
        t.goto(0, t.ycor() - 25)  # পরবর্তী লাইনে যাওয়ার জন্য কিছু নিচে যাবে
        t.pendown()

# এনিমেশন শেষ হওয়ার পর বক্স ও কবিতা দেখানো
t.clear()  # লাভ মুছে ফেলা
draw_box()  # বক্স আঁকা
write_poem()  # কবিতা লেখা

# স্ক্রিন ধরে রাখা
t.hideturtle()
screen.mainloop()
