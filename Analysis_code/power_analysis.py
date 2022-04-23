from math import sqrt
from statsmodels.stats.power import TTestIndPower
  
#calculation of effect size
# size of samples in pilot study
n1, n2 = 8, 4
  
# variance of samples in pilot study
s1, s2 = 0.104, 0.205
  
# calculate the pooled standard deviation 
# (Cohen's d)
s = sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2))
  
# means of the samples
u1, u2 = 0.439, 0.194
  
# calculate the effect size
d = (u1 - u2) / s
print(f'Effect size: {d}')
  
# factors for power analysis
alpha = 0.05
power = 0.8
  
# perform power analysis to find sample size 
# for given effect
obj = TTestIndPower()
n = obj.solve_power(effect_size=d, nobs1=n1, alpha=alpha, 
                    ratio=n2/n1, alternative='larger')
  
print('Sample size/Number needed in each group: {:.3f}'.format(n))
