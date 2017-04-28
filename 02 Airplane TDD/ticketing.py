import cmd, csv, random

"""
Actions:
DONE > See the flight schedule
DONE > Add a new customer to the system
DONE > Lookup a customer by their frequent flyer number
DONE > Lookup a reservation by its 5-digit confirmation number
DONE > Make a new reservation
DONE > Cancel a reservation
DONE > See a list of passengers on a given flight
DONE > If the agent quits the app, then restarts it, they should be able to see all of data previously entered.
DONE > Implement Credit Card
"""

class MaroonAirShell(cmd.Cmd):
    intro = "\nWelcome to the MaroonAir Ticket Counter.\nType `help` or `?` to list commands. 'q' to quit.\n"
    prompt = '> '
    event = None

#==============================================================================
#                               INITIALIZING
#==============================================================================     
    with open('customers.csv') as csv_file:
        reader = csv.reader(csv_file)
        customers = {}
        customers = dict(reader)
        
    with open('reservations.csv') as csv_file:
        reader = csv.reader(csv_file)
        reservations = {}
        reservations = dict(reader)
        
    with open('flights.csv') as csv_file:
        reader = csv.reader(csv_file)
        flights = {}
        flights = dict(reader)

#==============================================================================
#                               ACTIONS
#==============================================================================         
    def do_q(self, arg):
        """Quit"""
        with open('customers.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            for k, v in self.customers.items():
                writer.writerow([k, v])
        
        with open('reservations.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            for k, v in self.reservations.items():
                writer.writerow([k, v])
        
        with open('flights.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            for k, v in self.flights.items():
                writer.writerow([k, v])      
        
        return True

    def do_EOF(self, arg):
        return True
    
    def do_erase_all(self, arg):
        """Erase ENTIRE database"""
        check = input("Are you SURE you want to delete the entire database? Y/N: ")
        if (check == "Y" or check == "yes" or check == "Yes" or check == "y"):
            print("Deleting entire database. Your changes will be saved when you exit the application.")
            self.customers.clear()
            self.reservations.clear()
            self.flights.clear()
        else:
            print("Nothing was deleted.")
            return

#==============================================================================
#                               SCHEDULE
#============================================================================== 
    def do_schedule(self, arg):
        """Display today's flight schedule"""
        for destination in self.read_schedule():
            print("Flight #" + destination["flight_num"],
                  "to", destination["destination"].upper(),
                  "at", destination["departure"],
                  "arrives", destination["arrival"],
                  "$" + destination["price"])

    def read_schedule(self):
      rows = []
      with open('schedule.csv') as csv_file:
        schedule = csv.DictReader(csv_file)
        for row in schedule:
          rows.append(row)
      return rows

#==============================================================================
#                               CUSTOMERS
#============================================================================== 
    def do_customer_lookup(self, ffn):
        """Look up a customer using the frequent flyer number.\nFormat is: customer_lookup <ffn>"""
        if (ffn == ''):
            print("ERROR: Format is: customer_lookup <ffn>")
            return

        if ffn in self.customers:
            print(self.customers[ffn])
        else:
            print("ERROR: No such customer in database.")
            return None
    
    def do_customer_add(self, arg):
        """Add a customer to the database.\nFormat is: customer_add <firstname> <lastname>"""
        if (arg == ''):
            print("ERROR Format is: customer_add <firstname> <lastname>")
            return
            
        arg = arg.split()
        print(arg)
        if len(arg) != 2:
            print("ERROR Format is: customer_add <firstname> <lastname>")
            return
            
        fname = arg[0]
        lname = arg[1]
        ffn = str(self.getRandomNumber("customer"))
        self.customers[ffn] = [fname, lname]
        print(ffn + ": " + str(self.customers[ffn]) + " added.")

#==============================================================================
#                               RESERVATIONS
#==============================================================================        
    def do_reservation_make(self, arg):
        """Make a reservation.\nFormat is: reservation_make <flight> <customer_ffn> <credit_card>"""
        if (arg == ''):
            print("ERROR: Format is: reservation_make <flight> <customer_ffn> <credit_card>")
            return
            
        arg = arg.split()
        if len(arg) != 3:
            print("ERROR: Format is: reservation_make <flight> <customer_ffn> <credit_card>")
            return
        
        flight = arg[0]
        customer_ffn = arg[1]
        credit_card = arg[2]
        
        if not self.check_credit_card(credit_card):
            print("ERROR: Invalid credit card. We only accept valid 6-digit VISA, MasterCard, and Discover cards.")
            return
        
        reservation_num = str(self.getRandomNumber("reservation"))        
        self.reservations[reservation_num] = [flight, customer_ffn, credit_card]
        
        if flight in self.flights:
            self.flights[flight].append(customer_ffn) 
        else:
            self.flights[flight] = customer_ffn
        
        print("Reservation Number: " + reservation_num + ", Flight #, Customer, Credit Card: " + str(self.reservations[reservation_num]))

    def do_reservation_cancel(self, reservation_num):   
        """Cancel a reservation.\nFormat is: reservation_cancel <reservation_num>"""
        if (reservation_num == ''):
            print("ERROR: Format is: reservation_cancel <reservation_num>")
            return

        flight = self.reservations[reservation_num][0]
        
        try:
            del self.flights[flight]
        except KeyError:
            print("ERROR in  making reservation. Flight doesn't have reserveration.")
            return
            
        self.reservations.pop(reservation_num, None)
        #Returns item if successful, None if does not exist
    
    def do_reservation_lookup(self, reservation_num):
        """Lookup reservation using confirmation number.\nFormat is: reservation_lookup_confirmation_num <reservation_num>"""
        if (reservation_num == ''):
            print("ERROR: Format is: reservation_lookup_confirmation_num <reservation_num>")
            return
            
        if reservation_num in self.reservations:
            print(self.reservations[reservation_num])
            return
        else:
            print("ERROR: No such reservation in database.")
            return None
    
    def do_check_flight(self, flight_num):
        """Check customers on a flight.\nFormat is: check_flight <flight_num>"""
        if (flight_num == ''):
            print("ERROR: Format is: check_flight <flight_num>")
            return
            
        if flight_num in self.flights:
            for customer_id in self.flights[flight_num]:
                print("FFN: " + customer_id + ", Name: " + self.customers[customer_id])
            return
            
        else:
            print("No passengers on this flight.")
            return None

#==============================================================================
#                               PRINTING FUNCTIONS
#==============================================================================   
    def do_customers(self, arg):
        """Display all customers"""
        print(self.customers)
    
    def do_reservations(self, arg):
        """Display all reservations"""
        print(self.reservations)
    
    def do_flights(self, arg):
        """Display all flights that have customers"""
        print(self.flights)

#==============================================================================
#                               HELPER FUNCTIONS
#==============================================================================     
    def getRandomNumber(self, category):
        random_number = random.randint(10000, 99999)
        if category == "customer":
            if random_number in self.customers:
                self.getRandomNumber("customer")
        else:
            if random_number in self.reservations:
                self.getRandomNumber("reservation")
        return random_number
    
    def check_credit_card(self, number):
        num_list = list(map(int, str(number)))
        if len(num_list) != 6:
            return False
        
        if not ((num_list[0] == 3 and (num_list[0] == 4 or num_list[0] == 7)) or
        (num_list[0] == 5 and (num_list[0] == 5 or num_list[0] == 1)) or
        (num_list[0] == 4)):
            return False
        
        for i in range(len(num_list)):
            if (i%2 != 0):
                num_list[i] = 2 * num_list[i]
        
        total = 0
        
        for item in num_list:
            if len(str(item)) == 1:
                total += item
            else:
                while(item > 0):
                    tmp = item % 10
                    total += tmp
                    item /= 10
                    
        if (total % 10 == 0):
            return True
        return False
            
            
            

if __name__ == '__main__':
    MaroonAirShell().cmdloop()
