def main():
    words = str(input("Input a word or sentence:")).split()
    for word in words:
        print(word[1:] + word[0] + "ay", end = " ")
    print ()

main()
