year = int(input("Entrez l année a verifier:\n"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("L'année est une année bissextile!")
else:
    print("L'année n'est pas une année bissextile!")