import os

def batch_rename(folder_path, prefix):
    os.chdir(folder_path)
    
    files = os.listdir()
    
    for index, file_name in enumerate(files):

        name, extension = os.path.splitext(file_name)
        
        new_name = f"{prefix}_{index + 1}{extension}"
        
        os.rename(file_name, new_name)
        print(f"已将 {file_name} 重命名为 {new_name}")

# 使用示例
# batch_rename('C:/Photos', 'holiday_trip')
