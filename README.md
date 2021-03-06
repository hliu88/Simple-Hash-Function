# Simple Hash Function
 
This simple hash function is based on the sha1.py file in this repo that is based on the pseudocode of SHA1 design on Wikipedia. SHA1 has 2^160 possible values. It is a collision resistant algorithm. However, hash collision has been found for SHA1, and this project is to improve on the SHA1 design and make the hash generated from the algorithm more random and uniformly distributed.

The algorithm works by padding the messages and dividing the message into chunks. Each chunk is then processed through boolean algebra, and all chunks of words are being combined to form the final hash. Through dividing and operating boolean operations, it ensures that the algorithm is collision resistant, and it's origional value cannot be manipulated to form hash collisions.

To improve the SHA1 algorithm to avoid collisions without increasing the address space, we need to increase entrophy of the message. This includes shuffling of bits, compression, and LFSR. SHA1 has padding and compression function in place, thus its output is always 20 bytes. Thus, we'd like to implement shuffling of bits in the form of shift in bits, as well as LFSR(Linear feedback shift register). 

Sha_mod.py is an implementation of the options listed above. After the program first receives the message, it goes through the one sweep of a modified SHA1 algorithm first. The code is modified that all chunks of the messages are being manipulated to increase entrophy. This is done using LSFR as well as shifting. The string of binary values are shifted to the left once, and the right most value is being deteremined not by the left most value but with the relation of XOR between index 0 and index 2 of the origional binary value. The code is then being left shifted once. This process is repeated for 5 times. 

Once this is completed, we further increase the entrophy of the hash by splitting the hash in half, then leftshifting both sides, spliting once again, and combining two halfs of the two portions together one by XOR and the other by AND operation. The two halfs are finally being concatinated together and LSFR is performed again to yield the final hash value. 

## Tests
All tests are being ran in tests.py and setup in github actions to automatically deploy and run.
1. The recreated SHA1.py code was compared against hashlib.sha1 and after executing both functions they output the same values. 
2. The sha_mod.py code was tested to see if output is determinstic by hashing the same string twice and comparing the values.
3. Compression of sha_mod.py was tested to see if all inputs returns the same hash length. 
4. Distribution of the hashes is tested, 10000 hashes were generated by random strings of letters(upper&lower case) and numbers of random length to 10000. Distribution is indicated by the left most value, and results are uniform. 
<img width="675" alt="" src="https://user-images.githubusercontent.com/17788596/163659276-5129d846-603b-447b-9fe9-a654e53b012e.png">

Full test result below:

<img width="1250" alt="" src="https://user-images.githubusercontent.com/17788596/163659664-7ffb5695-89f6-4650-8449-4e030e5a44fb.png">


Tests above are setup on github on github actions, and can be seen by clicking the green checkmark on home page of the repo.
