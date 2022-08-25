import pandas as pd
import json
import collections
import os

import sys 
def analyze(fn):
    df = pd.read_csv(fn,encoding='latin1' )
    all_data= dict()

    for  col in df:
        data= list(set(df[col].fillna('(blanks)')))
        data_len=len(data)
        #all_data[col]['Count']=data_len
        
        try : data =sorted(data)
        except: pass
        all_data[data_len]={col:data}

        print('\n',col,':',data_len)
        if data_len<20:
                
                print (*data,sep = "\n")  
        else :
            print ('too_much to print, refer to output report')

    od = collections.OrderedDict(sorted(all_data.items()))
    report_name=f'analyze_report_{os.path.basename(fn)}.json'
    with open(report_name, "w") as outfile:
        json.dump(od, outfile,indent=4)


    print (report_name," is created")    
   
if __name__=="__main__":
    if len(sys.argv)==1:
        print("usage: scriptname.py [filename1] [filename2]...")
    for i,arg in enumerate(sys.argv):
        if i!=0:
            try:
                analyze(arg)
            except:
                pass 

