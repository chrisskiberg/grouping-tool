from hidden_info import *
from grouping_functions import *

from math import floor, ceil

hosts=hosts_hidden
participants=participants_hidden

max_people_per_group=8
min_people_per_group=3

participants_per_host=participants/hosts

groups=[]


# Groups with only one host, when there are many participants per host 
# More hosts than one might make the group too big
if (3<participants_per_host):
    groups.append(singular_grouping(hosts, participants))
