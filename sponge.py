def sponge_case(sentence):

    # empty string list
    # loop through the input:sentence
    # check each character of the input with the method isAlpha():
    # true: implement the main method: one smaller case, one capital
            # if current position is odd: make the character lower case
            # If current position is even: make the character uppper case
            # add the current character into my String List
    # false: ignore the current character

    # brute force:
    # use another loop to loop through my result list and add all the characters altogether


    # return String list as my result


    # Handle spaces instead of only checking if it's alpha()
    # space messed up with my position counting
    result = []
    count = 0
    for index in range(len(sentence)):
        current_character = sentence[index]
        count += 1

        if count % 2 == 0 and current_character.isalpha(): # even position
            result.append(current_character.upper())
        elif count % 2 != 0 and current_character.isalpha(): # odd
            result.append(current_character.lower())
        elif current_character == " ":
            result.append(" ")

    print("".join(result))

    return "".join(result)






# Test cases
assert sponge_case("spongebob") == "sPoNgEbOb"
assert sponge_case("Who are YOU calling A Pinhead") == "wHo aRe yOu cAlLiNg a pInHeAd"
#assert sponge_case("WHAT is UP my dude") == "wHaT iS uP mY dUdE"
assert sponge_case("E") == "e"
assert sponge_case("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")