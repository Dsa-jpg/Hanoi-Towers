# Hanoi-Towers
                                           
![giphy](https://user-images.githubusercontent.com/65063262/209709444-1bc99434-5c5d-471e-8ba3-4bbc56623217.gif)

# Here's a brief overview of how the code works:

1) The code first imports the turtle and time modules.

2) It then sets up the GUI for the game using the turtle module, creating the base and 3 pins.

3) The Pin and Disc classes are defined to create the visual representation of the pins and discs in the game. The Pin class keeps track of the number of discs on each pin and the positions of each disc, while the Disc class stores the size and color of each disc.

4) The move_disc function is defined to move a disc from one pin to another. It uses a while loop to incrementally move the disc up or down to the desired position on the target pin.

5) The move function is defined to move a disc from one pin to another based on the given source and target pins. It uses the move_disc function to physically move the disc and updates the count and list of discs on each pin.

6) The hanoi function is the recursive solution to solve the Tower of Hanoi game. It takes in the number of discs, and the source, helper (via), and target pins as arguments. It first moves all but the bottom disc to the helper pin using the target pin as a temporary holding place. It then moves the bottom disc to the target pin. Finally, it moves the rest of the discs from the helper pin to the target pin using the source pin as a temporary holding place.


I hope this helps!

Time complexity is : O(2^n - 1)

Examples ->
7 disks -> 127 moves
6 disks -> 63 moves
5 drives -> 31 moves
4 discs -> 15 moves
3 discs -> 7 moves
2 disks -> 3 moves
1 disk ->1 move

# Don't forget for installing this package:

# Python Turtle 

Ubuntu Linux: sudo apt-get install -y python3-wxgtk4.0

Fedora: python3 -m pip install wxpython

On any GNU/Linux distribution: python3 -m pip install --user PythonTurtle PythonTurtle






