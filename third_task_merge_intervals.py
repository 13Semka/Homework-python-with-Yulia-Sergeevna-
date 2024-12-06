def merge(intervals):
        intervals.sort()                            # cортируем интервалы, чтобы было удобнее их мержить

        merged_list = [intervals[0]]                # добавляем первый интервал в список уже совмещенных
        for i in intervals:                         
            if merged_list[-1][1] < i[0]:           # если конец последнего в списке интервала меньше чем начало текущего интервала,
                merged_list.append(i)               # то все круто, они не оверлап и мы кайфуем
            else:                                   # а если нет, то берем максимальное из концов двух интервалов :)
                merged_list[-1][1] = max(merged_list[-1][1], i[1])  

        return merged_list