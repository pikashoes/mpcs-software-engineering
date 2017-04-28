HOW TO RUN:
-----------
In the terminal, write "python ticketing.py" to launch the command prompt. You may use the help functions built into the application to navigate, make reservations, add customers, etc.

WHAT IS IN THE DIRECTORY:
-------------------------
- customers.csv, flights.csv, reservations.csv, schedule.csv:
	> All the background "databases" that contain information to allow the agents to see their changes when they log in again.
- ticketingtest.py
	> The test file
- ticketing.py
	> The main python file

NOTES:
------
1. When developing this using TDD, initially I began by writing the unit tests as we had done in class. However, I ran into my first roadblock: how to test when things aren't being returned, but printed.
2. So while I initially began by writing functions that returned things (not void), I found that it was difficult to continue this testing method because I couldn't test it on the interface.
3. I saw on a Piazza post that how and what we choose to test is a decision we make, so I decided to test via the terminal on single functions.
4. I began with customer adding/look up and also the csv file that would allow for it to be saved.
5. Because I knew that the reservations and flights would be similar in terms of the csv file, I added that.
6. Then I tested the reservations adding and look up system.
7. I then did the flights, which I implemented within the reservations adding system.
8. My final test was for credit card validation(which I included in the unit test file because it actually returns True or False).

Overall, I implemented all the features and they worked for me. I finished it up by adding in more helpful descriptions for each function and error handling.