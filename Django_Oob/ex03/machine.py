import random
from beverages import *

class CoffeeMachine:

    def __init__(self, name="Coffee Machine"):
        self.name = name
        self.serve_count = 0
    
    class EmptyCup(HotBeverage):

        def __init__(self, name="empty cup", price=0.90):
            super().__init__()
            self.name = name
            self.price = price

        def description(self):
            return "An empty cup?! Gimme my money back!"
        
    class BrokenMachineException(Exception):
        def __init__(self, message="This coffee machine has to be repaired."):
            super().__init__(message)

    def repair(self):
        print("This coffee machine has been repaired.")
        self.serve_count = 0
    
    def serve(self,sweet_beverage : HotBeverage):
        if self.serve_count >= 10:
            raise CoffeeMachine.BrokenMachineException()
        self.serve_count += 1
        return random.choice([sweet_beverage, CoffeeMachine.EmptyCup()])
    
def main():
    coffee_machine = CoffeeMachine()
    try :
        for i in range(11):
            if i < 10:
                print(f"    ------ Drink number : {i + 1} ------")
            print(coffee_machine.serve(Coffee()))
    except CoffeeMachine.BrokenMachineException as e:
        print(f"\033[91m    ------ Machine Broken ------\033[0m")
        print(e)
        print(f"\033[92m    ------ Machine Repair ------\033[0m")
        coffee_machine.repair()
    try :
        for j in range(11):
            if j < 10:
                print(f"    ------ Drink number : {j + 1} ------")
            print(coffee_machine.serve(Tea()))
    except CoffeeMachine.BrokenMachineException as e:
        print(f"\033[91m    ------ Machine Broken ------\033[0m")
        print(e)
        print(f"\033[92m    ------ Machine Repair ------\033[0m")
        coffee_machine.repair()

if __name__ == '__main__':
   main()