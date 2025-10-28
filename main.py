import pandas as pd
import numpy as np
import scipy.stats as stats
import streamlit as st

df=pd.read_csv("/Users/s.sivasankaranarayanan/PycharmProjects/Data Science classes/heart.csv")
st.title("Heart Disease")
st.subheader("shows the relation between two factor affection Heart disease")
#(df.columns)

c1=st.selectbox("enter column 1",df.columns)
c2=st.selectbox("enter column 2",df.columns)
def find_chi_square(df, col1, col2):
  con = pd. crosstab(df[col1], df[col2])
  chi2,pval, dof, freq = stats.chi2_contingency(con)
  st.write(f"chi square : {round(chi2,2)}")
  st.write(f"pvalue : {round(pval,2)}")
  st.write(f"degree of freedom : {dof}")
  #print(f"frequency \n: {freq}")

  val_data = pd.DataFrame(freq, index =con.index, columns = con.columns)
  #print(val_data)
  return pval

def But():

    pval = find_chi_square(df, c1, c2)
    if pval < 0.05:
        st.success (f"Relationship exists between col {c1} and col {c2}")
    else:
        st.error (f"Relationship does not exist between col {c1} and col {c2}")

if st.button("Check"):
    But()
