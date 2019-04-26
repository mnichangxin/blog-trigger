import compare
import convert

def posts2htmls(f_list):
    htmls = []
    try:
        for i in range(len(f_list)):
            text = convert.mdFile2Text(f_list[i])
            html = convert.mdText2html(text)
            htmls.push(html)
    except Exception as e:
        print('<Exception: %s>' % 'posts2htmls')
    return htmls