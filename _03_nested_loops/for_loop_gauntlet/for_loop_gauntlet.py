"""
Create algorithms and use to solve
https://central.jointheleague.org/levels/Level0/Recipes/ForLoopGauntlet.html
"""


if __name__ == '__main__':
    # for i in range(101):
    #     print(i)
    #
    # for i in range(100, -1, -1):
    #     print(i)
    # for i in range(0, 102, 2):
    #     print(i)
    # for i in range(1, 100, 2):
    #     print(i)
    # for i in range(1, 501):
    #     beans = i % 2
    #     if beans == 0:
    #         print(str(i)+" is even")
    #     else:
    # #         print(str(i)+" is odd")
    # for i in range(0, 778, 7):
    #     print(i)
    # banana = 0
    # for i in range(1558, 2024+1):
    #     print("in "+str(i)+" i was "+str(banana))
    #     banana = banana + 1

    # for i in range(3):
    #     for j in range(3):
    #         print (i, j)

    # for i in range(1, 7+1, 3):
    #     for j in range(i, i+3):
    #         print(j, end=" ")
    #     print()
    for i in range(1, 100+1, 10):
        for j in range(i, i+10):
            print(j, end=" ")
        print()

    pass
