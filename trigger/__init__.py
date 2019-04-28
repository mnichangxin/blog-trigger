from flask import Flask

# import compare
# import convert

# def posts2htmls(f_list):
#     htmls = []
#     try:
#         for i in range(len(f_list)):
#             text = convert.mdFile2Text(f_list[i])
#             html = convert.mdText2html(text)
#             htmls.push(html)
#     except Exception as e:
#         print('<Exception: %s>' % 'posts2htmls')
#     return htmls

def create_app():
    app = Flask(__name__)
    
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    from .api.hooks import hooks as api_hooks_blueprint
    app.register_blueprint(api_hooks_blueprint, url_prefix='/api/v1/hooks')

    return app