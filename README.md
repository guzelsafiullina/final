# final
This repo contains solution of final exam in SDwP
## angle.py
This file contain solution of task 1 from exam. You can test it with main_task1_task2.py.

More details:

This class works with coordinates of some object. User can write degrees, minutes and direction and class method print_angle() will print it beautifully.

## obj.py
This file contain solution of task 2 from exam. You can test it with main_task1_task2.py.
More details:
This class creates objects and gibe

## main_task2_task2.py
This file is created to test angle.py and obj.py

Here is the example of usage:
```python3
Input: 
45
45
W
Output:
0°0' W # this is autimatically created Class Object
45°45.0' W # this is coordinates with your parameters

Input:
181
43
E
Output:
Incorrect input #because you coordinates must be from 0 to 180 degrees

Input:
170
54
R
Output:
Incorrect direction #because direction must be W, E, N or S
#repeat it for 2 times
```
As a minus, you have to do it 5 times, before you get access to the second task results.
Be careful, this program doesn't check if minutes are less than 60.

After repeating previous steps there will be output:
```python3
Output:
My number is 21 with time of creation 2021-10-07 15:55:40.247668
My number is 34 with time of creation 2021-10-07 15:55:40.249080
My number is 55 with time of creation 2021-10-07 15:55:40.250080
```
It's result of creating and printing of 3 objects with different labels and time of its creation
## sheep.py
This is the solution of 3 task. It works with location of ships and numbers of existing ships. 
You can test it in main_task_3.py.
Requirements: obj.py, angle.py, sys
More details:
Sheep - is a class that store the name of ship, it's capacity, location and its unique label. It also print all information and doesn't allow user to create more than certain number of ships.

## main_task_3.py

This file was created to test sheep.py

```python3
Input:

Output:
My location is 56°67' E
My name is Maria
 My capacity is 32
My number is 21 with time of creation 2021-10-07 18:43:51.189100
My location is 13°54' N
My name is Mary
 My capacity is 54
My number is 34 with time of creation 2021-10-07 18:43:51.191095
My location is 12°35' S
My name is Friend
 My capacity is 45
My number is 55 with time of creation 2021-10-07 18:43:51.191095
Too many sheeps in the ocean
Only 3 ships are allowed in the ocean #this messages occurs while trying create 4th ship.
```

