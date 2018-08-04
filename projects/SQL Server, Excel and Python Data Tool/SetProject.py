# -*- coding: utf-8 -*-


import pandas as pd
import sqlalchemy as sa
import pyodbc 
from time import gmtime, strftime
import os
import numpy as np

#######################################################################################################################      
def import_excel(selectedChoiceServer, selectedChoiceDatabase, selectedChoiceSchema, filePath):
    try:
        #this part is to import Project excel sheet into SQL server database
        xl = pd.ExcelFile(filePath)
        df1 = xl.parse()  
        importdatabase = 'Import' + selectedChoiceDatabase[4:]
        importschema =  selectedChoiceSchema + '-' + strftime("%Y%m%d%H%M%S", gmtime()) 
        importschema_string =  '[' + importschema +']'
        filename = filePath[::-1][0:filePath[::-1].find('/')][::-1]
    
        #connect to import database
        server = selectedChoiceServer
        database = importdatabase
        username = ''
        password = ''
        
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    
        sql = 'create schema ' + importschema_string 
        print()
        cursor = cnxn.cursor()
        cursor.execute('USE [' + database + ']')
        cursor.execute(sql)
        cnxn.commit()
    
        
        engine = sa.create_engine('mssql+pyodbc://:@' + selectedChoiceServer + '/' + importdatabase +'?driver=ODBC+Driver+11+for+SQL+Server')    
        # write the DataFrame to a table in the sql database
        df1.to_sql(filename, engine, schema = importschema)
        
    #######################################################################################################################    
    
        #this part is to just print given data into final output excel sheet
        customer_Project_sql =  """
            select type,	num	,date,	name,	OpenBalance 
                from 
                	[""" +  importdatabase  +"""].[""" + importschema +"""].[""" +filename +"""]  xl
                where 
                	xl.type is not null
        """
         
        data = pd.read_sql(customer_Project_sql, cnxn)
        #print(data)
        
        TotalofCustomerProject = float(data['OpenBalance'].sum())
        #print (TotalofCustomerProject)
        writer = pd.ExcelWriter( selectedChoiceSchema +  ' Project Analysis.xlsx')
        data.to_excel(writer, sheet_name='Customer Project')


    #######################################################################################################################      
    # this part is used to connect to prod database
        
        server = selectedChoiceServer
        database = selectedChoiceDatabase
        username = ''
        password = ''
        
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password,autocommit=False)
    
    #######################################################################################################################      
        #create the global temporary table for bills
        create_global_temp_table_sql = """select * into ##aktemp"""+selectedChoiceSchema+"""  from [""" +  importdatabase  +"""].[""" + importschema +"""].[""" +filename +"""] as xl where xl.Num is not null and xl.type = \'Invoice\' """
        #print()
        cursor = cnxn.cursor()
        cursor.execute(create_global_temp_table_sql)
        cnxn.commit()

        
    #######################################################################################################################      
    #dealing with bills 
    
    
    #this part is to get only non-duplicate bills 
       
        create_non_duplicate_bills_sql =     """
        
        WITH duplicate_cte AS
        (
        select 
        	xl.*
        	,ROW_NUMBER() OVER(Partition BY xl.num ORDER BY xl.num) AS rownum
        	,COUNT(xl.num) OVER(Partition BY xl.num) AS cntr
        from 
        	##aktemp1"""+selectedChoiceSchema+"""  xl
        inner join """ + selectedChoiceSchema + """.Invoice i on xl.num = i.Number 
        )
        SELECT * 
        INTO ##non_duplciate_bills"""+selectedChoiceSchema+""" 
        FROM duplicate_cte WHERE cntr = 1
        
        """
        
        print()
        cursor = cnxn.cursor()
        cursor.execute(create_non_duplicate_bills_sql)
        cnxn.commit()
        
    
    
    #######################################################################################################################      
    # this part is to get next value     
        
        
        get_current_value_sql =     """
        select  cast(s.current_value as nvarchar) 
          from sys.sequences s
          join sys.schemas ss
          on s.schema_id = ss.schema_id
          where ss.name = '""" + selectedChoiceSchema + """'
          and s.name like '%int64%'
        """
        
        cursor = cnxn.cursor()
        cursor.execute(get_current_value_sql)
        row = cursor.fetchone()
        strrow = str(row)
        newstr = strrow.replace("\'",'').replace(",",'').replace('(','').replace(')','')
        identity = int(newstr)
        print("identity at start :" ,identity)
        ConstId = identity 
        identity = identity + 1
        
    #######################################################################################################################          
    #update balances of all imported bills to 0
        
        
        update_bill_balance_to_zero_sql =     """
        UPDATE i
        SET    i.balance = 0
        FROM """ + selectedChoiceSchema +   """.bill i
        WHERE  i.[STATUS] <> 0
           AND i.ImportId IS NOT NULL
        """
        
        cursor = cnxn.cursor()
        cursor.execute(update_bill_balance_to_zero_sql)
        
    #######################################################################################################################      
    #update balances from excel
        
        
        update_balance_from_excel_sql =     """
        UPDATE i
        SET    i.Balance = xl.[OpenBalance]
        FROM   ##non_duplciate_bills"""+selectedChoiceSchema+"""  xl
        INNER JOIN """ + selectedChoiceSchema + """.Invoice i ON xl.num = i.Number
        """
        
        cursor = cnxn.cursor()
        cursor.execute(update_balance_from_excel_sql)
        
    
    #######################################################################################################################      
    #insert applied payment type for Project tool
        check_paymenttype_sql =     """
        SELECT 1 FROM """+selectedChoiceSchema+""".[TypeofPayment] WHERE [Name] = \'Applied payment type by Project tool\'
        """
        
        cursor = cnxn.cursor()
        cursor.execute(check_paymenttype_sql)
        row = cursor.fetchone()
        strrow = str(row)
        newstr = strrow.replace("\'",'').replace(",",'').replace('(','').replace(')','')
        yes = newstr
        print("PaymentType exist then 1 else None :" ,newstr)      
    
    
    
        if yes == 'None':
            insert_applied_payment_type_sql =     """
            INSERT INTO """ + selectedChoiceSchema + """.[TypeofPayment] ( [Id] ,
                                                 [Name] ,
                                                 [Active] ,
                                                 [ImportId] )
            VALUES (""" +str(identity)+ """, 'Applied payment type by Project tool', 0, 'Applied payment type by Project tool' )
            """
            
            cursor = cnxn.cursor()
            cursor.execute(insert_applied_payment_type_sql)
            identity = identity + 1
            
            
        else:
            print('hi')
            
        
    #######################################################################################################################      
    #setting ceiling
    
        identity = identity + 1000
    
        state =  """ALTER SEQUENCE ["""+ selectedChoiceSchema +"""].[Int64-Generator] restart WITH  +""" + str(identity)
        
        set_ceiling_sql =     """
        exec sp_executesql ? """ 
       
        
    
        cursor = cnxn.cursor()
        cursor.execute(set_ceiling_sql,state)
        
        
        get_current_value_sql =     """
        select  cast(s.current_value as nvarchar) 
          from sys.sequences s
          join sys.schemas ss
          on s.schema_id = ss.schema_id
          where ss.name = '""" + selectedChoiceSchema + """'
          and s.name like '%int64%'
        """
        
        cursor = cnxn.cursor()
        cursor.execute(get_current_value_sql)
        row = cursor.fetchone()
        strrow = str(row)
        newstr = strrow.replace("\'",'').replace(",",'').replace('(','').replace(')','')
        identity = int(newstr)
        print("identity at end :" ,identity)
    
    #######################################################################################################################          
        writer.save()
        cnxn.commit()
        cursor.close()
        cnxn.close()    
        return 1
        
    #######################################################################################################################      
  
    except Exception as e:
        print('Some Error Occured, so Project was not set')
        print('Error is :' + str(e))
        return str(e)
    
    
    
#######################################################################################################################      
  