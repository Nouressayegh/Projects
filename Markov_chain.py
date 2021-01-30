# module load anaconda/python3
# ipython  Markov_chain.py
# sbatch Job_3D_Markov_chain.job

import Markov_chain_functions 
# We first import the functions. 

extract_transition_matrix = Markov_chain_functions.extract_transition_matrix
simulate_finite_mc = Markov_chain_functions.simulate_finite_mc
invariant_distribution = Markov_chain_functions.invariant_distribution

probability_distribution_k = Markov_chain_functions.probability_distribution_k
frequency_distribution_k = Markov_chain_functions.frequency_distribution_k
continuous_curves=Markov_chain_functions.continuous_curves



#the importation of the matrix
P1=Markov_chain_functions.extract_transition_matrix("transition_matrix_q2.csv")
I=[0,1,2,3,4,5,6,7,8,9,10,11]



#We extract the eigen vector and save the frequecy distribution in a file 

eigen_vec=invariant_distribution("transition_matrix_q2.csv",histogram = True,state_space=I)

n = 10000 
frequency_distribution_k("transition_matrix_q2.csv", 11, n, histogram = True, ini = 0, state_space = I)



proba_X = []
for k in range(5):
    proba_X.append(probability_distribution_k("transition_matrix_q2.csv", k, histogram = False, ini = 0, state_space = I))

print(proba_X)


I2=[1,2,3,4,5,6,7,8,9,10,11]

#we create the transition matrix of this new Markov Chain in the file "transition_matrix.csv"
print( "Question 3-a :")
P2=Markov_chain_functions.extract_transition_matrix("transition_matrix.csv")
print(P2)


asymptotic_proba = probability_distribution_k("transition_matrix.csv",k = 100000,histogram = True,ini=10,state_space=[])
print(asymptotic_proba)



#the two files are in the zip document
fichier3 = "subclass_1.csv"
fichier4 = "subclass_2.csv"
invariant1 = invariant_distribution(matrix_file = fichier3,histogram = False, state_space = [0,1,2,3,4])
print("the asymptotic probability distribution of the first subclasse {1,2,3,4,5} is: ",invariant1)
invariant2 = invariant_distribution(matrix_file = fichier4,histogram = False, state_space = [6,7,8,9])
print("the asymptotic probability distribution of the first subclasse {6,7,8,9} is: ",invariant2)
print(invariant1 + invariant2)



def simulate_T10f(matrix_file,k,ini):
    states = simulate_finite_mc(matrix_file = matrix_file ,n = k,histogram = False,ini = ini,state_space = [0,1,2,3,4,5,6,7,8,9,10])
    while states[0] == 9 or states[0] == 10:
        states = states[1:]
    return states
    
chain_t10f = simulate_T10f("transition_matrix.csv",k =1000,ini =10)
print("The Markov chain after it leaves the states 10 for another other than 11 is: ",chain_t10f)


continuous_curves([0,1,2,3,4,5,6,7,8,9,10],asymptotic_proba, plot_name= "plot.png", X_name = "X", Y_name = "Y",X2 = [], Y2 = [ ])


