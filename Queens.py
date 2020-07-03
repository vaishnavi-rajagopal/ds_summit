#8 Queens Problem

# Library Declaration
import random
import numpy as np
from numpy.random import choice
import pandas as pd
import re

class GA:

    global target, length, total_popln, mutation_rate, crossover_thres, top_n
    target = '46031752'
    total_popln = 150
    length = 8
    mutation_rate = 0.2
    crossover_thres = 0.5

    def InitPop(total):
    #Function to generate the initial population
      popln = []
      while len(popln) < total :
        seq = ''
        opts = ['0','1','2','3','4','5','6','7']
        for i in range(0,len(opts)):
          num = random.choice(opts)
          opts.remove(num)
          seq = seq + num
        popln.append(seq)
      return popln

    def CalcFitness(Pop):
    # Function to score the population
        score = []
        #length = 8
        for i in range(0,len(Pop)):
          fitscore = 0
          seq = Pop[i]
          for num in range(0,length):
            if seq[num] == target[num]:
              fitscore = fitscore + 1
          score.append(fitscore)
        return score

    def CrossOver(lst_val):
    # Function to perform cross over of the selected gene pool
      new_lst = []
      ops = set('01234567')
      top_n = int(crossover_thres * len(lst_val))
      for i in range(0, int(top_n/2)):
        for j in range(int(top_n/2), int(top_n)):
          child = lst_val[i][:4] + lst_val[j][4:]
          flag = len(child) - len(set(child))
          if (flag == 0):
            new_lst.append(child)
          else:
            child = ''.join(set(child))+''.join((ops-set(child)))
            new_lst.append(child)

      return new_lst

    def Mutation(lst_val):
    # Function to perform mutation of the selected gene pool
        opts = list('01234567')
        mut_prm = random.sample((list(range(0,len(lst_val)))),int(mutation_rate * len(lst_val)))
        for i in mut_prm:
          for j in lst_val[i]:
            val = random.sample(opts,2)
            elem1 = int(val[0])
            elem2 = int(val[1])
            lst_temp = list(lst_val[i])
            temp = lst_val[i][elem1]
            lst_temp[elem1] = lst_val[i][elem2]
            lst_temp[elem2] = temp
            new_val =''.join(lst_temp)
            lst_val[i] = new_val
        return lst_val

    def Main(self):
    # Main function to execute the Generic Algorithm
      fitness_score = 0

      inp_popln = GA.InitPop(total_popln)

      while int(fitness_score) != length :
        pop_score = []
        pop_score = GA.CalcFitness(inp_popln)
        lst_pop = pd.DataFrame(np.column_stack([inp_popln,pop_score]), columns=['value', 'score'])
        lst_pop = lst_pop.sort_values(by = ['score'], ascending = False)

        fitness_score = max(lst_pop['score'])
        #print(fitness_score)

        if int(fitness_score) != 8:

          inp_popln = []
          lst_pop = lst_pop.drop_duplicates()

          nxt_val = list(lst_pop['value'])
          term = GA.CrossOver(nxt_val)
          inp_popln = GA.Mutation(term)
      print(lst_pop['value'].head(1).to_string(index=False).strip())

# Call Main function in the GA class
queens8 = GA()
queens8.Main()
