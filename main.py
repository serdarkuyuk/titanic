#%%
from pathlib import Path
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

#%%

titanic_df = pd.read_csv(Path().joinpath('data','train.csv'))

# %%
sample_titanic = titanic_df.sample(10)



#%%
sum_null=titanic_df.isnull().sum()

#%%

def count_plot(x, hue, data):
    sns.countplot(x=x, hue=hue, data=data)
    plt.show()


count_plot('Survived', 'Sex', titanic_df)
count_plot('Survived', 'Pclass', titanic_df)
#%%


