from typing import List, Dict
import numpy as np
import operator
from collections import Counter
import matplotlib.pyplot as plt
import os

def get_oov_rates(train:List, test:List) -> List:
    
    main_list = np.setdiff1d(test,train)
    ctr= len(main_list)
    ov= ctr/len(test)
    return ov


def plot_oov_rates(oov_rates:Dict) -> None:
    
   key= list(oov_rates.keys())
   values= list(oov_rates.values())
   plt.figure(figsize=(8,6))
   plt.plot(key,values)
   plt.ylabel('OVV-Rate')
   plt.xlabel('Vocabulary_Size')
   plt.xticks(rotation=45)
   plt.show()