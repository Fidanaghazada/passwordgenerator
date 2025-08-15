print("Düşün bir rəqəm 1 ilə 100 arasında")
print("Cavab variantları: 'l' (aşağı), 'h' (yuxarı), 'DÜZ' (tapdın)")

l = 1
h = 100
guesses = 0

while True:
    if l > h:
        print("Bu mümkün deyil. Yəqin ki, cavablarda səhv etdin.")
        break

    guess = (l + h) // 2
    guesses += 1

    if guess > 100:
        guess = 100
    elif guess < 1:
        guess = 1

    print(f"Təxminim: {guess}")
    ans = input("Cavab ver: ").strip().lower()

    if ans == "l":  # Mənim təxminim çox böyükdür → yuxarı həddi endir
        h = guess - 1
    elif ans == "h":  # Mənim təxminim çox kiçikdir → aşağı həddi qaldır
        l = guess + 1
    elif ans == "DÜZ" or ans == "düz" or ans=="duz":  # Mənim təxminim düzgündür
        print(f" Mən {guesses} cəhdə tapdım!")
        break
    else:
        print("Düzgün cavab yaz: 'l', 'h', ya da 'DÜZ'")

