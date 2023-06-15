import streamlit as st
from PIL import Image
import pickle
import json
import numpy as np

"""
# Credit-Score Classification
"""
st.markdown("![Alt text](https://static.wixstatic.com/media/3becc4_3a836c1a60f4473b95a15d67e7686d62~mv2.gif)")
with open('./model_pickle','rb') as f:
    model= pickle.load(f)

path= "./columns.json"
f1= open(path)
data= json.load(f1)
data_columns= data['data_columns']
# close the file
f1.close()

monthly_inhand_salry= st.number_input('Enter Your monthly_inhand_salry, Example:20000')
monthly_inhand_salry= float(monthly_inhand_salry)
st.write('You Selected',monthly_inhand_salry)

Delay_from_due_date= st.number_input('Enter No of days delay from due_date, Example:10days, only put number in below box')
Delay_from_due_date= int(Delay_from_due_date)
st.write('You Selected',Delay_from_due_date)

Credit_Utilization_Ratio = st.number_input('Enter Your Credit_Utilization_Ratio, Example: 30%, Enter only number')
Credit_Utilization_Ratio= float(Credit_Utilization_Ratio)
st.write('You Selected',Credit_Utilization_Ratio)

Total_EMI_per_month = st.number_input('How much EMI monthly you pay, Example:10000')
Total_EMI_per_month= float(Total_EMI_per_month)
st.write('You Selected',Total_EMI_per_month)

Annual_Income_new = st.number_input('Enter Your Annual_Income, Example:400000')
Annual_Income_new= float(Annual_Income_new)
st.write('You Selected',Annual_Income_new)

Age_new = st.number_input('Enter Your Age:')
Age_new= int(Age_new)
st.write('You Selected',Age_new)

Outstanding_Debt_new = st.number_input('Enter Your Outstanding_Debt, Example:5000')
Outstanding_Debt_new= float(Outstanding_Debt_new)
st.write('You Selected',Outstanding_Debt_new)

Monthly_Balance_new = st.number_input('Enter Your Monthly Savings, Example:2000')
Monthly_Balance_new= float(Monthly_Balance_new)
st.write('You Selected',Monthly_Balance_new)

Credit_Mix= st.selectbox(
    'Select your Credit_Mix_Type',
    ('Credit_Mix_new_Bad','Credit_Mix_new_Good','Credit_Mix_new_Standard')
)
st.write('You Selected',Credit_Mix)

Payment_Behaviour= st.selectbox(
    'Select your Payment_Behaviour',
    ('Payment_Behaviour_new_High_spent_Large_value_payments','Payment_Behaviour_new_High_spent_Medium_value_payments','Payment_Behaviour_new_High_spent_Small_value_payments','Payment_Behaviour_new_Low_spent_Large_value_payments','Payment_Behaviour_new_Low_spent_Medium_value_payments','Payment_Behaviour_new_Low_spent_Small_value_payments')
)
st.write('You Selected',Payment_Behaviour)

Payment_min_amount= st.selectbox(
    'Do you pay the Min Amount Payment?',
    ('Payment_of_Min_Amount_new_No','Payment_of_Min_Amount_new_Yes')
)
st.write('You Selected',Payment_min_amount)



def predict_credit_score(monthly_inhand_salry,Delay_from_due_date,Credit_Utilization_Ratio,Total_EMI_per_month,Annual_Income_new,Age_new,Outstanding_Debt_new,Monthly_Balance_new,Credit_Mix,Payment_Behaviour,Payment_min_amount):
    try:
        credit_mix_index= data_columns.index(Credit_Mix.lower())
        Payment_Behaviour_index= data_columns.index(Payment_Behaviour.lower())
        Payment_min_amount_index= data_columns.index(Payment_min_amount.lower())
    except:
        credit_mix_index= -1
        Payment_Behaviour_index = -1
        Payment_min_amount_index = -1
    x= np.zeros(len(data_columns))
    x[0]=monthly_inhand_salry
    x[1]=Delay_from_due_date
    x[2]=Credit_Utilization_Ratio
    x[3]= Total_EMI_per_month
    x[4]= Annual_Income_new
    x[5]= Age_new
    x[6]= Outstanding_Debt_new
    x[7]= Monthly_Balance_new
    if (credit_mix_index>=0) and (Payment_Behaviour_index>=0) and (Payment_min_amount_index>=0):
        x[credit_mix_index]=1
        x[Payment_Behaviour_index]=1
        x[Payment_min_amount_index]=1
    credit_score=  model.predict([x])[0]
    if credit_score==1:
        return 'Good'
    elif credit_score==2:
        return 'Standard'
    else:
        return 'Poor'
    
if st.button('Predict Credit-Score'):
    st.write(predict_credit_score(monthly_inhand_salry,Delay_from_due_date,Credit_Utilization_Ratio,Total_EMI_per_month,Annual_Income_new,Age_new,Outstanding_Debt_new,Monthly_Balance_new,Credit_Mix,Payment_Behaviour,Payment_min_amount))
