import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


st.set_page_config(page_title="Analyse des ventes de café", layout="wide")


st.title("Analyse des ventes de café")

# Création des onglets
tab1, tab2, tab3, tab4 = st.tabs(["Accueil", "Analyse des ventes", "Analyse de la répartition","Recommandations"])

with tab1:
    st.header("Bienvenue dans la page d'analyse des ventes de café")
    st.write("""
    Cette application vous permet d'explorer les données de ventes de café à travers différents canaux et régions.
    
    Naviguez entre les onglets pour découvrir :
    - L'analyse complète des ventes par produit et par région
    - La répartition des ventes entre les différents canaux de distribution
    - Des recommandations basées sur les données
    GitHub Link: https://github.com/flyingthunder92/ProjetCafe
    """)
    
    st.image("https://theamericanomp.com/wp-content/uploads/2020/03/great-coffee-bean.jpeg", 
             caption="Analyse des ventes de café", width=600)

with tab2:
    st.header("Analyse des ventes")
    
    
    data = pd.read_csv("BeansDataSet.csv")
    
    
    total_arabica = data['Arabica'].sum()
    total_robusta = data['Robusta'].sum()
    total_espresso = data['Espresso'].sum()
    total_Lungo = data['Lungo'].sum()
    total_Latte = data['Latte'].sum()
    total_Cappuccino = data['Cappuccino'].sum()
    total_vente_global = total_arabica + total_Cappuccino + total_espresso + total_Latte + total_Lungo + total_robusta
    
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Ventes totales Arabica", f"{total_arabica:,}")
        st.metric("Ventes totales Robusta", f"{total_robusta:,}")
    with col2:
        st.metric("Ventes totales Espresso", f"{total_espresso:,}")
        st.metric("Ventes totales Lungo", f"{total_Lungo:,}")
    with col3:
        st.metric("Ventes totales Latte", f"{total_Latte:,}")
        st.metric("Ventes totales Cappuccino", f"{total_Cappuccino:,}")
    
    st.metric("Ventes globales totales", f"{total_vente_global:,}")
    
    

        
    fig, ax = plt.subplots(figsize=(10, 6))

    categories = ['Arabica', 'Robusta', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']
    values = [total_arabica, total_robusta, total_espresso, total_Lungo, total_Latte, total_Cappuccino]

    ax.bar(categories, values)
    ax.set_ylabel('Ventes totales')
    ax.set_title('Comparaison des ventes par catégorie')

    #
    plt.xticks(rotation=45, ha='right')

   
    for i, v in enumerate(values):
        ax.text(i, v, f'{v:,}', ha='center', va='bottom')

   
    plt.tight_layout()

    
    st.pyplot(fig)
    
    
    st.subheader("Ventes par région")
    data['Total'] = data.iloc[:, 2:].sum(axis=1)
    sales_by_region = data.groupby('Region')['Total'].sum()
    
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    regions = sales_by_region.index
    totals = sales_by_region.values
    ax2.bar(regions, totals, color=['red', 'blue', 'green'])
    ax2.set_title('Total Sales by Region')
    ax2.set_xlabel('Region')
    ax2.set_ylabel('Total Sales')
    st.pyplot(fig2)
    
    
    st.subheader("Détail des ventes par région")
    total_sales_by_region = data.groupby('Region').sum(numeric_only=True)
    st.dataframe(total_sales_by_region.style.format("{:,.0f}"))



    data['Total_Ventes'] = data['Robusta'] + data['Arabica'] + data['Espresso'] + data['Lungo'] + data['Latte'] + data['Cappuccino']


    st.title("Top 3 des ventes par région")


    for region in data['Region'].unique():
    
        region_data = data[data['Region'] == region]
    
    
        top_3 = region_data.nlargest(3, 'Total_Ventes')
    
   
        st.subheader(f"Région {region}")
    
    
        st.dataframe(top_3[['Channel', 'Total_Ventes', 'Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']])
    
    
        st.write("---")
    
   
with tab3:
    st.header("Analyse de la répartition des ventes")
    
  
    st.subheader("Répartition des ventes par canal")
    vente_online=data[data['Channel']=='Online'];
    total_online_sales = vente_online.select_dtypes(include=['int64', 'float64']).sum().sum()
    
    vente_store=data[data['Channel']=='Store'];
    total_store_sales = vente_store.select_dtypes(include=['int64', 'float64']).sum().sum()
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Ventes totales Online", f"{total_online_sales:}$")
    with col2:
        st.metric("Ventes totales en magasin", f"{total_store_sales:}$")
    
    
    st.subheader("Comparaison des ventes par type de café et par canal")
    grouped = data.groupby('Channel').sum(numeric_only=True).reset_index()
    melted = pd.melt(grouped, id_vars='Channel', var_name='Coffee_Type', value_name='Sales')
    
    fig3, ax3 = plt.subplots(figsize=(12,6))
    sns.barplot(data=melted, x='Coffee_Type', y='Sales', hue='Channel', ax=ax3)
    ax3.set_title('Ventes des différents cafés par canal (Online vs Store)')
    ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45)
    plt.tight_layout()
    st.pyplot(fig3)
    
    
    st.subheader("Répartition globale des ventes par canal")
    sales_by_channel = data.groupby('Channel')['Total'].sum()
    
    fig4, ax4 = plt.subplots(figsize=(8,5))
    channels = sales_by_channel.index
    totals = sales_by_channel.values
    ax4.bar(channels, totals, color=['blue', 'green'])
    ax4.set_title('Total Sales: Online vs Store')
    ax4.set_xlabel('Channel')
    ax4.set_ylabel('Total Sales')
    st.pyplot(fig4)

    data['Total_Ventes'] = data['Robusta'] + data['Arabica'] + data['Espresso'] + data['Lungo'] + data['Latte'] + data['Cappuccino']

    # Titre 
    st.title("Analyse des moyennes de ventes")

    # 1. Moyennes par région
    st.header("1. Moyennes par région")
    moyennes_region = data.groupby('Region')[['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino', 'Total_Ventes']].mean()
    st.dataframe(moyennes_region.style.format("{:,.1f}"))

    # 2. Moyennes par produit (toutes régions confondues)
    st.header("2. Moyennes par produit (global)")
    moyennes_produits = data[['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']].mean().to_frame().T
    st.dataframe(moyennes_produits.style.format("{:,.1f}"))

    # 3. Moyennes par canal (medium)
    st.header("3. Moyennes par canal de vente")
    moyennes_canal = data.groupby('Channel')[['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino', 'Total_Ventes']].mean()
    st.dataframe(moyennes_canal.style.format("{:,.1f}"))

    # 4. Moyennes détaillées par région ET par canal
    st.header("4. Moyennes par région et par canal")
    moyennes_region_canal = data.groupby(['Region', 'Channel'])[['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']].mean()
    st.dataframe(moyennes_region_canal.style.format("{:,.1f}"))

    # 5. Moyennes par produit pour chaque région
    st.header("5. Détail par produit et par région")
    produits = ['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']
    for produit in produits:
        st.subheader(f"Moyennes pour {produit}")
        moyennes_produit_region = data.groupby('Region')[produit].mean().to_frame()
        st.dataframe(moyennes_produit_region.style.format("{:,.1f}"))
    

    

   

    # Colonnes de produits
    product_cols = ['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']

    # 1. Agrégation par Région et Canal
    grouped = data.groupby(['Region', 'Channel'])[product_cols].mean()

    # 2. Calcul des moyennes globales
    global_means = data[product_cols].mean()

    # 3. Ratio par rapport à la moyenne
    ratio = grouped.div(global_means) * 100

    
    ratio = ratio.reset_index()
    heatmap_data = ratio.melt(id_vars=['Region', 'Channel'], 
                            value_vars=product_cols,
                            var_name='Produit',
                            value_name='Ratio')

    
    fig, ax = plt.subplots(figsize=(12, 6))
    heatmap_data['Region_Channel'] = heatmap_data['Region'] + ' - ' + heatmap_data['Channel']
    pivot_data = heatmap_data.pivot(index='Region_Channel',
                                columns='Produit',
                                values='Ratio')

    # Heatmap avec seaborn
    sns.heatmap(pivot_data, 
            annot=True, 
            fmt=".0f", 
            cmap="RdYlGn",
            center=100,
            linewidths=.5,
            ax=ax,
            cbar_kws={'label': '% de la Moyenne Globale'})

    # Rotation des labels x
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

    # Titres
    ax.set_title('Performance des Ventes par Rapport à la Moyenne Globale', pad=20)
    ax.set_xlabel('Type de Produit')
    ax.set_ylabel('Région et Canal')

    # Ajustement de la disposition
    plt.tight_layout()

    # Affichage dans Streamlit
    st.pyplot(fig)
    
