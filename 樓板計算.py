import pandas as pd

# 讀取 Excel 檔案，指定 header 為 1 以使用第二行作為列名
df = pd.read_excel('/workspaces/race/分析樓板明細表.xlsx', header=1)

while True:
    # 提示用戶輸入多個族群類型，以逗號分隔
    族群類型輸入 = input("請輸入一個或多個族群類型（以逗號分隔），或輸入'結束'以結束程式: ")
    if 族群類型輸入 == '結束':
        break
    族群類型列表 = [類型.strip() for 類型 in 族群類型輸入.split(',')]

    # 根據用戶輸入過濾數據
    filtered_df = df[df['族群類型'].isin(族群類型列表)]

    # 計算體積和數量的總和

    總面積= filtered_df['面積'].sum()
    總數量 = filtered_df['數量'].sum()

    # 輸出總體積和總數量
    print(f"總面積: {總面積}, 總數量: {總數量}")