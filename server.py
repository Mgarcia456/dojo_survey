from flask import Flask, render_template, request, redirect # added request
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

#    this rouyte is when u post alll trhe info in the survey
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    email_from_form = request.form['email']
    return render_template("show.html", name_on_template=name_from_form, email_on_template=email_from_form)

#    tghis route is for the results to be shown /userrname/ location/ language/ comment
@app.route('/result', methods=['POST'])
def process():
    print('processing')
    username = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    if request.form.get('gender'):
        gender = request.form['gender']
    else:
      #    if none is checked it will display no reply
        gender = "No Reply"
#       checkbox for subcribe to newsletter if its clicked it will be on actuvated to show
#       in the rsults page if not clciked it wont show anytext regarding the newsletter
    if request.form.get('newsletter'):
        # newsletter = request.form['newsletter']
        newsletter = request.form.get('newsletter')
        #   yes newsletter
        return render_template("result.html", nameTemp = username, locationTemp = location, languageTemp = language, commentTemp = comment, newsletterTemp = newsletter, genderTemp = gender)
    else:
      #   no newsletter
        return render_template("result.html", nameTemp = username, locationTemp = location, languageTemp = language, commentTemp = comment, genderTemp = gender)







if __name__ == "__main__":
    app.run(debug=True)