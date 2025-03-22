# %%
import streamlit as st
from pandas import read_csv
from scipy.cluster.hierarchy import linkage, dendrogram
from matplotlib import pyplot as plt


st.header("Cluster Analyse")

in_file = st.sidebar.file_uploader("Upload file", "csv")
if st.sidebar.button("Load file"):
    if "df" not in st.session_state:
        st.session_state["df"] = read_csv(in_file, index_col=0)

    st.dataframe(st.session_state["df"], width=600)
    attributes = st.multiselect("Select Attributes", options=st.session_state["df"].columns)

    Z = linkage(st.session_state["df"][attributes], method="ward")

    m = int(Z[-1][1])

    threshold = st.slider("Threshold", min_value=0, max_value=m)

    fig = plt.figure()
    dendrogram(Z, color_threshold=threshold)

    st.pyplot(fig)
