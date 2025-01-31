import markdown
import os

f = open('page.md', 'r')
md_content = f.read()
f.close()

f = open('template.html', 'r')
template = f.read().split('SPLIT')
f.close()

html_content = template[0] + markdown.markdown(md_content) + template[1]

f = open('index.html', 'w')
f.write(html_content)
f.close()

for filename in os.scandir('src'):
    f = open(filename.path, 'r')
    content = f.read()
    page_html_content = template[0] + markdown.markdown(content) + template[1]
    fn = str(filename.path)
    f.close()
    f = open("pages/" + fn[4: len(fn) - 2] + "html", 'w')
    f.write(page_html_content)
    f.close()
