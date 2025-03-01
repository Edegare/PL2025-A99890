import sys
import re

def converter(lines):
    html = []
    inside_list = False  
    
    for line in lines:
        line = line.strip()

        # head
        if re.match(r'#{1,3} ', line):
            level = line.count('#')
            content = line[level:].strip()
            html.append(f'<h{level}>{content}</h{level}>')
            continue

        # bold
        line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)

        # italic
        line = re.sub(r'(?<!\*)\*(.*?)\*(?!\*)', r'<i>\1</i>', line)

        # image
        line = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', line)

        # link
        line = re.sub(r'(?<!!)\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', line)

        # ordered list
        if re.match(r'\d+\.', line):
            if not inside_list:
                html.append('<ol>')
                inside_list = True
            html.append(f'<li>{line[3:].strip()}</li>')
            continue
        elif inside_list:
            html.append('</ol>')
            inside_list = False

        html.append(line)

   
    if inside_list:
        html.append('</ol>')

    return '\n'.join(html)

if __name__ == "__main__":
    lines = []
    for line in sys.stdin:
        lines.append(line)
    print(converter(lines))


    