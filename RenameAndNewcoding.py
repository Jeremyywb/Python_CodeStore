# A new encoding type
# GB18030 has more stringcode than gbk
import os

listfiles = os.listdir()
for fname in listfiles:
    df = read_csv(fname,"GB18030",'\t')
    newfname = "NEW_" + fname
    df.to_csv(newfname,index = False)

# This code to rename file


to_rename = os.listdir()
for docname in to_rename:
    path_doc = "E:/path/to/file/"+docname
    path_rename = "E:/another_or_sanme_path/to/file/"+newnames
    os.rename(path_doc,path_rename)

def genSQL(col,tbname,fname,dbname):
    createsql_0 = 'create table ['+ dbname +'].[dbo].['
    createsql_1 = ']( '
    colstr = ',\n'.join([co + ' VARCHAR(MAX)' for co in col]) + ')'
    sql = createsql_0 +tbname+createsql_1 + colstr
    Bucksql = 'bulk insert [' + dbname + '].[dbo].[' + tbname + "] from 'E:/自动化存储源/准备导入数据库/" + fname + "'"+''' with(   
   FIRSTROW=2,
   FIELDTERMINATOR='\t',   
   ROWTERMINATOR='\n'  
)  '''
    return sql,Bucksql
