file_path = "test.txt"

# 寫入文件
with open(file_path, "w", encoding="utf-8") as file:
    file.write("Hello world")

print(f"File '{file_path}' has been cre ated and writ ten successfully.")