# Cycles
```
### Directing

Director - Directs the game


### Scripting

Action - A thing that is done (overridden by other Action children classes)
Script - A collection of actions to perform each "turn"
Control Actors - Gets direction and moves the bike [child of Action]
Draw Actors - Draws actors on the screen [child of Action]
Handle Collisions - Checks if a player has collided with a trail [child of Action, and an implementation of Action interface]]
Move Actors - Update all actors' new positions [child of Action, and an implementation of Action interface]
Update Scores - Adds to the scores as needed [child of Action]


### Casting/Actors

Actor - A thing that does something
Cycle - The bike(s) controlled by the player(s) [child of Actor]
Cast - A collection of actors and groups of actors
Score - An object that keeps track of a player's score [child of Actor]


### Services

Keyboard Service - Gets inputs from the keyboard
Video Service - Puts outputs on the screen


### Other

Color - Holds an RGBA color value
Point - Holds location info
```
