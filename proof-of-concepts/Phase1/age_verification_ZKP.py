import random

#Here, we set up the math. We will use a prime number, denoted by "p", and a generator, denoted by "g".
p = 103
g = 2
 #The generator must be a primitive root modulo. This means that it must satisfy 3 conditions:

#1. When you keep multiplying g by itself (modulo p), it should eventually produce every possible number between 1 and p−1.

#2. It must be easy to calculate gx(modp), but hard to do the reverse (find x if you only know the result). This is the Discrete Logarithm Problem.

#3. It cannot be 0 or 1, because if g were 1, then 1x is always 1. The proof would be useless because the result never changes.

def age_verification_ZKP():
    #This variable here is the secret that we're trying to protect. For the purposes of this demonstration, it represents the user's age.
    #Let us say that the user's age is 23, and this information has been legally confirmed by a government issuer such as the DMV. 
    secret_age = 23

    #We know the legal requirement to access an online service according to these laws is 18, so we'll put that down as a variable.

    legal_requirement = 18

    #If ZKPs were implemented in every operating system, the DMV or a similar government agency would have to "sign" the user's age by giving them a public identity 'y' based on their secret age.

    #Below is the public value, which is what any apps or services asking for the user's age will see:

    public_y = pow(g, secret_age, p) 
    
    #The math that was conducted above is something known as Modular Exponentiation and Python has built in functions to take care of it for us.
    #Here we print a few lines of text to just get an understanding of what the goal of the ZKP is.
    
    print(f"DMV Record: User's Public ID (y) is: {public_y}")
    print(f"Goal: Prove that the user is >= {legal_requirement} without revealing {secret_age} \n")

    #Now it's time to carry out the proof.
    #To do so, the user needs to prove that they know some secret 'x' such that x = legal_requirement + some_positive_remainder.

    remainder = (secret_age - legal_requirement) % p 

    #You may notice that we wrapped the remainder around modulo p. That is due to the nature of modulo arithmetic; modular math does not really have a concept of negative numbers because the remainder loops around to a large number that is closer to the prime 'p'. 
    #This means that if the secret_age = 17, and 17 - 18 = -1, modular math makes it look like 102. This could allow a minor to cheat the system.

    #So, we wrap the remainder around modulo p so that when we perform the logic check later, the system identifies this as an invalid (negative) age gap. 

    #Now the user commits to this 'remainder' instead of their true age. This proves that they are at least the limit.

    k = random.randint(1, p - 2)

   #The variable above is some random number k. The variable below it, r, is a hint that gives clues about what k is without revealing it.

    r = pow(g, k, p)

    #The above lines are the deeply mathematical part of the ZKP. It uses modular exponentiation and Discrete Logarithms to calculate important numbers. This is what helps to ensure the verifier never knows more than what it needs to.

    #Now suppose a website questions the user, asking for their age. It issues a random challenge, c.

    c = random.randint(0, 1)

    #The user creates a response to this challenge using the remainder.
    #If the math works for the remainder, the user must be at or above the legal requirements.
    s = (k + c * remainder)

    #Now it's time to verify the user's age. It doesn't get checked directly. The check is simple: Is (Age - Limit) = Remainder?
    # Mathematically, this is: g^s == r * (y /g^requirement)^c
    #We perform this math with Python's functions to make it easier to comprehend the process.

    age_gap_public = (public_y * pow(pow(g, legal_requirement, p), -1, p)) % p

    #We'll now break down our system into two parts: a left side and a right side. This left side and right side act as a scale to balance each other out. 

    #The left side takes the secret (s) that we sent, and raises it to the power of g, the generator we chose at the start of the project.

    #The right side is a mathematical construction using the parts that were made public. It is the public value, raised to the power of the challenge (c) that the theoretical website sent, then mulitplied by the hint (r) that the user sent back. That whole result is then divided by p and we look at the remainder (mod p).

    #The right side is also the expectation. The website can say: If the user really knows the secret (secret_age) behind the public value(public_y), then the response (s) should perfectly bridge the gap between the hint (r) and the public identity (public_y)

    left_side = pow(g, s, p)
    right_side = (r * pow(age_gap_public, c, p)) % p

    #We also add a "reasonable range", which is 0-80 years above the limit to resolve the modular math problem mentioned earlier.

    max_range = 80


    #To recap, we print out the process here.
    print(f"Step 1: User sends commitment (r): {r}")
    print(f"Step 2: Verifier (the website) sends a challenge (c): {c}")
    print(f"Step 3: User sends response (s): {s}")
    print("Math Check: \n")

    if(left_side == right_side and remainder <= max_range):
        print("Verified! The user is 18 or older.")
        print(f"Note that the verifier (website) still does not know the user is {secret_age}.")
    elif left_side == right_side and remainder > max_range:
        print("Failed! The math passed, but the age is 'negative' (wrapped around p).")
        print("This is how a system could potentially catch someone trying to cheat with a younger age.")
    else:
        print("Failed. The math scale did not balance.")


age_verification_ZKP()
