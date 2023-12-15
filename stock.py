import pandas as pd
import json

# # 讀取 CSV 文件
# df = pd.read_csv('./OriginalStockData.csv')

# # 選擇特定的列，例如 'Column1'、'Column2'、'Column3'
# selected_columns = ['公司代號', '公司簡稱']
# df_selected = df[selected_columns]


# # 顯示選擇的列的前幾行
# print(df_selected.head())

# # 儲存csv
# df_selected.to_csv('selected_data.csv', index=False)

###############################################

# 讀取CSV文件
csv_file_path = './selected_data.csv'
df = pd.read_csv(csv_file_path, encoding='utf-8')

# 將DataFrame轉換為字典
data_dict = df.to_dict(orient='records')

# 將字典轉換為JSON字符串
json_data = json.dumps(data_dict, ensure_ascii=False, indent=2)

# 將JSON字符串保存到文件中
json_file_path = 'output.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)

###############################################


# # # 讀取 CSV 文件
# df = pd.read_csv('./OriginalStockData.csv')

# # 創建新的公司名稱列
# df['公司名稱'] = df['公司代號'].astype(str) + ' ' + df['公司簡稱']

# # 選擇需要的列，即公司代碼和公司名稱
# result_df = df[['公司代號', '公司名稱']]

# print(result_df.head())

# result_df.to_csv('selected_data.csv', index=False)
