import os

import pandas as pd
import streamlit as st

if __name__ == '__main__':
    print(os.getcwd())
    elections = 25
    election_dir = f'{elections}'
    df_fact = pd.read_csv(f'{election_dir}/df_fact.csv')
    st.scatter_chart(df_fact,
                     x='tsne_x',
                     y='tsne_y',
                     color="cluster")
