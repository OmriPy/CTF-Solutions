# Solution for coin1
## Note
I executed the file `coin1.py` within pwnable.kr's server becuase my computer ran it faster inside the server than outside.
## Explanation
We need to find counterfeit coins within the range 0 to `N` - 1 using only `C` attempts.
When we find 100 counterfeit coins, we will get a reward which is of course the flag.

The way to find the fake coin within `C` attemps is by using Binary Search. So I used binary search in order to find 100 fake coins.

View `coin1.py` for the code.
