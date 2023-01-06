print("Who is the first president of Ghana?")
answer = "KWAME NKRUMAH"
guess_count= 0
guess_limit= 3
while guess_count<guess_limit:
    response = input("Enter response: ")
    response1 = response.upper()
    guess_count +=1
    if response1== answer:
        print("You are right, you won!")
        break
else:
    print("You lose")



