import random

option = int(input("choose task:\n"
                   "enter 1,2,3 or 4\n"
                   "task: "))
if option == 1:
    head = int(input("head: "))
    x = int(input("x: "))
    tails = random.sample(range(10, 30), 5)


    def cons(head, tails):
        list = []
        list.append(head)
        list.append(tails)
        print(list)

    cons(head, tails)


elif option == 2:
    begin = int(input("begin "))
    end = int(input("end "))
    step = int(input("step "))

    def rrange(begin,end,step):
        begin = int(input("begin "))
        end = int(input("end "))
        step = int(input("step "))
        list = []
        if (begin > end and step > 0) or (begin < end and step < 0):
            return print("list: ", list)
        else:
            for i in range(begin, end, step):
                list.append(i)
        print("list: ",list)

    rrange(begin,end,step)

elif option == 3:

    print()
elif option == 4:
    m = int(input("m: "))
    n = int(input("n: "))


    def A(m, n):

        if m == 0:
            return n + 1
        elif n == 0:
            return A(m - 1, 1)
        else:
            return A(m - 1, A(m, n - 1))
    print(A(m, n))