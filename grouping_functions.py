from hidden_info import *
from accepted_groups import *
from math import floor, ceil

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
    possible_combination_hosts=[]
    possible_combination_parts=[]

    # combs = list(itertools.product({'a', 'b', 'c'}, repeat=10))
    # for in range() - a, aa, aaa, aaaa, aaaaa
    combs = list(itertools.product({130, 140, 221, 230, 240, 251, 262, 343, 352}, repeat=2))
    # print(combs)
    # combs_sorted=[sorted (x) for x in combs]
    combs_sorted=[tuple (sorted (x)) for x in combs]
    # print(combs_sorted)
    combs = list(set(combs_sorted))
    # print(combs)

    combs_HP=[]
    for i in range(len(combs)):
        combs_HP_i=[]
        priority_i=0
        host_sum_i=0
        parts_sum_i=0
        for j in range(len(combs[i])):
            priority_i-=int(str(combs[i][j])[2])
            combs_HP_i.append([int(str(combs[i][j])[0]), int(str(combs[i][j])[1])])
        combs_HP_i.insert(0, priority_i)
        combs_HP.append(combs_HP_i)
        # print(priority_i, combs_HP_i)
        print(combs_HP)




    # accepted_1_groups = [[1,3], [1,4]]
    # accepted_2_groups = [[2,2], [2,3], [2,4], [2,5], [2,6]]
    # accepted_3_groups = [[3,4], [3,5]]


    # shortest_pos_comb=0
    # longest_pos_comb=0
    
    # # Find all the combinations of numbers that add up to the target sum
    # for i in range(1, hosts):
    #     for combination in itertools.combinations_with_replacement(accepted_num_hosts_per_group, i):
    #         if sum(combination) == hosts:
    #             if (shortest_pos_comb==0 or len(combination)<shortest_pos_comb):
    #                 shortest_pos_comb=len(combination)
    #             if (longest_pos_comb==0 or longest_pos_comb<len(combination)): 
    #                 longest_pos_comb=len(combination)
    #             possible_combination_hosts.append(list(combination))
    # print(possible_combination_hosts)

    # for i in range(shortest_pos_comb, longest_pos_comb+1):
    #     for combination in itertools.combinations_with_replacement(accepted_num_parts_per_group, i):
    #         if sum(combination) == participants:
    #             possible_combination_parts.append(list(combination))
    #             #  problem - Nå er det bare en måte å arrangere de på, men for å matche må arrangere på flere måter
    #             # Kan prøve å finne riktig element, gi til noen og pope til noen elementer, hvis ingen matcher da er det ikke mulig
    #                 # Men en mengde participants kan matche med flere hosts  
    # print(possible_combination_parts)    
    # print("h3i")

    # for i in range(len(possible_combination_hosts)):
    #     for j in range(len(possible_combination_parts)):
    #         if (len(possible_combination_hosts[i])==len(possible_combination_parts[j])):
    #             possible_parts=[[] for i in range(len(possible_combination_hosts[i]))]
    #             for l in range(len(possible_combination_hosts[i])):
    #                 if (possible_combination_hosts[i][l]==1):
    #                     common = [x for x in possible_combination_parts[j] if x in accepted_1_host_parts]
    #                     print(possible_combination_hosts[i][l], common)
    #                 elif (possible_combination_hosts[i][l]==2):
    #                     common = [x for x in possible_combination_parts[j] if x in accepted_2_host_parts]
    #                     print(possible_combination_hosts[i][l], common)
    #                 elif (possible_combination_hosts[i][l]==3):
    #                     common = [x for x in possible_combination_parts[j] if x in accepted_3_host_parts]
    #                     print(possible_combination_hosts[i][l], common)
    #                 if (len(common)==0):
    #                     break
    #             print(possible_combination_hosts[i])
    #             print(possible_combination_parts[j])
    #             # print(possible_parts)

    #         # Sjekke om possible combinations har alle tallene
    #         elif (len(possible_combination_hosts[i])<len(possible_combination_parts[j])): 
    #             break


    # all_possible_combinations=[]
    # for i in range(len(possible_combination)):
    #     possible_combination_parts_i=[]
    #     for j in range(len(possible_combination[i])):
    #         if (possible_combination[i][j]==1):
    #             possible_combination_parts_i.append([3,4])
    #         elif (possible_combination[i][j]==2):
    #             possible_combination_parts_i.append([2,3,4,5,6])
    #         elif (possible_combination[i][j]==3):
    #             possible_combination_parts_i.append([4,5])
    #     all_possible_combinations.append(possible_combination_parts_i)
    #     print("hei")


    # pot_max_grouping_with_sing_3s=0
    # # Gi enkeltfolk 3, holde følge med gjennomsnittet til enkeltfolk - Gjennomsnittet bør være minst 1.5
    # for i in range(1, hosts):
    #     print(participants-3*i)
    #     print(hosts-i)
    #     remaining_participants_per_host=(participants-3*i)/(hosts-i)
    #     if (remaining_participants_per_host<1  or (hosts-i)<=1 and (participants-3*i)<=2):
    #         break
    #     else:
    #         pot_max_grouping_with_sing_3s=i

    # if (pot_max_grouping_with_sing_3s!=0):

    #     max_host_after_3=ceil((hosts-j)/2)


    #     # for j in range(1, pot_max_grouping_with_sing_3s):
    #     #     grouping_with_sing_3s=[[1,3] for i in range(j)]
    #     #     # print(grouping_with_sing_3s)

    #     #     max_host_after_3=ceil((hosts-j)/2)
    #     #     # telle nedover alle starter på største og teller ned
    #     #     for i in range(max_host_after_3):
    #     #         grouping_with_sing_3s.append([3,5])
    #     #     print(grouping_with_sing_3s)
    #     #     while (sum([sublist[0] for sublist in grouping_with_sing_3s])>hosts):
    #     #         if (grouping_with_sing_3s[-1][0]==3):
    #     #             grouping_with_sing_3s[-1]=[2,6]
    #     #         elif (grouping_with_sing_3s[-1][0]==2):
    #     #             grouping_with_sing_3s.pop()
    #     #         else:
    #     #             print("break")
    #     #             break
    #     #     print(hosts)
    #     #     print(grouping_with_sing_3s)

    #         # if (sum([sublist[0] for sublist in grouping_with_sing_3s]==hosts)):
    #         #     break    


    # pot_max_grouping_with_sing_4s=0
    # # Gi enkeltfolk 3, holde følge med gjennomsnittet til enkeltfolk - Gjennomsnittet bør være minst 1.5
    # for i in range(1, hosts):
    #     # print(participants-4*i)
    #     # print(hosts-i)
    #     remaining_participants_per_host=(participants-4*i)/(hosts-i)
    #     if (remaining_participants_per_host<1 or (hosts-i)==1 and (participants-3*i)<=2):
    #         break
    #     else:
    #         pot_max_grouping_with_sing_4s=i

    # # print(pot_max_grouping_with_sing_3s)
    # # print(pot_max_grouping_with_sing_4s)


    # # Deretter gå igjennom og prøv liste med aksepterte grupper

    # # Bare prøve liste med aksepterte gruppper  

    return grouping

def small_size_grouping(hosts=hosts_hidden, participants=participants_hidden):
    grouping=[]

    return grouping


