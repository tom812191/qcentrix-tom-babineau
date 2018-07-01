# Q-Centrix Screening Problem for Tom Babineau

## The Problem
> Given an array of integers as input to your function, find the maximum possible product of 3 integers in the array.
>
> Example
> [1, 3, 7, 9] yields the maximum product of 3 values as 189 (3*7*9)
>
> Notes:
> Please be sure to carefully address edge cases for this problem. If you need any clarification on which cases to consider and which to ignore, please ask before submitting your code. Make reasonable decisions on how to handle any exceptional cases and where to draw the line on edge case detection.
>
> Submit code to calculate the above, please also include a spec / test file of unit tests for your code. Any language may be used but we prefer: Ruby, Python, JavaScript, C# or Java.

## The Solution
The file max_product.py contains two functions:
1. max_product
2. max_product_fast

Both implement solutions to the problem. The first runs in *O(n log n)* time due to a sorting operation, but has more straightforward code. The second runs in *O(n)* time, but the code is slightly more complex.

A quick performance benchmark run in profile/max_product_profile.py shows that in practice, either could be used for arrays of size less than 10^8, but the *O(n)* implementation would be prefered for anything larger.

### Performance Results
Times are in seconds:
> max_product: 1.9311904907226562e-05 for array of length 10
> max_product_fast: 1.4066696166992188e-05 for array of length 10
> max_product: 2.2172927856445312e-05 for array of length 100
> max_product_fast: 2.7894973754882812e-05 for array of length 100
> max_product: 0.00020384788513183594 for array of length 1000
> max_product_fast: 0.00015807151794433594 for array of length 1000
> max_product: 0.0023908615112304688 for array of length 10000
> max_product_fast: 0.0014920234680175781 for array of length 10000
> max_product: 0.02609086036682129 for array of length 100000
> max_product_fast: 0.017785072326660156 for array of length 100000
> max_product: 0.2847020626068115 for array of length 1000000
> max_product_fast: 0.14953112602233887 for array of length 1000000
> max_product: 2.9009320735931396 for array of length 10000000
> max_product_fast: 1.554677963256836 for array of length 10000000

### Edge Case Handling
See tests/max_product_test.py for a full spec.

In summary:
* Passing `None` as an argument or passing an empty list or tuple will return `None`
* Passing a list or tuple with length less than 3 will return the product of the integers given
* Passing an argument that is not a list or tuple will raise a `TypeError`
* Passing a list or tuple of floats will not raise any errors and will work in the same way as integers
* Integers in the input array may be positive, negative, or zero