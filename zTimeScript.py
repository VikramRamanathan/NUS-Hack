import datetime
def timestuff(time):
    time = time[:-6]
    d1 = str(datetime.datetime.now())
    d1 = d1 [11:][:-10]
    d2 = str(datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S"))[11:][:-3]
    curmin = int(d1[3:])
    curh = int(d1[:-3])
    duemin = int(d2[3:])
    dueh = int(d2[:-3])
    curmin = curmin + curh * 60
    duemin = duemin + dueh * 60
    diff = duemin - curmin
    return diff