from hidden_info import *
from accepted_groups import accepted_groups
from math import floor, ceil

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


    pot_max_grouping_with_sing_3s=0
    # Gi enkeltfolk 3, holde følge med gjennomsnittet til enkeltfolk - Gjennomsnittet bør være minst 1.5
    for i in range(1, hosts):
        print(participants-3*i)
        print(hosts-i)
        remaining_participants_per_host=(participants-3*i)/(hosts-i)
        if (remaining_participants_per_host<1  or (hosts-i)==1 and (participants-3*i)<=2):
            break
        else:
            pot_max_grouping_with_sing_3s=i

    if (pot_max_grouping_with_sing_3s!=0):
        for j in range(1, pot_max_grouping_with_sing_3s):
            grouping_with_sing_3s=[[1,3] for i in range(j)]
            # print(grouping_with_sing_3s)

            max_host_after_3=ceil((hosts-j)/2)
            # telle nedover alle starter på største og teller ned
            grouping_with_sing_3s.append([[3,5] for i in range(max_host_after_3)])
            print(grouping_with_sing_3s)
            while (sum([sublist[0] for sublist in grouping_with_sing_3s]>hosts):
                if (grouping_with_sing_3s[-1][0]==3):
                    grouping_with_sing_3s[-1]=[2,6]
                else:
                    grouping_with_sing_3s.pop()

            # if (sum([sublist[0] for sublist in grouping_with_sing_3s]==hosts)):
            #     break    


    pot_max_grouping_with_sing_4s=0
    # Gi enkeltfolk 3, holde følge med gjennomsnittet til enkeltfolk - Gjennomsnittet bør være minst 1.5
    for i in range(1, hosts):
        # print(participants-4*i)
        # print(hosts-i)
        remaining_participants_per_host=(participants-4*i)/(hosts-i)
        if (remaining_participants_per_host<1 or (hosts-i)==1 and (participants-3*i)<=2):
            break
        else:
            pot_max_grouping_with_sing_4s=i

    # print(pot_max_grouping_with_sing_3s)
    # print(pot_max_grouping_with_sing_4s)


    # Deretter gå igjennom og prøv liste med aksepterte grupper

    # Bare prøve liste med aksepterte gruppper  

    return grouping

def small_size_grouping(hosts=hosts_hidden, participants=participants_hidden):
    grouping=[]

    return grouping
