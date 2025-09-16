text_list = ["kitob", "dastur", "AI", "hello", "python"]

long_text = []

for i in text_list:
    if len(i) > 5:
        long_text.append(i)

print(long_text)