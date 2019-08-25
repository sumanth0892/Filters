import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main(file = 'gasPricesBrazil.tsv'):
    

    file = 'gasPricesBrazil.tsv'
    gas_df = pd.read_csv(file,sep='\t')
    gas_df = gas_df.rename(columns = {'DATA INICIAL':'Initial Date',
                                  'DATA FINAL':'Final Date',
                                  'REGIÃO':'Region',
                                  'ESTADO':'STATE',
                                  'PRODUTO':'Product',
                                  'NÚMERO DE POSTOS PESQUISADOS':'Number of Searches',
                                  'UNIDADE DE MEDIDA':'Unit of Measurement',
                                  'PREÇO MÉDIO REVENDA':'Average Resale Price',
                                  'DESVIO PADRÃO REVENDA':'Default Resale',
                                  'PREÇO MÍNIMO REVENDA':'Minimum Resale Price',
                                  'PREÇO MÁXIMO REVENDA':'Maximum Resale Price',
                                  'COEF DE VARIAÇÃO REVENDA':'Resale Change Coeff',
                                  'PREÇO MÉDIO DISTRIBUIÇÃO':'Average Price Distribution',
                                  'DESVIO PADRÃO DISTRIBUIÇÃO':'Default Distribution Deviation',
                                  'PREÇO MÍNIMO DISTRIBUIÇÃO':'Minimum Price Distribution',
                                  'PREÇO MÁXIMO DISTRIBUIÇÃO':'Maximum Price Distribution',
                                  'COEF DE VARIAÇÃO DISTRIBUIÇÃO':'Distribution Variation Coeff',
                                  'MÊS':'Month',
                                  'ANO':'year',
                                  'MARGEM MÉDIA REVENDA':'Resale Average Margin'})
    gas_df = gas_df.drop({'Number of Searches','Unit of Measurement','Month','year'},axis=1)
    

