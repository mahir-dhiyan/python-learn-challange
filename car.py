class Car: 
    wheels=4 #Class variable
    def __init__(self,make,model,year,color):
        self.make=make #These are instance variables
        self.model=model
        self.year=year
        self.color=color
    def drive(self):
        print("This "+ self.model +" is driving")

    def stop(self):
        print("This "+ self.model +" is stopped")