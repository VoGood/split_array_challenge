# Split Array Challenge

This code is submitted as an answer to the assignment Twig Coding Challenge included in 
the hiring process for the position _Back-End Web Developer_ at Twig Education.
Its instructions may be found in the document `doc/Twig Education Coding Challenge - March 2019.pdf`.


## Index

* [Problem Statement](#problem-statement)
  * [Example pseudo-code](#requirements)
  * [Programing language](#programing_language)
* [Solution](#solution)
  * [How to run](#how-to-run)
  * [Tests](#test)



## Problem Statement ##

### Requirements ### 

Given an array of length >= 0, and a positive integer N, return the contents of the array divided into N
equally sized arrays.
Where the size of the original array cannot be divided equally by N, the final part should have a length equal
to the remainder.

### Example pseudo-code ###
```
groupArrayElements([ 1 , 2 , 3 , 4 , 5 ], 3 );
// [ [ 1, 2 ], [ 3, 4 ], [ 5 ] ]
```

### Programing language ###

The code is written in Python 3.7.1.

## Code structure and usage

All the application proper is fully contained in the single top-level module `split_array`. 
Type hints are present in all relevant signatures and basic documentation is included in the code itself.

## Solution ## 

### How to run ###

```
from split_array import split
new_array = split([1,2,3,4,5,6,7],2);
print(new_array.splitter_operator)
```

### Tests ###
The following tests have been implemented:

   * If size of the original array cannot be divided equally by N, the final part will return length equal
to the remainder.
   * Test for even split.
   * Empty the array test.
   * Test if the splitter is non-integer.
   * Test if the splitter is negative integer.
   * Test for the input array type.
   
A moderately extensive suite of tests is included in `tests/`. The autodiscovery feature of `unittest` makes it fairly convenient to run them by executing the following command:
 ````
$ git clone https://github.com/VoGood/split_array_challenge
$ cd split_array_challenge/
$ python -m unittest -v
````
The `-v` switch is optional and it stands for its verbose mode.
