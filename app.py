import plotly.express as px 
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt


st.set_page_config(
    page_title="My expenses data",
    layout="wide")

alt.themes.enable("dark")


st.title("My expenses data")
st.write("This is a dataset that consists of my monthly income and expenses. I've been tracking my finances for 4 months till now and I'll update it whenever I finish the consecutive months.")

df = pd.read_csv("expense_data_1.csv")
df = df.drop(df.columns[7], axis=1)
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y %H:%M")
dfe = df[df["Income/Expense"] != "Income"]


with st.expander("See Data"):
    st.dataframe(df)

col1, col2 = st.columns([1.5, 1])

with col1:
    pie = px.sunburst(
        df,
        path=["Income/Expense", "Category"],
        values="Amount",
        title="Sunburst Chart: Income/Expense Category Note"
    )

    pie.update_layout(
        width=900,  
        height=900,  
        margin=dict(t=50, l=0, r=0, b=50)  
    )
    st.plotly_chart(pie)




with col2 : 
    tab1 , tab2 = st.tabs(["Line","eCDF"])

    with tab1:

        fig = px.line(dfe, x="Date", y=["Amount"],
                    color = "Category",
                    hover_data="Note",
                    title='Expenses')
        fig.update_xaxes(
            dtick="M1",
            tickformat="%b\n%Y",
            ticklabelmode="period",
            )

        fig.update_layout(
            width=900, 
            height=400,  
            margin=dict(t=50, l=0, r=0, b=50)  
        )
        st.plotly_chart(fig)

    with tab2: 

        fig = px.ecdf(dfe, x="Date", y=["Amount"],
                    color = "Category",
                    hover_data="Note",
                    title='Expenses')
        fig.update_xaxes(
            dtick="M1",
            tickformat="%b\n%Y",
            ticklabelmode="period",
            )

        fig.update_layout(
            width=900,  
            height=300,  
            margin=dict(t=50, l=0, r=0, b=50)  
        )
        st.plotly_chart(fig)



    fig = px.bar(df, x="Category", y="Amount", color="Income/Expense")
    fig.update_layout(
        width=900,  
        height=300,  
        margin=dict(t=50, l=0, r=0, b=50)  
    )
    st.plotly_chart(fig)


