class Train:
    def __init__(self,ts):
        self.totalSeats=ts
        self.seats={}
        self.seatNum=0
        self.fares=1200
        
    def getStatus(self):
        print(f"Seats Left: {self.totalSeats-self.seatNum}")
        return
    
    def bookSeat(self):
        if self.seats!=self.totalSeats:
            self.seatNum+=1
            name=input(f"Payment: Rs.{self.fares}\nEnter your name: ")
            self.seats.update({name:self.seatNum})
            print(f"Seat booked successfully!\nSeat # {self.seats[name]}\nName: {name}")
        else:
            print("Train is full!")
        return
    
    def faresDetails(self):
        print(self.fares)
       

def main():
    train = Train(25)
    while True:
        print("\n1. Show fare details\n2. Book a seat\n3. Get status\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            train.faresDetails()
        elif choice == '2':
            train.bookSeat()
        elif choice == '3':
            train.getStatus()
        elif choice == '4':
            print("Thank you for using the train booking system!")
            break
        else:
            print("Invalid choice, please try again.")

main()