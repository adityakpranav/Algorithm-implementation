import random


#datasets
X = list(range(20))
Y = list(range(20))


def individualNSize(n:list,individual_size=3)->str:
    choice =[0,1]
    individual=random.choice(['+','-'])
    for _ in range(n):
        individual+=random.choice(['0','1'])
    return individual    


	
def fitness(population:dict)->dict:
    if type(population)==list: 
	    population = dict.fromkeys(population,1)
    for individual in population:
        error=0
        for x,y in zip(X,Y):
            error+=(int(individual,2)*x-y)**2
        population[individual] = round((error/len(X))**0.5,2)
    return(population)
	

def crossover(population:dict ,n_crossovers:int)->list:

    '''
	population :dict{string bits: fittness }
    population_temp : list :values decreasing order of fitness
	
	'''
    
    if type(population)==dict:
        population_temp = sorted(population,key=lambda a:population[a])
    n_individual = len(population_temp)
    for ith in range(int(n_individual/2)):

#      list of bits string(individual divided at bit level) 
        one = list(population_temp[ith])
        two = list(population_temp[-ith-1])
        
        for _ in range(n_crossovers):
            swap = random.randint(0,min(len(one),len(two))-1)
        
            one[swap],two[swap] = two[swap],one[swap]
            population_temp[ith], population_temp[-ith-1] =  "".join(one),"".join(two) 

    return(population_temp)

	
def mutation(victims:list)->list:

    new_gen=[]
    for victim in victims:
        victim = list(victim)
        mut = random.randint(0,len(victim)-1)

        if mut ==0:
            victim[mut]=random.choices(['+','-'])[0]
        else:
            victim[mut]=random.choices(['0','1'])[0]
        new_gen.append("".join(victim))
    return(new_gen)

	

	
#parameters
population_limit = 4
individual_size=3
population=[]
generation =0
limit=200
n_crossovers =2


#initial population 
for _ in range(population_limit):
    population.append(individualNSize(individual_size))


#generations
while(generation<limit):
    print("generation::",generation)
    population = fitness(population)
    print(" current population",population)
    print("\n")
    if all(population.values()):
        population = fitness(mutation(crossover(population,n_crossovers)))
        while(len(population)<population_limit ):
            ind = individualNSize(individual_size)
            population.setdefault(ind,1)
        generation+=1
    else:
        print("DONE!!!")
        break

		
print("finished in generation::",generation)
print("population::",population)
print("Y = (%d) * X"%int(sorted(population,key=lambda x:population[x] )[0],2))

'''O/P
generation:: 0
 current population {'-001': 22.23, '+110': 55.57, '+111': 66.68, '-100': 55.57}


generation:: 1
 current population {'-000': 11.11, '-100': 55.57, '+100': 33.34, '-111': 88.9}


generation:: 2
 current population {'+101': 44.45, '+100': 33.34, '-100': 55.57, '-110': 77.79}


generation:: 3
 current population {'-100': 55.57, '+110': 55.57, '-110': 77.79, '+001': 1}


generation:: 4
 current population {'+001': 0.0, '-010': 33.34, '+110': 55.57, '-110': 77.79}


DONE!!!
finished in generation:: 4
population:: {'+001': 0.0, '-010': 33.34, '+110': 55.57, '-110': 77.79}
Y = (1) * X

'''


