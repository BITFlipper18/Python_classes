# 1. Toon hoeveel 3 maal 4 is. 
# print(3*4)

# # 2. Controleer of 4.6 kleiner is of gelijk aan 5

# # 3. Vraag de gebruiker om zijn leeftijd, geef weer als hij ouder is dan 18 jaar.
# age = int(input("What is your age?: "))
# if age > 18:
#     print("You are above 18 years old")
# else:
#     pass

# # 4. Maak een programma dat van een getal weergeeft even of oneven. Geef een boolean terug.
# number = int(input("Please enter a number: "))
# if number%2 == 0:
#     number = True
# else:
#     number = False
# print(f"Is the given number an even number? {number}")

# # 5. Vraag de gebruiker zijn naam en nadien zijn leeftijd, druk dan af binnen hoeveel jaar hij op pensioen mag gaan (leeftijd 67)

# name = input("Please enter your name: ")
# age = int(input("Please enter your age: "))
# retirement_age = 67

# if age < retirement_age:
#     print(f"Hi {name}, you can retire in {retirement_age - age} years")
# elif age == retirement_age:
#     print(f"Congratulations {name}, you have hit the age to retire!")
# elif age > retirement_age:
#     print(f"Uhm, {name}? I suppose you are aware that you have been retiref for {age - retirement_age} years?!?!")

# 6. Vraag de gebruiker om een getal tussen 1 en 100 en geef weer als dit een even of oneven getal is

# number = int(input("Please enter a number between 1 and 100: "))
# while number > 100 and number < 1:
#     print("Be sure to enter a number between 1 and 100: ")

# number = 0
# def range_number():
#     if number >= 1 and number <= 100:
#         print("The number is in the range 1 and 100")

# if number >= 1 and number <= 100:
#     print("The number is in the range 1 and 100")
# elif range_number():

# 7. Vraag de gebruiker om een cijfer tussen 1 en 20 en geef een puntenquotering weer waar kleiner dan 5 = F, tussen 5 en 9 = E, tussen 9 en 12 = D, tussen 12 en 15 = C, tussen 15 en 18 = B, tussen 18 en 20 = A
# 8. Vraag de gebruiker om een getal tussen 1 en 10 in te geven. Druk dan alle voorafgaande nummers af.
# 9. Vraag de gebruiker om een getal tussen 1 en 60 in te geven. Druk alle cijfers af die je kan delen door 9. 
# 10. Vraag de gebruiker om een tekst in te geven. Tel het aantal letters en cijfers en druk deze dan af 
# 11. De prijs van een limonade is € 3. Vraag de gebruiker hoeveel limonades hij koopt. Toon daarna hoeveel hij in totaal moet betalen. Als hij meer dan 10 limonades koopt, krijgt hij 5 % korting.
#     Voorbeeld 1: hij koopt 4 limonades, hij betaalt € 12.
#     Voorbeeld 2: hij koopt 15 limonades, hij betaalt € 42.75 (15 x 3 en daarop 5 % korting)
# 12. De prijs van een limonade is € 3. De gebruiker typt hoeveel limonades hij koopt. Zolang hij een getal typt dat kleiner is of gelijk aan 0, moet hij dit getal opnieuw typen. Toon daarna hoeveel hij in totaal moet betalen.
# 13. De gebruiker typt een getal. Toon de tafel van vermenigvuldiging van dit getal: 1 x dit getal, 2 x dit getal, ... 10 x dit getal.
# 14. Vraag aan de gebruiker of hij werk heeft.
#     Als hij ja antwoordt toon je : "Veel werkplezier".
#     Anders vraag je of hij een opleiding wil volgen.
#     Als hij ja antwoordt, toon je : "Je vindt opleidingen op www.syntra-ab.be".
#     Anders toon je : "Je vindt vacatures op www.vdab.be/jobs".

work_status = input("Do you have work? (YES/NO): ")

if work_status == "YES":
    print("Have fun at work!")
elif work_status == "NO":
    course_status = input("Do you want to follow a course? (YES/NO): ")
    if course_status == "YES":
        print("You can find courses at www.syntra-ab.be!")
    elif course_status == "NO":
        print("You can find vacancies at www.vdab.be/jobs!")

