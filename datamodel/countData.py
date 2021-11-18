import pandas as pd
import pymysql as py

def readDatabase():    
    connection=py.connect(
                host='127.0.0.1',
                user='root',
                password='',
                db='bd de psicología')

    print("A continuación se mostrará la cantidad de respuestas para cada pregunta, recuerde ignorar el registro 'Log' para cada caso")
    print("------------------------------------------------------------")
    sql1='SELECT *FROM respuesta1;'
    sql2='SELECT *FROM respuesta2;'
    sql3='SELECT *FROM respuesta3;'
    sql4='SELECT *FROM respuesta4;'
    sql5='SELECT *FROM respuesta5;'
    data1=pd.read_sql(sql1, connection)
    data2=pd.read_sql(sql2, connection)
    data3=pd.read_sql(sql3, connection)
    data4=pd.read_sql(sql4, connection)
    data5=pd.read_sql(sql5, connection)
    print(data1['Log'].value_counts())
    print("------------------------------------------------------------")
    print(data2['Log'].value_counts())
    print("------------------------------------------------------------")
    print(data3['Log'].value_counts())
    print("------------------------------------------------------------")
    print(data4['Log'].value_counts())
    print("------------------------------------------------------------")
    print(data5['Log'].value_counts())