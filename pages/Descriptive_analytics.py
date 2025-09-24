# Percentage of women
percentage_women = (df['Sex'] =='Female').mean() * 100

# Percentage of men
percentage_men = (df['Sex'] =='Male').mean() * 100

#Mean age 
mean_age = df["Age"].mean()

col1, col2 = st.columns(3)
col1.metric("Percentage of women (%)", f"{percentage_women: .2f}", border=True)
col2.metric("Percentage of men (%)", f"{percentage_men: .2f}", border=True)
col2.metric("Percentage of men (%)", f"{mean_age: .2f}", border=True)