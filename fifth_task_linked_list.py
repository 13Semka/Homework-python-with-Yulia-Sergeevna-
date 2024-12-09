def getIntersectionNode(headA, headB):
    list1 = headA
    list2 = headB
                                # если кратко, то проходим по двум связанным спискам, пока они не будут равны (null = null тоже равенство),
                                # и так получается что когда то они стопроц будут равны это мы возвращаем в ретёрне
    while list1 != list2:   
        if list1:                   # пока headA не равно null мы идем дальше, одновременно с headB, если заканчивается, то мы начинаем
            list1 = list1.next      # идти по headB, в конце концов они встретятся, доказывается это легко,
        else:                       # т.к. len(a) + len(b) = len(b) + len(a)
            list1 = headB

        if list2:                   # тоже самое что и сверху толька для второго списка
            list2 = list2.next
        else:
            list2 = headA
                
    return list1                    # возвращаем че попало, потому что нам все равно лялялялялял
            


        