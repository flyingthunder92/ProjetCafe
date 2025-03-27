# %% [markdown]
# <h1>Traitement des donnees</h1>

# %%
from pandas import read_csv
import pandas as pd
fichier='BeansDataSet.csv'
data=read_csv(fichier)
print(data)

# %%
from matplotlib import pyplot as plt
import seaborn as sn
print(data.describe())

# %%
class_count=data.count()
class_count

# %%
class_count=data.groupby('Region').size()
print(class_count)

# %%
class_count=data.groupby('Channel').size()
print(class_count)

# %%
class_count=data.groupby('Robusta').size()
print(class_count)

# %%
import pandas as pd

# Lecture du fichier CSV
df = pd.read_csv('BeansDataSet.csv')

# Somme des ventes Arabica toutes régions confondues
total_arabica = df['Arabica'].sum()

print(f"Total des ventes Arabica toutes régions confondues : {total_arabica}")


# %%
import pandas as pd

# Lecture du fichier CSV
df = pd.read_csv('BeansDataSet.csv')

# Somme des ventes Arabica toutes régions confondues
total_robusta = df['Robusta'].sum()

print(f"Total des ventes Robusta toutes régions confondues : {total_robusta}")


# %%
import pandas as pd

# Lecture du fichier CSV
df = pd.read_csv('BeansDataSet.csv')

# Somme des ventes Arabica toutes régions confondues
total_espresso = df['Espresso'].sum()

print(f"Total des ventes Espresso toutes régions confondues : {total_espresso}")


# %%
import pandas as pd

# Lecture du fichier CSV
df = pd.read_csv('BeansDataSet.csv')

# Somme des ventes Arabica toutes régions confondues
total_Lungo = df['Lungo'].sum()

print(f"Total des ventes Lungo toutes régions confondues : {total_Lungo}")


# %%
import pandas as pd

# Lecture du fichier CSV
df = pd.read_csv('BeansDataSet.csv')

# Somme des ventes Arabica toutes régions confondues
total_Latte = df['Latte'].sum()

print(f"Total des ventes Latte toutes régions confondues : {total_Latte}")


# %%
import pandas as pd

# Lecture du fichier CSV
df = pd.read_csv('BeansDataSet.csv')

# Somme des ventes Arabica toutes régions confondues
total_Cappuccino = df['Cappuccino'].sum()

print(f"Total des ventes Cappuccino toutes régions confondues : {total_Cappuccino}$")


# %%
import pandas as pd

# Lecture du fichier CSV
df = pd.read_csv('BeansDataSet.csv')

# Somme des ventes Arabica toutes régions confondues
total_vente_global=total_arabica+total_Cappuccino+total_espresso+total_Latte+total_Lungo+total_robusta

print(f"Total des ventes toutes régions confondues : {total_vente_global}$")


# %%
import pandas as pd

# Lecture du fichier CSV
df = pd.read_csv('BeansDataSet.csv')

# Somme des ventes Arabica toutes régions confondues
vente_online=df[df['Channel']=='Online'];
total_vente_online=vente_online[['Robusta','Arabica','Espresso','Lungo','Latte','Cappuccino']].sum().sum;

print(f"Total des ventes Online en fonction du cafe : {total_vente_online}$")


# %%

import pandas as pd

# Lecture du fichier CSV
df = pd.read_csv('BeansDataSet.csv')

# Somme des ventes Arabica toutes régions confondues
vente_online=df[df['Channel']=='Online'];
total_online_sales = vente_online.select_dtypes(include=['int64', 'float64']).sum().sum()

print(f"Total des ventes Online en fonction du cafe : {total_online_sales}$")



# %%
import pandas as pd

# Lecture du fichier CSV
df = pd.read_csv('BeansDataSet.csv')

# Somme des ventes Arabica toutes régions confondues
vente_store=df[df['Channel']=='Store'];
total_store_sales = vente_store.select_dtypes(include=['int64', 'float64']).sum().sum()

print(f"Total des ventes Online en fonction du cafe : {total_store_sales}$")

# %%
import pandas as pd

# Lecture du fichier CSV
df = pd.read_csv('BeansDataSet.csv')

