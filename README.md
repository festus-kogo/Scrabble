### Scrabble
In this project, you will process some data from a group of friends playing scrabble. You will use dictionaries to organize players, words, and points.

There are many ways you can extend this project on your own if you finish and want to get more practice!

### Build your Point Dictionary
**1.** We have provided you with two lists, `letters` and `points`. We would like to combine these two into a dictionary that would map a letter to its point value.

Using a list comprehension and `zip`, create a dictionary called `letter_to_points` that has the elements of `letters` as the keys and the elements of `points` as the values.
**2.** Our `letters` list did not take into account blank tiles. Add an element to the `letter_to_points` dictionary that has a key of `" "` and a point value of `0`.