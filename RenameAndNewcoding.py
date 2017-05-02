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
