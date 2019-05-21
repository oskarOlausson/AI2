# AI2
Back propagation network designed to recognize emotions in smiley, invariant to the rotation of the smiley.


The images looked like this:


![](https://oskarolausson.github.io/profilePage/static/img/faces/michevious.png)



This one is rotated 180 degrees and is michevious

# Algorithm

The backpropagation-algorithm learns by using a single layered neural network (required by specs). Each node in the network looks at one pixel and makes a guess. In the training phase all nodes are moved slighlty towards the right guess if the guess was wrong. This made the AI able to guess correctly 67% between the 4 emotions the smileys could have.


To make it better, we pre-rotaded the smileys using a heuristic that allowed us to guess where the eyes were (the darkest part of the image) and rotated it before we guesses. This made the algorithm 98% effective.

To bring it up to 100% we split the network into analyzing the top-part (the eyes) and the bottom-part (the mouth) separately.

The eyes could be in one of two states, / \ or \ /. And the mouth could be happy or sad.

We then grabbed the guesses from the two networks and determinated the result based upon the two guesses.
