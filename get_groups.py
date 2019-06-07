import sys
from random import randint

class cell(object):
    def __init__(self,number_cell,count_pigs,size):
        self.num = number_cell
        self.count = count_pigs
        self.size = size

class group(cell):
    def __init__(self,index):
        # print("Created group")
        self.cells=[] #list of cells
        self.sum=0 #quantity of pigs in group
        self.index=index # number of group
    def add_cell(self,cell_object):
        self.cells.append(cell_object)
        self.sum+=cell_object.count
class groups(group):
    #self.groups_= []
    def __init__(self):
        print("Created groups")
        self.groups_ = []
    def add_group(self,group_object):
        self.groups_.append(group_object)
        print("Group number "+str(group_object.index)+"added with quantity: "+str(group_object.sum))

list_cell=[]
SIZE={1:"BIG",2:"MIDDLE",3:"LITTLE"} # sizes of pigs in cells
all_quant=0
big_cells_quant=0
mid_cells_quant=0
lit_cells_quant=0

for i in range(0,52): #get list of cells
    list_cell.append(cell(i+10,randint(6,13),randint(1,3)))
    all_quant+=list_cell[i].count
    if list_cell[i].size==1:
        big_cells_quant+=1
    if list_cell[i].size==2:
        mid_cells_quant += 1
    if list_cell[i].size==3:
        lit_cells_quant+=1
    print "Cell Number_"+str(list_cell[i].num)+"="+str(list_cell[i].count)+" :"+SIZE[list_cell[i].size]

print("**************************************")
print("ALL QUANT PIGS: "+str(all_quant))
print("BIG CELLS:" + str(big_cells_quant))
print("MID CELLS:" + str(mid_cells_quant))
print("LIT CELLS:" + str(lit_cells_quant))

GROUP_COUNT = 5 # count groups need
quant_1group = all_quant // GROUP_COUNT # quant pigs of one group
print("Quantity needed of one group: " +str(quant_1group))
print("**************************************")

# here will be sorting list by size
# bla bla
groups=groups()
index=0
while(index<GROUP_COUNT):
    group_ = group(index+1)
    while(quant_1group> group_.sum):
        try:
            cell_=list_cell.pop(0)
            group_.add_cell(cell_)
        except Exception as err:
            print(str(err))
            break

    groups.add_group(group_)
    index+=1