# Somme des ventes Arabica toutes régions confondues
vente_store_cat=df[df['Channel']=='Store'];
total_vente_store=vente_store_cat[['Robusta','Arabica','Espresso','Lungo','Latte','Cappuccino']].sum().sum;

print(f"Total des ventes Online en fonction du cafe \n:{total_vente_store}$")


# %%
import pandas as pd

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv('BeansDataSet.csv')

# Grouper les données par région et calculer la somme des colonnes numériques
total_sales_by_region = df.groupby('Region').sum(numeric_only=True)

# Afficher le résultat
print("Total des ventes par région :")
print(total_sales_by_region)

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data.hist(figsize=(15,10),bins=20,layout=(3,3),grid=True)
plt.show()


# %%
total_sales_by_region.hist(figsize=(15,10),bins=20,layout=(3,3),grid=True)
plt.show()

# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# On regroupe les ventes par Channel (Online/Store), seulement les colonnes numériques
grouped = df.groupby('Channel').sum(numeric_only=True).reset_index()

# On "melt" le dataframe pour faciliter l'utilisation avec seaborn
melted = pd.melt(grouped, id_vars='Channel', var_name='Coffee_Type', value_name='Sales')

# Création du graphique
plt.figure(figsize=(12,6))
sns.barplot(data=melted, x='Coffee_Type', y='Sales', hue='Channel')
plt.title('Ventes des différents cafés par canal (Online vs Store)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# On regroupe les ventes par Channel (Online/Store) en sommant seulement les colonnes numériques
grouped = df.groupby('Channel').sum(numeric_only=True)

# Transposer pour mettre les types de café en lignes et les canaux en colonnes
grouped = grouped.transpose().reset_index()
grouped.columns = ['Coffee_Type', 'Online', 'Store']

# Melt pour faciliter l'affichage côte à côte
melted = pd.melt(grouped, id_vars='Coffee_Type', var_name='Channel', value_name='Sales')

# Création du graphique
plt.figure(figsize=(12,6))
sns.barplot(data=melted, x='Coffee_Type', y='Sales', hue='Channel')
plt.title('Ventes Online et Store par type de café')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# On regroupe les ventes par Channel (Online/Store) en sommant seulement les colonnes numériques
grouped = df.groupby('Channel').sum(numeric_only=True)

# Transposer pour mettre les types de café en lignes et les canaux en colonnes
grouped = grouped.transpose().reset_index()
grouped.columns = ['Coffee_Type', 'Online', 'Store']

# Melt pour faciliter l'affichage côte à côte
melted = pd.melt(grouped, id_vars='Coffee_Type', var_name='Channel', value_name='Sales')

# Création du graphique
plt.figure(figsize=(12,6))
sns.barplot(data=melted, x='Coffee_Type', y='Sales', hue='Channel')
plt.title('Ventes Online et Store par type de café')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# %%
import pandas as pd
import matplotlib.pyplot as plt



# Calculer le total des ventes pour chaque ligne
df['Total'] = df.iloc[:, 2:].sum(axis=1)

# Regrouper par canal de vente et sommer les totaux
sales_by_channel = df.groupby('Channel')['Total'].sum()

# Créer l'histogramme
channels = sales_by_channel.index
totals = sales_by_channel.values

plt.bar(channels[0], totals[0], color='blue', label='Online')
plt.bar(channels[1], totals[1], color='green', label='Store')
plt.title('Total Sales: Online vs Store')
plt.xlabel('Channel')
plt.ylabel('Total Sales')
plt.show()


# %%
#Total des ventes en fonction des regions:

import pandas as pd
import matplotlib.pyplot as plt

# Charger le dataset
df = pd.read_csv("BeansDataSet.csv")

# Calculer le total des ventes pour chaque ligne
df['Total'] = df.iloc[:, 2:].sum(axis=1)

# Regrouper les données par région et sommer les totaux
sales_by_region = df.groupby('Region')['Total'].sum()

# Créer l'histogramme
regions = sales_by_region.index
totals = sales_by_region.values

plt.bar(regions[0], totals[0], color='red', label='Central')
plt.bar(regions[1], totals[1], color='blue', label='North')
plt.bar(regions[2], totals[2], color='green', label='South')
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.show()


# %%
#moyenne des ventes



