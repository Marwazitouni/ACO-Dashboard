def write_solution(path,nb_subsystems,subsystems):
    if path[0] == "placeholder":
        print("No solutions found")
    else:
        solution = [[] for _ in range(nb_subsystems) ]
        for ele in path[0]:
            if (ele[1]+1<=subsystems[ele[0]].nb_components):
                solution[ele[0]].append(ele[1] + 1)

        for i in range(nb_subsystems):
            print("Subsystem ", i+1,sorted(solution[i])) 

        print("Availability : ", path[1][1])
        print("Cost : ", path[1][2])
        print("Capacity : ", path[1][3])




