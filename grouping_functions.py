from hidden_info import *
from math import floor, ceil

# [[H, P], [H, P], ...]
def singular_grouping(hosts=hosts_hidden, participants=participants_hidden):
    grouping=[]
    min_participants_per_host=floor(participants/hosts)
    for i in range(hosts):
        grouping.append([1, min_participants_per_host])

    remaining_participants=participants-min_participants_per_host*hosts
    for i in range(remaining_participants):
        grouping[i][1]+=1

    return grouping
