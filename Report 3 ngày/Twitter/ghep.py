import os
import pandas as pd

#hàm tách camp
# def tachcamp(str):
#     arr=str.split("_")
#     max=arr[0]
#     for i in range(len(arr)):
#         if len(max) < len(arr[i]):
#             max=arr[i]
    
#     return max
    



# Thư mục chứa các file Excel
folder_path = 'D:\\Report 3 ngày\\Twitter'

# Danh sách các cột bạn muốn giữ lại
import os
import pandas as pd

# Thư mục chứa các file Excel


# Danh sách các cột bạn muốn giữ lại
selected_columns = ['Account name', 'Campaign name', 'Reach', 'Impressions', 'Frequency', 'Currency',
                    'Amount spent (USD)', 'Attribution setting', 'Campaign delivery', 'Reporting starts',
                    'Reporting ends']

# Tạo một DataFrame để chứa dữ liệu từ các file Excel
merged_data = pd.DataFrame()

# Lặp qua tất cả các file trong thư mục
for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx'):  # Chỉ xử lý các file có định dạng Excel
        file_path = os.path.join(folder_path, filename)
        
        # Đọc dữ liệu từ file Excel
        
        df = pd.read_excel(file_path)
        df = df.rename(columns={'Status': 'Campaign delivery'})
        df = df.rename(columns={'Spend': 'Attribution setting'})
        df['Account name'] = os.path.splitext(filename)[0]
        missing_columns = set(selected_columns) - set(df.columns)
        for missing_column in missing_columns:
            df[missing_column] = 0
        df = df[selected_columns]
        df = df[~((df['Campaign name'].str.contains('total', case=False, na=False)) | (df['Attribution setting'] == 0))]
        
        merged_data = pd.concat([merged_data, df], ignore_index=True)
        
merged_data.to_excel('Twitter 3 ngày.xlsx', index=False)
