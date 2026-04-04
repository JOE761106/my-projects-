import tkinter as tk

kg_ask = "enter weight in kilograms"
age_ask = "enter age in years"
hours_ask = "enter how many hours you exercise per week"
height_ask = "enter height in meters"

asking = [kg_ask, age_ask, hours_ask, height_ask]

class calorie_app:
    def __init__(self , window):
        self.window = window
        self.weight = 0.0
        self.height = 0.0
        self.age = 0
        self.bmi = 0.0
        self.info = []
        self.bmr = 0.0
        self.activity = 0.0
        self.tdee = 0.0
        self.calories = 0.0
        self.productivity = 0
        self.meal_history = []
        self.calories_eaten = 0.0
        self.remain = 0.0
        self.calories_per_100g={
            "apple": 52,
            "banana": 89,
            "orange": 47,
            "strawberry": 32,
            "grapes": 69,    
            "carrot": 41,
            "broccoli": 34,
            "tomato": 18,
            "cucumber": 15,
            "potato": 77,
        
            "rice": 130,
            "white bread": 265,
            "pasta": 131,
            "oats": 389,
            "corn": 96,

            
            "egg": 155,
            "chicken breast": 165,
            "beef": 250,
            "tuna": 132,
            "lentils": 116,
            "milk": 42,
            "cheese": 402,
            "yogurt": 59,
            "butter": 717,
            "mozzarella": 280,
            "almonds": 579,
            "peanuts": 567,
            "walnuts": 654,
            "cashews": 553,
            "olive oil": 884,

    }


        for i, text in enumerate(asking):
            tk.Label(window, text=text).grid(row=i, column=0, padx=10, pady=10)

            entry = tk.Entry(window)        # moved inside loop
            entry.grid(row=i, column=1, padx=10, pady=10)

            self.info.append(entry)

        tk.Button(window, text="Submit", command=self.send_data)\
            .grid(row=4, column=0, columnspan=2, pady=15)

    def delete(self):
        for widget in self.window.winfo_children():
            widget.destroy()
    def send_data(self):
        self.weight = float(self.info[0].get())
        self.age = int(self.info[1].get())
        self.productivity = int(self.info[2].get())
        self.height = float(self.info[3].get())

        self.bmi = self.weight / self.height**2
    
        for widget in self.window.winfo_children():
            widget.destroy()
        self.calc_calories()
    def calc_calories(self):
        self.bmr = 10 * self.weight + 6.25 * (self.height * 100) - 5 * self.age + 5
        if self.productivity == 0:
            self.activity = 1.2
        elif self.productivity <= 2:
            self.activity = 1.375
        elif self.productivity <= 4: 
            self.activity = 1.55
        elif self.productivity <= 6:
            self.activity = 1.725
        else:
            self.activity = 1.9
        self.tdee = self.bmr* self.activity
        self.calories = self.tdee + 500
        self.second_screen()
        

    def second_screen(self):
        if self.bmi < 18.5:
            text = "You are just skin and bones wanna gain weight skelly?"
        elif self.bmi > 24.9:
            text = "You are a fatty fat fat wanna lose weight chud?"
        else:
            text = "Your weight is healthy. Want to maintain it?"

        tk.Label(self.window, text=text).grid(row=0, column=0, padx=10, pady=10)
        
        tk.Button(self.window, text="yes" , command= lambda:[self.delete() , self.third_window()] ).grid(row=1, column=0, pady=10)
        tk.Button(self.window, text="no"  , command=window.destroy).grid(row=2, column=0, pady=10)
    def third_window(self):
        tk.Label(self.window, text="Here is a page that could help you ").grid(row=0, column=0, padx=10, pady=10)
       
        tk.Button(self.window, text="continue" , command = lambda:[self.delete() , self.fourth_page()] ).grid(row=1, column=0, pady=10)
        
        tk.Label(self.window, text="https://en.wikipedia.org/wiki/Bodybuilding").grid(row=2, column=0, padx=10, pady=10)

    def fourth_page(self):
        if self.bmi>24.9:
            self.calories = self.tdee-500   
        if 18.5<self.bmi<24.9:
            self.calories = self.tdee
        tk.Label(self.window , text="goal:"+str(self.calories) , font=("Helvetica" , 10 , "bold")).grid(row = 2 , column=0 , padx=10 , pady=10 )
        tk.Label(self.window , text="eaten:" + str(int(self.calories_eaten)), font=("Helvetica" , 10 , "bold")).grid(row = 3 , column=0 , padx=10 , pady=10 )
        remaining = self.calories - self.calories_eaten
        tk.Label(self.window , text="remaining:" +str(remaining)  , font=("Helvetica" , 20 , "bold")).grid(row = 4 , column=0 , padx=10 , pady=10 )
        tk.Button(self.window , text="add food:" , font=("Helvetica" , 13 , "bold" , ) , command = lambda:[self.delete() , self.calorie_screen()]).grid(row = 5 , column=0 , padx=10 , pady=10 )
        tk.Label(self.window , text="meal history:" , font=("Helvetica" , 14 , "bold")).grid(row = 6 , column=0 , padx=10 , pady=10 )
        for i, meal in enumerate(self.meal_history):
            tk.Label(self.window, text=meal).grid(row=11 + i, column=0)
    def calorie_screen(self):
        self.food_var = tk.StringVar()
        self.food_var.set("apple")  

        self.food_menu = tk.OptionMenu(
            self.window,
            self.food_var,
            *self.calories_per_100g.keys()
        )
        self.food_menu.grid(row=4, column=0, padx=10, pady=1)
        self.food_menu.grid(row=4, column=0, padx=10, pady=10)
        tk.Label(self.window , text="choose the food you ate" , font=("Helvetica" , 10 , "bold")).grid(row = 3 , column=0 , padx=10 , pady=10 )
        tk.Label(self.window , text="enter amount of grams the food you ate" , font=("Helvetica" , 10 , "bold")).grid(row = 6 , column=0 , padx=10 , pady=10 )
        self.grams_entry = tk.Entry(self.window)
        self.grams_entry.grid(row=7, column=0, padx=10, pady=5)
        tk.Button(
            self.window,
            text="confirm",
            font=("Helvetica", 13, "bold"),
            command=lambda: [self.add_food(), self.delete(), self.fourth_page()]
            ).grid(row=9, column=0, padx=10, pady=2)
        tk.Button(self.window , text="back to main menu" , font=("Helvetica" , 13 , "bold" , ) , command = lambda:[self.delete() , self.fourth_page()]).grid(row = 10 , column=0 , padx=2 , pady=10 )
    def add_food(self):
        food = self.food_var.get()
        grams = float(self.grams_entry.get())
        calories_for_food = (self.calories_per_100g[food] / 100) * grams
        self.calories_eaten +=calories_for_food
        self.meal_history.append(
            f"{food} - {grams}g ({int(calories_for_food)} cal)"
    
        )
window = tk.Tk()

app = calorie_app(window)   

window.mainloop()