with tab4:
    st.header("Recommandations")   
    
     
    
    st.subheader("Recommandations")
    st.write("""
    1. **Augmenter les promotions sur l'Arabica** - Les ventes sont inférieures à celles du Robusta
    2. **Développer les ventes en ligne des cafés spéciaux** - Les Lattes et Cappuccinos se vendent mieux en magasin
    3. **Cibler la région Sud** - C'est la région avec le plus fort volume de ventes
    4. **Optimiser l'inventaire en magasin** - Réduire les stocks de Lungo qui se vendent moins bien
    5. **Packaging différencié** - Créer des offres bundles pour booster les ventes d'Espresso en ligne
    6. **Creer des programmes de fidelite** - Cela permettra de collecter des informations sur la clientelle et donc mieux cibler les compagne de communication
    7. **Ajouter les adresses et codes postaux des differents stores** - Pour avoir une analyse plus precise il est necessaire d'avoir les adresses des differents magasins pour cibler ceux dont les ventes ne sont pas satisfaisants et etablir une politique de developpement basee sur la proximite a la clientelle
    8. **Reevaluer la pertinence de certains stores** - Mettre en place d'urgence des politiques de communication afin d'augmenter les ventes dans la region nord et centre qui restent tres faibles par rapport a la region sud
    9. **Cibler certains medium (Channel) de la region qui tombent sous la moyenne des ventes globales** -                   
                               
    """)

