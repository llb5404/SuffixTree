import sys

sys.setrecursionlimit(10**6)

string2 = "TAGTTAGCGAGA$"

def last_cp_position2(suffix, nc_val, cn, max_count,item_count=0, c_count=0, g_count=0, t_count=0, a_count=0, total_count = 0,new_countv = [],it_count = [],edge = '', edge_vec = []):
   
    new_values = nc_val[item_count] #this would just be list
    
   
    if len(new_values) - 1 == 0: #if no children, we can start writing edges

        if new_values[0][0] == suffix[total_count]:
            
            edge += suffix[total_count]
           
            total_count += 1
            if new_values[0][0] == 'C':
                c_count += 1
                new_count = c_count
            elif new_values[0][0] == 'T':
                t_count += 1
                new_count = t_count
            elif new_values[0][0] == 'G':
                g_count += 1
                new_count = g_count
            else:
                a_count += 1
                new_count = a_count
            #designate a list where you have # of previous counts of all asc. letters
            new_countv.append(new_count)

            item_count = cn[new_values[0][0]][new_values[0][1]-1][new_count - 1] #[which character in child][which # substring is this][number of letter that ou've had before]
            
            it_count.append(item_count)
            if item_count == max_count: 
                edge_vec.append(edge)
                return total_count, suffix[total_count], new_countv, item_count, it_count, edge_vec
            else:
                return last_cp_position2(suffix, nc_val, cn, max_count, item_count=item_count, c_count=c_count, g_count=g_count,
                                        t_count=t_count, a_count=a_count, total_count = total_count, new_countv = new_countv, it_count = it_count, edge = edge, edge_vec = edge_vec)  # Return the result of the recursive call
        elif new_values[0][0] != suffix[total_count]:
            return total_count, suffix[total_count], new_countv, item_count, it_count, edge_vec 
    else:
        k = 0 #if children, store in list, make another edge
        edge_vec.append(edge)
        while k <= len(new_values) - 1:

            if new_values[k][0] == suffix[total_count]:
                edge = suffix[total_count]
                total_count += 1
                if new_values[k][0] == 'C':
                    c_count += 1
                    new_count = c_count
                elif new_values[k][0] == 'T':
                    t_count += 1
                    new_count = t_count
                elif new_values[k][0] == 'G':
                    g_count += 1
                    new_count = g_count
                else:
                    a_count += 1
                    new_count = a_count

                new_countv.append(new_count)
                
                item_count = cn[new_values[k][0]][new_values[k][1]-1][new_count - 1]
                it_count.append(item_count)
                if item_count == max_count:
                    edge_vec.append(edge)
                    return total_count, suffix[total_count], new_countv, item_count, it_count, edge_vec 
                else:
                    return last_cp_position2(suffix, nc_val, cn, max_count,item_count=item_count, c_count=c_count, g_count=g_count,
                                            t_count=t_count, a_count=a_count, total_count = total_count, new_countv = new_countv, it_count = it_count, edge = edge, edge_vec = edge_vec)  # Return the result of the recursive call
            elif new_values[k][0] != suffix[total_count]:
                if k == len(new_values) - 1:
                    edge_vec.append(edge)
                    return total_count, suffix[total_count], new_countv, item_count, it_count, edge_vec
                else: 
                    k+=1
    return total_count, suffix[total_count], new_countv, item_count, it_count, edge_vec


def change_nc2(nc,nc_val, node_num, new_char,suffix,cum_length,item_count,num_iter):           
    #iteration 1, cum_length = len(string)
    nc_to_append = nc_val[item_count]
    nc_to_append.append([new_char,num_iter])
    nc_val[item_count] = nc_to_append
    nc[item_count] = nc_val[item_count]
    new_string = suffix[node_num:]
  
    for i in range(len(new_string)):
        nc_val.append([[new_string[i],num_iter]])
    for i in range(len(new_string)):
        nc[i+cum_length] = nc_val[i+cum_length] #key = index, val = character #for nc2, this is len(string)

    return nc

#look at total number of nodes in common (in this case 1)
def change_cn2(suffix,node_num,position_location,item_counts,cn,cn_val,cum_length):

    new_string = suffix[node_num:]

    c_vec1 = []
    g_vec1 = []
    t_vec1 = []
    a_vec1 = []
    dollar_vec1 = []
    old_string = string2[:node_num]
  
    #get letter associated w string, and get associated position using newcount
    if len(old_string) == 1:
        for i in range(len(old_string)):
            pos = item_counts[i]
            
            if old_string[i] == 'C':
                    c_vec1.append(pos)
            elif old_string[i] == 'G':
                    g_vec1.append(pos)
            elif old_string[i] == 'T':
                    t_vec1.append(pos)
            elif old_string[i] == 'A':
                    a_vec1.append(pos)
            
        
    else:
        
        for i in range(len(old_string)):
            pos = item_counts[i]

            if old_string[i] == 'C':
                        c_vec1.append(pos)
            elif old_string[i] == 'G':
                        g_vec1.append(pos)
            elif old_string[i] == 'T':
                        t_vec1.append(pos)
            elif old_string[i] == 'A':
                        a_vec1.append(pos)
                        
    if len(new_string) == 1:
        dollar_vec1.append(cum_length)
    else:
        for i in range(len(new_string)): #create lists with positions
            if new_string[i] == 'C':
                    c_vec1.append(i+cum_length)
            elif new_string[i] == 'G':
                    g_vec1.append(i+cum_length)
            elif new_string[i] == 'T':
                    t_vec1.append(i+cum_length)
            elif new_string[i] == 'A':
                    a_vec1.append(i+cum_length)
            elif new_string[i] == '$':
                dollar_vec1.append(i + cum_length)
        
    

    cn_val[0].append(c_vec1)
    cn_val[1].append(g_vec1)
    cn_val[2].append(t_vec1)
    cn_val[3].append(a_vec1)
    cn_val[4].append(dollar_vec1)

    cn['C'] = cn_val[0]
    cn['G'] = cn_val[1]
    cn['T'] = cn_val[2]
    cn['A'] = cn_val[3]
    cn['$'] = cn_val[4]
    return len(new_string) + cum_length-1

