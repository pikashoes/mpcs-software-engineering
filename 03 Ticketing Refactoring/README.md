STEPS I TOOK TO IMPROVE THE CODE:

Initial Run
----------------------------
First thing I did was test each function without any arguments.

1. events:

	>There are no arguments required, so no problems here.

2. event:

	> The print statement was not very informative in telling the user what to input instead, so I modified it to indicate the correct format.

3. buy:

	> There was an error when I used this without arguments, so I edited it to print the correct format for the user and put a 'return' so that the program didn't crash.

4. seats:

	> Without going through 'event' first, there were no charts to unpack. So I made self.chart an instance variable that was initialized to 'None', and when the self.chart is None, then I had it print out instructions to select an event first.

Help Test
----------------------------
I then checked to make sure there were 'help' texts available for all of them. There were, so no changes here!

Refactoring
----------------------------
1. To focus on individual functions, I first looked at the 'events' function. The name of the function was not clear enough for me to indicate what it is. So I changed it from 'events' to 'event_list'.

2. Next I focused on making the 'do_event' function better.

	> First, I replaced all the 'if, else' statements with a dictionary that simulates a 'case, switch' in Java. The default is None.

	> I realized also that if the file were nowhere to be found, for whatever reason, there was no error handling for it. So I added a 'try, except' that makes sure it doesn't crash the program.

3. I then looked at 'buy'.

	> I found that when I went through all the correct steps and then tried to buy a ticket, but put in wrong things (like a comma), it threw a ValueError instead of letting me try again. So I fixed it to allow me to try again. I got rid of my if statement that originally checked if arg == 0 and instead put it in the 'except' part of the try.

	> I realized that there was a KeyError when I tried to buy a ticket, even if it was valid, and it was throwing the error from the section. I edited the if-else statements to prevent this error from closing the program.

4. Next, 'seats'.

	> The first problem I found is that after I've selected an event and then look at the seats, if I make a typo in the seat-name, there is an error and it exits the program. I added in a condition where if it was not a part of the dictionary self.chart, then the user had to enter a correct one.

5. The first utility function was 'save_chart'.

	> I couldn't find anything to improve.

6. The second utility function was 'buy_ticket'.

	> There were a lot of nested 'if' statements, so I merged the first two.

	> I also made the error cases much more specific (added in the -3 and -4 return which are clarified in the 'buy' function).

	> I also added a try-catch to make sure that the index was in range for the row_chart. If not, it returns -1.
