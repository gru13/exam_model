'''
    # "Physcis":[Frame,["1+2=","3","4","5","6"],["1+2=","3","4","5","6"],["1+2=","3","4","5","6"],["1+2=","3","4","5","6"],["1+2=","3","4","5","6"],["1+2=","3","4","5","6"],["1+2=","3","4","5","6"],Frame,[Frame]],

# creating qnos 
for a in Database:
    # print(a)
    # print(Database[a])
    no_of_question_len = len(Database[a]) - 3 #-3 because of 3 frame
    # print(no_of_question_len)
    Database[a][-1][0] = Database[a][-1][0](Database[a][0])
    Database[a][-1][0].pack(side=LEFT) # question nos tab frame
    # qnosf is Database[a][-1][0]
    for ax in range(1,no_of_question_len+1):
        Database[a][-1][ax] = Database[a][-1][ax](Database[a][-1][0],text=str(ax),command=lambda:qnos_command(Database[a][-1][-1],a,ax))
    # align of qnos
    # print(Database[a])
    # Button are in region of Database[a][-1][1:-1]
    l_contain_b_index = []
    if no_of_question_len % 3 == 0:
        for aa in range(0,no_of_question_len,3):
            for b in range(0,3):
                # print(a,b)
                l_contain_b_index.append([aa,b])
    else:
        remain = no_of_question_len % 3
        for aa in range(int((no_of_question_len-remain)/3)):
            for b in range(0,3):
                l_contain_b_index.append([aa,b])
        # print(remain)
        for ad in range(remain):
            l_contain_b_index.append([int((no_of_question_len-remain)/3),ad])
    print(l_contain_b_index)
    for ad in range(1,len(l_contain_b_index)+1):
        Database[a][-1][ad].grid(row=l_contain_b_index[ad-1][0],column=l_contain_b_index[ad-1][1])
'''