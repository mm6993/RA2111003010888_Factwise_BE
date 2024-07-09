def number_to_words(n):
    ones=["","one","two","three","four","five","six","seven","eight","nine"]
    teens=["","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens=["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    if n==1000:
        return "onethousand"
    words=""
    hundreds_digit=n//100
    tens_digit=(n%100)//10
    ones_digit=n%10
    if hundreds_digit>0:
        words+=ones[hundreds_digit]+"hundred"
        if tens_digit>0 or ones_digit>0:
            words+="and"
    if tens_digit==1 and ones_digit>0:
        words+=teens[ones_digit]
    else:
        words+=tens[tens_digit]
        words+=ones[ones_digit]
    return words
def count_letters_in_numbers():
    total_letters=0
    for i in range(1,1001):
        words=number_to_words(i)
        total_letters+=len(words)
    return total_letters 
if __name__=="__main__":
    total_letters=count_letters_in_numbers()
    print("Total letters used from 1 to 1000(inclusive):",total_letters)