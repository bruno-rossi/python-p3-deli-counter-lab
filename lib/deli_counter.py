katz_deli = ["Logan", "Avi", "Spencer"]

def line(katz_deli):

    if len(katz_deli) == 0:
        print("The line is currently empty.") 
    else:

        customers = []
   
        for person in katz_deli:
            customers.append(f"{katz_deli.index(person) + 1}. {person}")
        
        print(f"The line is currently: {' '.join(customers)}")

line(katz_deli)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {katz_deli.index(katz_deli[-1]) + 1} in line.")

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        del katz_deli[0]