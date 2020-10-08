R = int(input("Please enter your score: "))
if 95 <= R <= 100:
    print("Excellent")
elif 85 <= R <= 94:
    print("Very good")
elif 75 <= R <= 84:
    print("Good")
elif 65 <= R <= 74:
    print("Satisfactory")
elif 60 <= R <= 64:
    print("Marginal")
elif 0 <= R <= 60:
    print("Unsatisfactory")
elif R < 0 or R > 100 :
    print("Error")