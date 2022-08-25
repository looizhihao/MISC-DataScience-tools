import pandas as pd
import numpy as np

#to remove chinese characters from pandas to enhance software compatibility

def remove_chinese_characters(df : pd.DataFrame, column_name:str,target:str = r'[^\x00-\x7F]+', replace_with : str= '')  -> pd.Series:
    print('replacing chinese caharactors')
    df[column_name]= df[column_name].str.replace(target,replace_with) 

def simple_clean_column(df:pd.DataFrame, column:str,replace :str ='',replace_with:str=''):
    print('simple cleaning')
    df[column]= df[column].str.replace(r'\x98','')
    df[column]= df[column].str.replace('\"','')
    df[column]=df[column].str.upper()
    if replace != '':
        replace_str(df,column,replace,replace_with)

    df[column]=df[column].str.strip()

def replace_nan(df:pd.DataFrame, column:str, replace:float = np.nan, replace_with:str=''):
    if replace != '':
        df[column]=df[column].replace(replace, replace_with)

def replace_str(df:pd.DataFrame, column:str,replace :str ='',replace_with:str=''):
    print('simple replace')
    
    df[column]=df[column].str.replace(replace, replace_with)

    df[column]=df[column].str.strip()

def extract_num(df:pd.DataFrame, column:str):
     df[column]=df[column].str.replace(r"[a-zA-Z]",'')

import country_converter as coco    
def convert_country(df:pd.DataFrame, column:str,out_column:str=''):
    if out_column == '':
        out_column=column
    cc = coco.CountryConverter()
    country_names=df[column]
    df[out_column] = cc.convert(names = country_names, to = 'ISO2')