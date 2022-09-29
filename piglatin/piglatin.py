def main():
    words = str(input("Input a word or sentence:")).split()
    for word in words:
        print(word[1:] + word[0] + "ay", end = " ")
    print ()

main()


def piglatinify(word):
    first=word[0]
    if first in 'aeiouAEIOU':
        result=word + 'ay'
    else:
        result=word[1:].capitalize()+first.lower()+'ay'
      else:
        result=word[1:]+first+'ay'
    return result
