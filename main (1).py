def numToWords(n):
    ones=["","one","two","three","four","five","six","seven","eight","nine"]
    teens=["","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens=["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    if n==1000:
        return "onethousand"
    words=""
    hundredsDigit=n//100
    tensDigit=(n%100)//10
    onesDigit=n%10
    if hundredsDigit>0:
        words+=ones[hundredsDigit]+"hundred"
        if tensDigit>0 or onesDigit>0:
            words+="and"
    if tensDigit==1 and onesDigit>0:
        words+=teens[onesDigit]
    else:
        words+=tens[tensDigit]
        words+=ones[onesDigit]
    return words
def letInNumbers():
    totalLetters=0
    for i in range(1,1001):
        words=numToWords(i)
        totalLetters+=len(words)
    return totalLetters 
if __name__=="__main__":
    totalLetters=letInNumbers()
    print("total numbers from 1 to 1000:",totalLetters)
