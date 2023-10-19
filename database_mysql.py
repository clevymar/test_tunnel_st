import pandas as pd
import sys
sys.path.insert(0, '..')

from database_connect import PADB_connection


    
def SQLA_read_table(tablename,retrieve_only_info_for_last_date:bool=False):
    with PADB_connection() as engine:
        try:
            if retrieve_only_info_for_last_date:
                sql = f""" select * from {tablename} where Date = (select max(Date) from {tablename}) """
            else:
                sql = f""" select * from {tablename} """
            tmp = pd.read_sql_query(sql , engine)
            return tmp
        except Exception as e:
            errorMsg = f"Error getting info from {tablename}"
            print(errorMsg, "FAIL")
            raise Exception(errorMsg) from e
    






