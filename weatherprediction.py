import streamlit as s
import pandas as pd
import pickle as p
import sys

s.title('weather prediction')

precipitation = s.number_input('enter precipitation')
temp_max = s.number_input('enter step')
temp_min = s.number_input('enter type')
wind = s.number_input('enter old balance org')
year = s.number_input('enter old balance dest')
month = s.number_input('enter new balance dest ')
day = s.number_input('enter day ')


if s.button('predict'):
    in_pickle = open("predicting-weather.pkl", 'rb')
    pipe = p.load(in_pickle)
    result = pd.DataFrame(
            [[precipitation,temp_max,temp_min,wind,year,month,day]],
                              columns = ['precipitation','temp_max','temp_min','wind','year','month','day'])
    r = pipe.predict(result)

    if r==0:
        s.success('drizzle')
    elif r==1:
        s.success('rain')
    elif r==2:
        s.success('sun')
    elif r==3:
        s.success('snow')
    elif r==4:
        s.success('fog')
       
                                                                                               

    
    
    


        



        


    
    
        






#with open('pipe.pkl', 'rb') as file:
 #   final = pickle.load(file)