#Create dataframes by region and product
    hydEth_north = gas_df[(gas_df['Region'] == 'NORTE') & (gas_df['Product'] == 'ETANOL HIDRATADO')]
    hydEth_northeast = gas_df[(gas_df['Region'] == 'NORDESTE') & (gas_df['Product'] == 'ETANOL HIDRATADO')]
    hydEth_south = gas_df[(gas_df['Region'] == 'SUL') & (gas_df['Product'] == 'ETANOL HIDRATADO')]
    hydEth_southeast = gas_df[(gas_df['Region'] == 'SUDESTE') & (gas_df['Product'] == 'ETANOL HIDRATADO')]
    hydEth_midwest = gas_df[(gas_df['Region'] == 'CENTRO OESTE') & (gas_df['Product'] == 'ETANOL HIDRATADO')]
    hydEth_dfs = [hydEth_north,hydEth_northeast,hydEth_south,hydEth_southeast,hydEth_midwest]
    for i in range(len(hydEth_dfs)):
        hydEth_dfs[i] = hydEth_dfs[i].drop(['Region','Product'],axis=1)
    hydEth_n = hydEth_dfs[0];hydEth_ne = hydEth_dfs[1];hydEth_s = hydEth_dfs[2];hydEth_se = hydEth_dfs[3];hydEth_mw = hydEth_dfs[4]
    del hydEth_north,hydEth_northeast,hydEth_south,hydEth_southeast,hydEth_midwest
    
        
    comG_north = gas_df[(gas_df['Region'] == 'NORTE') & (gas_df['Product'] == 'GASOLINA COMUM')]
    comG_northeast = gas_df[(gas_df['Region'] == 'NORDESTE') & (gas_df['Product'] == 'GASOLINA COMUM')]
    comG_south = gas_df[(gas_df['Region'] == 'SUL') & (gas_df['Product'] == 'GASOLINA COMUM')]
    comG_southeast = gas_df[(gas_df['Region'] == 'SUDESTE') & (gas_df['Product'] == 'GASOLINA COMUM')]
    comG_midwest = gas_df[(gas_df['Region'] == 'CENTRO OESTE') & (gas_df['Product'] == 'GASOLINA COMUM')]
    comG_dfs = [comG_north,comG_northeast,comG_south,comG_southeast,comG_midwest]
    for i in range(len(comG_dfs)):
        comG_dfs[i] = comG_dfs[i].drop(['Region','Product'],axis=1)
    comG_n = comG_dfs[0];comG_ne = comG_dfs[1];comG_s = comG_dfs[2];comG_se = comG_dfs[3];comG_mw = comG_dfs[4]
    del comG_north,comG_northeast,comG_south,comG_southeast,comG_midwest
    

    lpg_north = gas_df[(gas_df['Region'] == 'NORTE') & (gas_df['Product'] == 'GLP')]
    lpg_northeast = gas_df[(gas_df['Region'] == 'NORDESTE') & (gas_df['Product'] == 'GLP')]
    lpg_south = gas_df[(gas_df['Region'] == 'SUL') & (gas_df['Product'] == 'GLP')]
    lpg_southeast = gas_df[(gas_df['Region'] == 'SUDESTE') & (gas_df['Product'] == 'GLP')]
    lpg_midwest = gas_df[(gas_df['Region'] == 'CENTRO OESTE') & (gas_df['Product'] == 'GLP')]
    lpg_dfs = [lpg_north,lpg_northeast,lpg_south,lpg_southeast,lpg_midwest]
    for i in range(len(lpg_dfs)):
        lpg_dfs[i] = lpg_dfs[i].drop(['Region','Product'],axis=1)
    lpg_n = lpg_dfs[0];lpg_ne = lpg_dfs[1];lpg_s = lpg_dfs[2];lpg_se = lpg_dfs[3];lpg_mw = lpg_dfs[4]
    del lpg_north,lpg_northeast,lpg_south,lpg_southeast,lpg_midwest
    
    cng_north = gas_df[(gas_df['Region'] == 'NORTE') & (gas_df['Product'] == 'GNV')]
    cng_northeast = gas_df[(gas_df['Region'] == 'NORDESTE') & (gas_df['Product'] == 'GNV')]
    cng_south = gas_df[(gas_df['Region'] == 'SUL') & (gas_df['Product'] == 'GNV')]
    cng_southeast = gas_df[(gas_df['Region'] == 'SUDESTE') & (gas_df['Product'] == 'GNV')]
    cng_midwest = gas_df[(gas_df['Region'] == 'CENTRO OESTE') & (gas_df['Product'] == 'GNV')]
    cng_dfs = [cng_north,cng_northeast,cng_south,cng_southeast,cng_midwest]
    for i in range(len(cng_dfs)):
        cng_dfs[i] = cng_dfs[i].drop(['Region','Product'],axis=1)
    cng_n = cng_dfs[0];cng_ne = cng_dfs[1];cng_s = cng_dfs[2];cng_se = cng_dfs[3];cng_mw = cng_dfs[4]
    del cng_north,cng_northeast,cng_south,cng_southeast,cng_midwest
    
    do_north = gas_df[(gas_df['Region'] == 'NORTE') & (gas_df['Product'] == 'ÓLEO DIESEL')]
    do_northeast = gas_df[(gas_df['Region'] == 'NORDESTE') & (gas_df['Product'] == 'ÓLEO DIESEL')]
    do_south = gas_df[(gas_df['Region'] == 'SUL') & (gas_df['Product'] == 'ÓLEO DIESEL')]
    do_southeast = gas_df[(gas_df['Region'] == 'SUDESTE') & (gas_df['Product'] == 'ÓLEO DIESEL')]
    do_midwest = gas_df[(gas_df['Region'] == 'CENTRO OESTE') & (gas_df['Product'] == 'ÓLEO DIESEL')]
    do_dfs = [do_north,do_northeast,do_south,do_southeast,do_midwest]
    for i in range(len(do_dfs)):
        do_dfs[i] = do_dfs[i].drop(['Region','Product'],axis=1)
    do_n = do_dfs[0];do_ne = do_dfs[1];do_s = do_dfs[2];do_se = do_dfs[3];do_mw = do_dfs[4]
    del do_north,do_northeast,do_south,do_southeast,do_midwest
    

    ds_north = gas_df[(gas_df['Region'] == 'NORTE') & (gas_df['Product'] == 'ÓLEO DIESEL S10')]
    ds_northeast = gas_df[(gas_df['Region'] == 'NORDESTE') & (gas_df['Product'] == 'ÓLEO DIESEL S10')]
    ds_south = gas_df[(gas_df['Region'] == 'SUL') & (gas_df['Product'] == 'ÓLEO DIESEL S10')]
    ds_southeast = gas_df[(gas_df['Region'] == 'SUDESTE') & (gas_df['Product'] == 'ÓLEO DIESEL S10')]
    ds_midwest = gas_df[(gas_df['Region'] == 'CENTRO OESTE') & (gas_df['Product'] == 'ÓLEO DIESEL S10')]
    ds_dfs = [ds_north,ds_northeast,ds_south,ds_southeast,ds_midwest]
    for i in range(len(ds_dfs)):
        ds_dfs[i] = ds_dfs[i].drop(['Region','Product'],axis=1)
    ds_n = ds_dfs[0];ds_ne = ds_dfs[1];ds_s = ds_dfs[2];ds_se = ds_dfs[3];ds_mw = ds_dfs[4]
    del ds_north,ds_northeast,ds_south,ds_southeast,ds_midwest

    #Plot the maximum resale values
    ax = plt.gca()
    comG_n.plot(kind='line',x='Final Date',y='Maximum Resale Price',ax=ax)
    lpg_n.plot(kind='line',x='Final Date',y='Maximum Resale Price',ax=ax)
    do_n.plot(kind='line',x='Final Date',y='Maximum Resale Price',ax=ax)
    plt.grid()
    plt.show()

    

    #plot prices for region
    
    
    

    #return gas_df

    

    
if __name__ == '__main__':
    main()