def build_suffix_tree(string):
    ##PART 1: Initialize the tree with the string
    node_to_char = {} #dictionary that maps each numbered node to characters
    nc_values = [] #list to store values of nc dict
    char_to_node = {} #dictionary that maps each character to numbered nodes
    cn_values = [] #list to store values of cn dict
    c_vec = [] #vectors with the positions of letters in string
    g_vec = []
    t_vec = []
    a_vec = []
    dollar_vec = []

    for i in range(len(string)):
        nc_values.append([[string[i],1]])
        node_to_char[i] = nc_values[i] #key = index, val = character


    for i in range(len(string)): #create lists with positions
        if string[i] == 'C':
                c_vec.append(i+1)
        elif string[i] == 'G':
                g_vec.append(i+1)
        elif string[i] == 'T':
                t_vec.append(i+1)
        elif string[i] == 'A':
                a_vec.append(i+1)
        elif string[i] == '$':
                dollar_vec.append(i+1)


    cn_values.append([c_vec])
    cn_values.append([g_vec])
    cn_values.append([t_vec])
    cn_values.append([a_vec])
    cn_values.append([dollar_vec])

        #key = character, value = positions of character in string
    char_to_node['C'] = cn_values[0]
    char_to_node['G'] = cn_values[1]
    char_to_node['T'] = cn_values[2]
    char_to_node['A'] = cn_values[3]
    char_to_node['$'] = cn_values[4]

   
    #max node is len(string) - 1 + len(substring) - 1 +  
    max_count = len(string)
    mc_vec = [len(string)]
    ##PART 2: Build Tree
    for i in range(1,len(string)-1):
        suffix = string[i:]
    
        last_cp_position2(suffix, nc_values, char_to_node, max_count-1,new_countv = [],it_count = [])
        node_num = last_cp_position2(suffix, nc_values, char_to_node, max_count-1,new_countv = [],it_count = [])[0]
        new_char = last_cp_position2(suffix, nc_values, char_to_node, max_count-1,new_countv = [],it_count = [])[1]
        position_location = last_cp_position2(suffix, nc_values, char_to_node, max_count-1,new_countv = [],it_count = [])[2]
        item_count = last_cp_position2(suffix, nc_values, char_to_node, max_count-1,new_countv = [],it_count = [])[3] 
        item_counts = last_cp_position2(suffix, nc_values, char_to_node, max_count-1,new_countv = [],it_count = [])[4]
        change_nc2(node_to_char,nc_values,node_num,new_char,suffix,max_count,item_count,i+1)
        max_count = change_cn2(suffix,node_num,position_location,item_counts,char_to_node,cn_values,max_count+1)
    
    return char_to_node,node_to_char, max_count, cn_values
    
char_to_node,node_to_char,max_count, cn_values = build_suffix_tree(string2)
nc_sl = {}
for node in range(max_count):
    for i in range(len(node_to_char[node])):
        nc_sl[tuple(node_to_char[node][i])] = []

def dfs(node, char_to_node, node_to_char, visited, edge_vec, edge, nc_sl = nc_sl):
    for node in range(max_count):
        if node not in visited:
            
            for i in range(len(node_to_char[node])):
                print(nc_sl)
                print(node_to_char[node])
                if edge[0] == "_":
                     print("sl")
                     print(node_to_char[node])
                if node == max_count:
                    edge[0] += node_to_char[node][i][0]
                    edge_vec.append(edge[0])
                    return edge_vec
                elif node != 0 and len(node_to_char[node]) > 1:
                    edge_vec.append(edge[0])  # Append the current edge to edge_vec
                    edge[0] = ""  # Reset edge to an empty string
                    edge[0] += node_to_char[node][i][0]
                elif node_to_char[node][i][0] == '$':
                    edge[0] += node_to_char[node][i][0]
                    edge_vec.append(edge[0])
                    edge[0] = "_"
                    
                else:
                    edge[0] += node_to_char[node][i][0] 
                visited.add(node)

                for child_node in char_to_node[node_to_char[node][i][0]]:
                    for j in range(len(child_node)):
                        dfs(child_node[j], char_to_node, node_to_char, visited, edge_vec, edge, nc_sl = nc_sl) 
                        return edge_vec        
    return edge_vec


root_node = 0
visited_nodes = set()
edge_vector = []
start_node = 0  # Replace with the actual starting node
edge_str = [""]
result = dfs(start_node, char_to_node, node_to_char, visited_nodes, edge_vec = edge_vector, edge = edge_str)
result.append("$")
print(result)

with open('Practice.txt', 'w') as f:
    for i in range(len(result)):
        f.write(result[i])
        f.write('\n')
    







    









    

