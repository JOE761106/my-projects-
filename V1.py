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
        self.bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
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
        pass




window = tk.Tk()

app = calorie_app(window)   

window.mainloop()
