import io
import pandas as pd
import plotly.graph_objects as go
import pytest

from main import (
    plot_box_violin,
    plot_sunburst_chart,
    plot_boxplot,
    plot_correlation_matrix,
    plot_pca,
)

# Fixtures para os DataFrames
@pytest.fixture
def df_binance():
    binance_csv = """Altcoin,Preço (USD),Volume (24h),Market Cap (USD),Variação (24h)
Aergo (AERGO),0.12,5000000,60000000,2.5
Aion (AION),0.08,3000000,40000000,-1.2
Bluzelle (BLZ),0.05,2000000,25000000,0.8
Celer Network (CELR),0.03,1500000,18000000,1.5
COTI (COTI),0.04,1000000,20000000,-0.5
Elrond (EGLD),50,8000000,2500000000,3.2
Fetch.ai (FET),0.25,6000000,125000000,1.8
Harmony (ONE),0.02,4000000,10000000,-0.9
Hedera Hashgraph (HBAR),0.06,2500000,30000000,0.7
ICON (ICX),0.30,7000000,150000000,2.1
IOST (IOST),0.01,1800000,50000000,-1.5
Kava (KAVA),0.80,3500000,400000000,0.5
Komodo (KMD),0.55,1500000,275000000,-0.2
Kyber Network (KNC),0.70,1000000,350000000,3.0
Nervos Network (CKB),0.008,8000000,40000000,-0.7
Ocean Protocol (OCEAN),0.45,1200000,225000000,1.8
Ontology (ONT),0.50,2000000,250000000,1.2
Quant (QNT),100,4000000,5000000000,-1.5
Ravencoin (RVN),0.035,3000000,175000000,2.1
Reserve (RSV),0.02,1500000,10000000,0.5"""
    return pd.read_csv(io.StringIO(binance_csv))

@pytest.fixture
def df_github():
    github_csv = """Altcoin,Número de Commits (último mês),Número de Issues Abertas,Número de Pull Requests (último mês),Atividade da Comunidade (escala 1-10)
Aergo (AERGO),180,30,60,7.5
Aion (AION),150,25,50,6.8
Bluzelle (BLZ),120,20,40,6.2
Celer Network (CELR),190,32,65,7.8
COTI (COTI),160,28,55,7.2
Elrond (EGLD),250,40,80,8.5
Fetch.ai (FET),220,35,70,8.2
Harmony (ONE),170,30,58,7.5
Hedera Hashgraph (HBAR),200,38,75,8.0
ICON (ICX),230,35,75,8.3
IOST (IOST),140,22,45,6.5
Kava (KAVA),210,35,70,8.0
Komodo (KMD),165,28,55,7.3
Kyber Network (KNC),240,40,80,8.7
Nervos Network (CKB),185,32,62,7.8
Ocean Protocol (OCEAN),205,35,70,8.2
Ontology (ONT),195,33,68,7.9
Quant (QNT),260,45,90,9.0
Ravencoin (RVN),175,30,60,7.6
Reserve (RSV),155,25,50,7.0"""
    return pd.read_csv(io.StringIO(github_csv))

# Testes para as funções de plotagem
def test_plot_box_violin(df_binance):
    plot_box_violin(df_binance, "Altcoin", "Preço (USD)", "Teste Box Violin")

def test_plot_sunburst_chart(df_binance):
    plot_sunburst_chart(df_binance, "Market Cap (USD)", "Altcoin", "Teste Sunburst Chart")

def test_plot_boxplot(df_binance):
    plot_boxplot(df_binance, "Altcoin", "Volume (24h)", "Teste Boxplot")

def test_plot_correlation_matrix(df_github):
    plot_correlation_matrix(df_github, "Teste Correlation Matrix")

def test_plot_pca(df_binance):
    plot_pca(df_binance, "Teste PCA")