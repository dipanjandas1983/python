def calculate_love_score(name1, name2):

    combine_names = (name1 + name2).lower()

    # Count of letter TRUE

    t = combine_names.count("t")
    r = combine_names.count("r")
    u = combine_names.count("u")
    e = combine_names.count("e")

    true_score = t + r + u + e

    # Count of letter LOVE 

    l = combine_names.count("l")
    o = combine_names.count("o")
    v = combine_names.count("v")
    e = combine_names.count("e")

    love_score = l + o + v + e

    score = int(str(true_score) + str(love_score))

    print(score)

calculate_love_score(name1="Kanye West", name2="Kim Kardashian")
calculate_love_score(name1="Angela Yu", name2="Jack Bauer")





    