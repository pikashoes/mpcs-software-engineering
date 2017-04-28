# Homework #1


**20 pts**

**Due in 7 days: Thursday, Jan 26 5:29pm**

![Coin Machine Photo](http://www.icrtouch.com/forum/uploads/gallery/album_6/gallery_907_6_42590.jpg)

### Instructions

Your job is to implement the software for a typical coin change machine
that you've likely seen at your local Walgreens or grocery store.

*NOTE: You can solve this in Java (using JUnit), Ruby (using minitest), or C++ (using CppUnit) if you prefer.  Simply provide your code and delete the Python files.*

* Do not fork this repository.  Download this code using the green "Clone or Download" button on GitHub, then select "Download ZIP"; or, clone this repository and remove the git data (`rm -rf .git`).

* Use the `coin_machine.py` file to implement a class named `CoinMachine` that can dispense coins,
for a given an amount of money from ranging from 0 to 99 cents.  You may
add more files/classes/modules as needed, but the `CoinMachine` class
should provide the public interface for the machine.

* Use the `coin_machine_test.py` file to write tests that
measure the quality of your implementation.

* Publish your code as a private GitHub repository, and add me as a collaborator (repository Settings / Collaborators). My GitHub username is `jeffcohen`.

### Requirements:

1. Given an amount from 0 to 99, the machine should determine the
optimal set of coins to dispense in order to minimize the number of coins.

2. The machine should simulate dispensing the coins by emitting something to the screen.

  For example, given the amount 45, it should emit:

  ```
      Dispensing: 1 quarter
      Dispensing: 2 dimes
  ```

3. The machine should return a data structure indicating the quantity
and types of coins that were dispensed.

4. If the machine is unable to dispense the amount given,
    it must not dispense any money. Instead, it must
    return an error code or raise an exception.

5. The machine should be initially configurable as to
    the number of coins in its inventory. For example, it might be stocked with 10 of each type of coin. After several transactions,
    it may run out of inventory of certain coins and must make change
    with the coins remaining (if possible).


### Grading

* 4 points per requirement with reasonable test coverage
