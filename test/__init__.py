# from flask import (
#     Flask,
#     request,
#     render_template
# )
#
# # Create the application instance
# app = Flask(__name__, template_folder="templates")
#
# # Create a URL route in our application for "/"
# @app.route('/', methods=['GET', 'POST'])
# def home():
#     """
#     This function just responds to the browser ULR
#     localhost:5000/
#
#     :return:        the rendered template 'home.html'
#     """
#
#     if request.method == 'POST':
#         return render_template('post.html')
#     else:
#         return render_template('home.html')
#         # return show_the_login_form()
#
#
# # If we're running in stand alone mode, run the application
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import render_template
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('../swagger.yml')

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('./home.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
