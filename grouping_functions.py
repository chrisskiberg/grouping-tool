from hidden_info import *
from accepted_groups import *

from math import floor, ceil
import pandas as pd
import itertools

accepted_num_hosts_per_group = [1, 2, 3]
accepted_num_parts_per_group = [2, 3, 4, 5, 6]

def singular_grouping(hosts=hosts_hidden, participants=participants_hidden):
    grouping=[]
    min_participants_per_host=floor(participants/hosts)
    for i in range(hosts):
        grouping.append([1, min_participants_per_host])

    remaining_participants=participants-min_participants_per_host*hosts
    for i in range(remaining_participants):
        grouping[i][1]+=1

    return grouping

def medium_size_grouping(hosts=hosts_hidden, participants=participants_hidden):
    grouping_combs_HP={}

    for a in range(2,6):
        # combs = list(itertools.product({130, 140, 221, 230, 240, 251, 262, 343, 352}, repeat=a))
        combs = list(itertools.product({121, 130, 140, 221, 230, 240, 251, 262, 343, 352}, repeat=a))
        combs_sorted=[tuple (sorted (x)) for x in combs]
        combs = list(set(combs_sorted))
        for i in range(len(combs)):
            grouping_combs_HP_i=[]
            priority_i=0
            host_sum_i=0
            parts_sum_i=0
            for j in range(len(combs[i])):
                priority_i-=int(str(combs[i][j])[2])
                grouping_combs_HP_i.append([int(str(combs[i][j])[0]), int(str(combs[i][j])[1])])
                host_sum_i+=int(str(combs[i][j])[0])
                parts_sum_i+=int(str(combs[i][j])[1])
            grouping_combs_HP_i.insert(0, priority_i)
            grouping_combs_HP_i.insert(1, host_sum_i)
            grouping_combs_HP_i.insert(2, parts_sum_i)
            grouping_combs_HP_i.insert(3, len(combs[i]))

            if (host_sum_i in grouping_combs_HP and parts_sum_i in grouping_combs_HP[host_sum_i]):
                grouping_combs_HP[host_sum_i][parts_sum_i].append(grouping_combs_HP_i)
            elif (host_sum_i in grouping_combs_HP):
                grouping_combs_HP[host_sum_i][parts_sum_i]=[grouping_combs_HP_i]
            else:
                grouping_combs_HP[host_sum_i]={}
                grouping_combs_HP[host_sum_i][parts_sum_i]=[grouping_combs_HP_i]

    for hosts_key in grouping_combs_HP:
        for parts_key in grouping_combs_HP[hosts_key]:
            grouping_combs_HP[hosts_key][parts_key].sort(key = lambda x: x[0], reverse=True)

    return grouping_combs_HP


def save_medium_size_grouping(groups):
    groups_df=pd.DataFrame.from_dict({(i,j): groups[i][j] 
                           for i in groups.keys() 
                           for j in groups[i].keys()},
                       orient='index')

    file = open("groups_combinations.csv", "w")

    for row in groups_df.index:
        file.write("g")
        file.write(str(row[0]))    
        file.write("_")    
        file.write(str(row[1]))  
        file.write(": [")  
        file.write(str(groups_df[0][row]))
        file.write(", ")
        file.write(str(groups_df[1][row]))
        file.write(", ")
        file.write(str(groups_df[2][row]))
        file.write("], ")
        file.write("\n")

    file.close()
    print("hei")


def count_up_groups(hosts=hosts_hidden, participants=participants_hidden):
    groups_all=[]
    for groups_i in range(1, hosts+1):

        grouping=[]
        min_participants_per_group_i=floor(participants/groups_i)
        for i in range(groups_i):
            grouping.append([1, 1])

        remaining_hosts=hosts-groups_i
        for i in range(remaining_hosts):
            grouping[i%groups_i][0]+=1

        remaining_participants=participants-groups_i
        for i in range(remaining_participants):
                min_participants_per_host_j=0
                min_participants_per_host=participants/hosts
                for j in range(len(grouping)):
                    if (grouping[j][1]/grouping[j][0]<min_participants_per_host):
                        min_participants_per_host=grouping[j][1]/grouping[j][0]
                        min_participants_per_host_j=j
                # Større grupper kan ha mindre gjennomsnitt - om likt gi til den med mist
                grouping[min_participants_per_host_j][1]+=1


        priority_i=0
        for i in range(len(grouping)):
            if (grouping[i][0] in range(1,5) and grouping[i][1] in range(1,8)):
                priority_i-=accepted_groups[grouping[i][0]-1][grouping[i][1]][1]
            else:
                priority_i-=100

        grouping.insert(0, priority_i)
        grouping.insert(1, hosts)
        grouping.insert(2, participants)
        grouping.insert(3, groups_i)

        groups_all.append(grouping)
    groups_all.sort(key = lambda x: x[0], reverse=True)


    return grouping

