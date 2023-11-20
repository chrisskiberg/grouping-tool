from hidden_info import *
from accepted_groups import *

from math import floor, ceil
import pandas as pd
import itertools

accepted_num_hosts_per_group = [1, 2, 3]
accepted_num_parts_per_group = [2, 3, 4, 5, 6]



# [[H, P], [H, P], ...]
def singular_grouping(hosts=hosts_hidden, participants=participants_hidden):
    grouping=[]
    min_participants_per_host=floor(participants/hosts)
    for i in range(hosts):
        grouping.append([1, min_participants_per_host])
    # print(grouping)

    remaining_participants=participants-min_participants_per_host*hosts
    for i in range(remaining_participants):
        grouping[i][1]+=1

    # print(grouping)
    return grouping

def medium_size_grouping(hosts=hosts_hidden, participants=participants_hidden):
    grouping=[]

    # combs = list(itertools.product({'a', 'b', 'c'}, repeat=10))
    # for in range() - a, aa, aaa, aaaa, aaaaa
    # print(combs)
    # combs_sorted=[sorted (x) for x in combs]
    # print(combs_sorted)
    # print(combs)
    
    combs_HP={}

    for a in range(2,6):
        # combs = list(itertools.product({130, 140, 221, 230, 240, 251, 262, 343, 352}, repeat=a))
        combs = list(itertools.product({121, 130, 140, 221, 230, 240, 251, 262, 343, 352}, repeat=a))
        combs_sorted=[tuple (sorted (x)) for x in combs]
        combs = list(set(combs_sorted))
        # print(combs)
        print("")
        for i in range(len(combs)):
            combs_HP_i=[]
            priority_i=0
            host_sum_i=0
            parts_sum_i=0
            for j in range(len(combs[i])):
                priority_i-=int(str(combs[i][j])[2])
                combs_HP_i.append([int(str(combs[i][j])[0]), int(str(combs[i][j])[1])])
                host_sum_i+=int(str(combs[i][j])[0])
                parts_sum_i+=int(str(combs[i][j])[1])
            combs_HP_i.insert(0, priority_i)
            combs_HP_i.insert(1, host_sum_i)
            combs_HP_i.insert(2, parts_sum_i)
            combs_HP_i.insert(3, len(combs[i]))

            if (host_sum_i in combs_HP and parts_sum_i in combs_HP[host_sum_i]):
                combs_HP[host_sum_i][parts_sum_i].append(combs_HP_i)
            elif (host_sum_i in combs_HP):
                combs_HP[host_sum_i][parts_sum_i]=[combs_HP_i]
            else:
                combs_HP[host_sum_i]={}
                combs_HP[host_sum_i][parts_sum_i]=[combs_HP_i]


    for hosts_key in combs_HP:
        for parts_key in combs_HP[hosts_key]:
            combs_HP[hosts_key][parts_key].sort(key = lambda x: x[0], reverse=True)
    # print(combs_HP)

    # print(combs_HP[hosts_hidden][participants_hidden])
    return combs_HP


def save_medium_size_grouping(groups):
    groups_df=pd.DataFrame.from_dict({(i,j): groups[i][j] 
                           for i in groups.keys() 
                           for j in groups[i].keys()},
                       orient='index')
    groups_df=groups_df.iloc[:, 0:4]
    # print(groups_df.iloc[:, 0])
    print(groups_df.head())

    file = open("groups_combinations.csv", "w")

    # iterating the columns
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


        # print(row[0], end = "_")    
        # print(row[1], end = ": [")  
        # print(groups_df[0][row], end=", ")
        # print(groups_df[1][row], end=", ")
        # print(groups_df[2][row], end="], ")
        # print("")
    file.close()

        # print(groups_df.iloc[row, 1], end = ",")
        # print(groups_df.iloc[row, 2]end = "] \n")
 

    # groups_df.to_csv('groups_combinations.csv')
    # Kan hende at dette er en krevende CSV. Kanskje heller burde gjøre det på min måte
    # Bare velge topp 4
    # Eller bare ha alle kombinasjonene i en JS variabel 













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
                # Større grupper kan ha mindre gjennomsnitt
                grouping[min_participants_per_host_j][1]+=1

        print(grouping) 

        priority_i=0
        for i in range(len(grouping)):
            # if not in accepted group :
                # discard
            if (grouping[i][0] in range(1,5) and grouping[i][1] in range(1,8)):
                # print(accepted_groups[grouping[i][0]-1])
                # print(accepted_groups[grouping[i][0]-1][grouping[i][1]])
                # print(accepted_groups[grouping[i][0]-1][grouping[i][1]][1])
                priority_i-=accepted_groups[grouping[i][0]-1][grouping[i][1]][1]
                # print(accepted_groups[grouping[i][0]][grouping[i][1]])
            else:
                priority_i-=100
        print(priority_i)
        print("")

        grouping.insert(0, priority_i)
        grouping.insert(1, hosts)
        grouping.insert(2, participants)
        grouping.insert(3, groups_i)

        groups_all.append(grouping)
    # print(groups_all)
    groups_all.sort(key = lambda x: x[0], reverse=True)
    # print(groups_all)

    if (len(groups_all)<3):
        for i in range(len(groups_all)):
            print(groups_all[i])
    else: 
        for i in range(3):
            print(groups_all[i])

    return grouping

