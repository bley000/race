import pandas as pd

# 讀取 Excel 文件
df = pd.read_excel('/workspaces/race/數量表.xlsx')

# 對 '材料' 列進行分組，並對每個分組的 '數量' 列求和
材料數量總和 = df.groupby('材料')['數量'].sum()

# 輸出每種材料的總數量
print(材料數量總和)