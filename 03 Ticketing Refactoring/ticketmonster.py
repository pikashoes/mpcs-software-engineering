import cmd
import urllib.request
import json
import ssl

class TicketShell(cmd.Cmd):
    intro = '\nWelcome to TicketMonster.   Type help or ? to list commands.\n'
    prompt = '\n> '
    event_code = None
    chart = None

    def do_q(self, arg):
      """Quit"""
      return True

    def do_EOF(self, arg):
      return True

    def do_event_list(self, arg):
        """Lists all events for sale"""
        print("Event Code  Date        Description")
        print("----------  ----------  --------------------------------------------------")
        print("UC1         03/25/2016  Chicago Blackhawks vs St. Louis Blues at the United Center")
        print("UC2         03/27/2016  Chicago Blackhawks vs Minnesota Wild at the United Center")
        print("H1          04/11/2016  Hamilton at Chicago Theater")
        print("H2          04/12/2016  Hamilton at Chicago Theater")
        print("H3          04/13/2016  Hamilton at Chicago Theater")
        print("U2          07/06/2016  U2 at Soldier Field")
        print()
        print("To view available tickets, enter: 'event [event code]'")

    def do_event(self, event_code):
        """Displays the seating map for an event and makes it the 'current' event.  """

        event_name = None
        event_name = {
                     "UC1" : "UC1: 03/25/2016 - Chicago Blackhawks vs St. Louis Blues at the United Center",
                     "UC2" : "UC2: 03/27/2016 - Chicago Blackhawks vs Minnesota Wild at the United Center",
                     "H1"  : "H1: 04/11/2016 - Hamilton at Chicago Theater",
                     "H2"  : "H2: 04/12/2016 - Hamilton at Chicago Theater",
                     "H3"  : "H3: 04/13/2016 - Hamilton at Chicago Theater",
                     "U2"  : "U2: 07/06/2016 - U2 at Soldier Field",
                     None  : None
                     }.get(event_code, None)

        if event_name is not None:
            self.event_code = event_code

            # load seating chart for this event
            # look at one of the .dat files for an example
            chart = {}
            try:                
                with open('charts/events/' + event_code + ".dat", 'r') as f:
                  chart["code"] = event_code
                  for line in f:
                    section, row_number, seats = line.split()
                    if not section in chart:
                      chart[section] = {}
                    chart[section][row_number] = seats
    
                self.chart = chart
            except:
                print("ERROR: event data not found. Please contact support for help.")
                return
                
            print(event_name)
            print("Enter 'seats' for current seating chart and availability.")
        else:
            print("I don't recognize that event code. Enter 'event_list' to see the list of events and use the format: event <event code>.")

    def do_buy(self, arg):
        """Show the best available tickets for a given section"""
        
        try:
            section, row, seat_number, cc_number = arg.split()
        except:
            print("You need to indicate which seat you want to buy.\n")
            print("The format is: 'buy <section> <row> <seat number> <cc number>' WITHOUT any punctuation.")
            return
        
        if self.chart is not None:
            x = buy_ticket(self.chart, section, row, int(seat_number), cc_number)
            if x == 1:
                print("Ticket purchased!")
                # Print the current seating chart
                for row in self.chart[section].keys():
                    print(row.ljust(3), self.chart[section][row])
            elif x == 0:
                print("That seat is occupied.")
            elif x == -2:
                print("Payment not authorized.")
            elif x == -3:
                print("That section does not exist.")
            elif x == -4:
                print("That row number does not exist.")
            else:
                print("That seat doesn't exist.")
            return
        else:
            print("Select an event by using the `event` command.")
            return
        

    def do_seats(self, arg):
        """See the current seating for a given section"""
        arg = arg.strip()

        if not self.chart:
            print("No event selected. Please select an event first using: \n \t'event <event_code>'. \nUse 'events' to see the list of events.")
            return
            
        if len(arg) == 0:
            print("To see the section chart, use 'seats [section]', where section is one of:")
            # Figure out the list of sections in the current venue.
            # It's mostly just the keys in the chart dictionary,
            # but the 'name' key should be ignored (it holds the filename.)
            sections = list(self.chart.keys())
            sections.remove('code')
            print(" ".join(sections))
        elif arg not in self.chart:
            print("Your seat section was not valid. Please try again.")
        else:
            # Print the current seating chart
            print("\nLegend: [-] Seat Available                  [X] Seat Already Sold")
            print("To buy a seat, enter 'buy [section] [row] [seat-number] [cc-number]'")
            print("All seat numbers start at 1 on the far left.")
            print("\nSECTION", arg)
            print()
            for row in self.chart[arg].keys():
                print(row.ljust(3), self.chart[arg][row])


### Utility Functions

def save_chart(chart):
  filename = "charts/events/{0}.dat".format(chart['code'])
  with open(filename, 'w') as f:
    for section in chart:
      if section != 'code':
        for row_number in chart[section].keys():
          row_line = "{0} {1} {2}\n".format(section, row_number.rjust(3), chart[section][row_number])
          f.write(row_line)

# Example credit card numbers: 4111111111111111, 5105105105105100, 6011111111111117
def buy_ticket(chart, section, row_number, seat_number, credit_card_number):
  # Make sure we have sane inputs...
    if section not in chart:
        return -3
        
    if chart is not None and chart[section] is not None:
        if row_number not in chart[section]:
            return -4
        elif chart[section][row_number] is not None:
        # Check to make sure seat is available
            row_chart = chart[section][row_number]
            try:
                if row_chart[seat_number-1] == '-':
              # seat is available! let's try to buy it
              # first let's verify the credit card
                    url = "https://www.jeffcohenonline.com/creditcard.json?cc=" + credit_card_number
                    ctx = ssl.create_default_context()
                    ctx.check_hostname = False
                    ctx.verify_mode = ssl.CERT_NONE
                    try:
                        data = json.loads(urllib.request.urlopen(url, context=ctx).read().decode('utf8'))
                        if data["success"]:
                          # Sold!
                          # Now save the updated seating chart to disk
                          new_row_chart = row_chart[0:seat_number-1] + "X" + row_chart[seat_number:]
                          chart[section][row_number] = new_row_chart
                          save_chart(chart)
                          return 1
                        else:
                          return -2  # credit card API says card is invalid
                    except:
                        return -2 # credit card API is offline
                else:
                    return 0 # seat is occupied
            except:
                return -1
    else:
       return -1  # invalid args

if __name__ == '__main__':
    TicketShell().cmdloop()
