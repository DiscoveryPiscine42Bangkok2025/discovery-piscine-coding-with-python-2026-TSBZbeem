import sys
if len(sys.argv) == 3:
    keyword = sys.argv[1]
    text_string = sys.argv[2]
    result = text_string.count(keyword)
    if result > 0:
        print(result)
    else:
        print("none")
else:
    print("none")
