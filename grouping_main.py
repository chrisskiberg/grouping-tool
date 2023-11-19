from hidden_info import *
from grouping_functions import *

from math import floor, ceil


hosts=hosts_hidden
participants=participants_hidden

max_people_per_group=8
min_people_per_group=3

participants_per_host=participants/hosts

groups=[]

count_up_groups(hosts, participants)

# # Groups with only one host, when there are many participants per host 
# # More hosts than one might make the group too big
# if (3<participants_per_host):
#     groups.append(singular_grouping(hosts, participants))
#     # print(groups)
    
# # Groups with one host, when there are a medium number of participants per host 
# if (2<=participants_per_host and participants_per_host<=3):
#     groups.append(medium_size_grouping(hosts, participants))
#     # print(groups)

# if (1<=participants_per_host and participants_per_host<2):
#     groups.append(small_size_grouping(hosts, participants))
#     # print(groups)

# # if (participants_per_host<=1):
