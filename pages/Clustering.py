import streamlit as st
from pandas import read_csv
from scipy.cluster.hierarchy import linkage, dendrogram, maxdists
from matplotlib import pyplot as plt

st.set_page_config(
    "Cluster Analysis",
    "🔬",
    "wide",
    "expanded"
)

st.header("Cluster Analyse")

in_file = st.sidebar.file_uploader("Upload file", "csv")
if st.sidebar.button("Load file"):
    if "df" not in st.session_state:
        st.session_state["df"] = read_csv(in_file, index_col=0)


if "df" in st.session_state:

    st.dataframe(st.session_state["df"], width=600)


    # HIERARCHICAL CLUSTERING
    # =======================

    st.subheader("Hierarchical Clustering")

    attributes = st.multiselect(
        "Select Attributes",
        options=st.session_state["df"].select_dtypes("number").columns
    )

    Z = linkage(st.session_state["df"][attributes], method="ward")

    m = int(maxdists(Z)[-1])

    if m != 0:
        threshold = st.slider("Threshold", min_value=0, max_value=m)

        fig1 = plt.figure()
        dendrogram(Z, color_threshold=threshold)
        plt.hlines(y=threshold, xmin=plt.xlim()[0], xmax=plt.xlim()[1], color="r")

        st.pyplot(fig1)

    # VISUALIZING ATTRIBUTES
    # ======================

    st.subheader("Correlation Analysis")

    x_attribute = st.selectbox("X Axis", st.session_state["df"].select_dtypes("number").columns)
    y_attribute = st.selectbox("Y Axis", st.session_state["df"].select_dtypes("number").columns)

    fig2 = plt.figure()
    plt.scatter(
        st.session_state["df"][x_attribute],
        st.session_state["df"][y_attribute],
        alpha=0.4,
        color="orange"
    )
    plt.xlabel(x_attribute)
    plt.ylabel(y_attribute)
    st.pyplot(fig2)
