lines = []
print("Nhập các dòng văn bản (Nhập 'done' để kết thúc):")

while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)

print("Các dòng sau khi chuyển thành CHỮ IN HOA:")
for line in lines:
    print(line.upper())
