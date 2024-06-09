# My simple NotePad
#==========================================================
def break_lines(text):
    lines = []
    while len(text) > 0:
        if len(text) <= 50:
            lines.append(text)
            text = ""
        else:
            line = text[:50]
            space_index = line.rfind(" ")
            if space_index == -1:
                space_index = 50
            lines.append(text[:space_index])
            text = text[space_index+1:]
    return "\n".join(lines)

x = "c:/Users/iTakpc/Desktop/NotePad.txt"

with open(x, 'w') as f:
    print("\t<<<You can Enter your text below>>>\n ")
    try:
        text = input("===> ")
        lines = break_lines(text)
        f.write(lines)
        f.flush()
        f.close()
    except Exception as e:
            print("Error", str(e))
#==========================================================