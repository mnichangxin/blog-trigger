import os, codecs
import markdown

def mdFile2Text(path):
    f = codecs.open(os.path.dirname(__file__) + '../posts/test.md', mode='r', encoding='utf-8')
    text = f.read()
    f.close()
    return text

def mdText2html(text):
    f = codecs.open(os.path.dirname(__file__) + '../posts/test.md', mode='r', encoding='utf-8')
    text = f.read()
    f.close()

    html = markdown.markdown(text, extensions=['meta'], output_format='html5')

    print(html)

    return html