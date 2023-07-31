# PythonProg NetworkXGraphs
 Message Passing using NetworkX Graphs

 Code Files:
 1. dracula.py

## University of Galway Programming and Tools for AI
## (CT5132/CT5148) 2022/23 Assignment 3
## James McDermott
Suppose there is a Halloween party at the Students’ Union, and everyone who attends wears a costume that
fully disguises their real identity. <br><br>
During the party, Dracula talks to a Pumpkin. The next day, Dracula decides it would be nice to meet the
Pumpkin again. But Dracula doesn’t know the Pumpkin’s real name. How can Dracula find the Pumpkin?<br><br>
Luckily, everyone at the disco is a member of one or more Student Societies. Before the disco, each Society
had a meeting to choose their costumes in secret. So, everyone in a particular Society knows the costume of
everyone else in the society, but they don’t know the costume of anyone outside the society.<br><br>
For example, suppose Dracula is a member of the Karate Society and the Debating Society. Dracula can ask
everyone in those Societies whether they know the Pumpkin’s real name. If not, they can ask anyone they
know in other Societies, and so on, recursively.<br><br>
Here are the memberships of each Society (this is a small example):
> {<br>
> "Karate Society": ["Dracula", "Frankenstein", "Werewolf", "Pilot", "Luke", "Leia"],<br>
> "Debating Society": ["Dracula", "Frankenstein", "Leia", "Cockroach", "Iron Man", "Zombie"],<br>
> "Musical Society": ["Bunny", "Pumpkin", "Cinderella", "Goblin Queen", "Goblin King"],<br>
> "History Society": ["Bunny", "Pilot", "Luke"]<br>
> }<br>
<br>

Dracula wonders: Will I ever find the Pumpkin? Who exactly will pass my message on at each step? In this
example, we can see the path: [Dracula, Luke, Bunny, Pumpkin]. There are other paths equally long,
but none shorter.<br><br>
Write a program to answer these questions. It should work in general, not just for the example given above.
It should show the list of people who will pass the message from Dracula to Pumpkin (in order) or else
should output that the message will not reach Pumpkin.<br><br>
The Societies will be given in an input file, e.g. one of the following, provided in Bb.<br>
- societies1.txt<br>
- societies2.txt<br><br>

Your program should be named dracula.py and it will be called e.g. as follows:<br>
$ python dracula.py societies1.txt<br><br>
It should read the input specified on the command line (i.e. don’t copy-paste the input into your program)
and provide the solution, and should work for either input.<br><br>
Hint 1: you can use ‘eval’. Hint 2: you can use NetworkX if you like, but you don’t have to.
