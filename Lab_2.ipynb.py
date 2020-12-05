a = int(input("enter number of pages: "))
b = int(input("please choose sheets: 16,24 or 32:  "))
pages = []
pages2 = []
page2 = 1
myorder = []
page22 = 2
b2 = b - 1
def function1():
    print("кількість листів", a/b)
    print("зошити:", b)


function1()

while True:
    try:
        if b == 24 and a != 1280 or b == 16 or b == 32:
            if a % b == 0:
                for x in range(0,int((b/2)-1)):
                    #1 list
                    print("лист #", x+1)
                    pages.append(b)
                    pages.append(page2)
                    b = b-2
                    page2 = page2 + 2
                    print(pages)
                    pages.clear()
                    #list 2
                    pages2.append(page22)
                    pages2.append(b2)
                    b2 = b2 - 2
                    page22 = page22 + 2
                    print(pages2)
                    pages2.clear()
            else:
                print("кількість сторінок повинна бути кратною кількістю сторінок у зошиті")

        else:
            print("error")
        break
    except ValueError:
        print("value error")
