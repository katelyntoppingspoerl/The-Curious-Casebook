print("THE CURIOUS CASEBOOK")
print("Case 01: The Missing Photograph")
print()
print("A photograph of the Lantern Parade vanished from the exhibit.")
print("The curator found its original caption: 'Lantern Parade, October 1974.'")
print("The catalog may have the wrong title, but the year and event should match.")
print()

records = [
    "Box 12 | Lantern Parade | 1984 | Marchers carry lanterns down Main Street.",
    "Box 27 | Evening Procession | 1974 | Marchers carry lanterns down Main Street.",
    "Box 34 | Founders' Picnic | 1974 | Families gather in Riverside Park.",
]

print("CATALOG RECORDS")
for record in records:
    print(record)

print()
while True:
    guess = input("Which box holds the photo? Enter 12, 27, 34, or Q to quit: ")
    guess = guess.strip().lower()

    if guess == "27":
        print("Case solved! The year and the lanterns match. The title was cataloged differently.")
        break
    elif guess == "q":
        print("Case closed for now.")
        break
    elif guess in ("12", "34"):
        print("That box matches only part of the clue. Look for both the year and the lanterns.")
    else:
        print("Enter one of the three box numbers from the catalog, or Q to quit.")