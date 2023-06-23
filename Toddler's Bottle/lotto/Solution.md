# Solution for lotto
Because the code uses randomization by opening the file `/dev/urandom`, there could be a lot of possibilities.

The code

```
for(i=0; i<6; i++){

    lotto[i] = (lotto[i] % 45) + 1;

}
```

simply tells us that each byte is within the range 1-45 (included) in decimal.
The key to finding the flag is brute-forcing the 6 correct bytes.

Just as I wrote in my code, you nest 6 for loops that every one of them iterates between 1 to 45, because there could be 45^6 possiblities.

Make sure you run the code within the ssh.
