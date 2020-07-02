#8 Queens Problem

# Library Declaration
import random
import numpy as np
from numpy.random import choice
import pandas as pd
import re

class GA:

    def __init__(self,target,initial_pop,mutation_rate,crossover_thres):
    # Class Constructor
      self.target = target
      self.total_popln = initial_pop
      self.mutation_rate = mutation_rate
      self.top_n = int(crossover_thres * float(initial_pop))

    def InitPop(total):
    #Function to generate the initial population
      popln = []
      while len(popln) < total :
        seq = ''
        opts = ['1','2','3','4','5','6','7','8']
        for i in range(1,9):
          num = random.choice(opts)
          opts.remove(num)
          seq = seq + num
        popln.append(seq)
      return popln

    def CalcFitness(Pop,target):
    # Function to score the population
      score = []
      for i in range(0,len(Pop)):
        fitscore = 0
        seq = Pop[i]
        for num in range(0,8):
          if seq[num] == target[num]:
            fitscore = fitscore + 1
        score.append(fitscore)
      return score

    def CrossOver(lst_val,n):
    # Function to perform cross over of the selected gene pool
      new_lst = []
      ops = set('12345678')
      for i in range(0,n):
        for j in range(0,n):
          child = lst_val[i][0]+lst_val[j][1]+lst_val[i][2]+lst_val[j][3]+lst_val[i][4]+lst_val[j][5]+lst_val[i][6]+lst_val[j][7]
          flag = len(child) - len(set(child))
          if flag == 0:
            new_lst.append(child)
          else:
            child = ''.join(set(child))+''.join((ops-set(child)))
            new_lst.append(child)
      return new_lst

    def Mutation(lst_val):
    # Function to perform mutation of the selected gene pool
      new_lst = []
      opts = list('0123456')
      for i in range(0,len(lst_val)):
        val = int(random.choice(opts))
        inv = lst_val[i][val:val+2]
        if val == 0:
          mutnt = inv[2::-1] + lst_val[i][2:]
        elif val == 6:
          mutnt = lst_val[i][:6] + inv[2::-1]
        else:
          mutnt = lst_val[i][:val]+inv[2::-1]+lst_val[i][val+2:]
        new_lst.append(mutnt)
      return new_lst

    def Main(self):
    # Main function to identify the right sequence
        inp_popln = GA.InitPop(self.total_popln)
        fitness_score = 0

        while int(fitness_score) != 8 :
          pop_score = []
          pop_score = GA.CalcFitness(inp_popln,self.target)

          lst_pop = pd.DataFrame(np.column_stack([inp_popln,pop_score]), columns=['value', 'score'])
          lst_pop = lst_pop.sort_values(by = ['score'], ascending = False)
          fitness_score = max(lst_pop['score'])

          inp_popln = []
          lst_pop = lst_pop.drop_duplicates()
          nxt_val = list(lst_pop['value'])

          co_popln = GA.CrossOver(nxt_val,self.top_n)
          k = self.mutation_rate*float(len(co_popln))
          inp_popln = GA.Mutation(random.sample(co_popln,int(k)))

        output = lst_pop['value'].head(1).to_string(index=False).strip()
        print(output)

# Call Main function in the GA class
queens8 = GA('57142863',150,0.75,0.2)
queens8.Main()
