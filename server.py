from flask import Flask, render_template, url_for, request, redirect
# from flask_mail import Mail
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
	# print(url_for('static', filename ='bolt.ico'))
	return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n{email},{subject},{message}')

	
# def write_to_csv(data):
# 	with open('database.csv', mode='a', newline = '') as database2:
# 		email = data["email"]
# 		subject = data["subject"]
# 		message = data["message"]
# 		# email = data['email']
# 		# subject = data['subject']
# 		# message = data['message']
# 		csv_writer = csv.writer(database2, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
# 		csv_writer.writerow([email,subject,message])




@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('/thankyou.html')
			# return None 
		except:
			return 'did not save to database'
	else:
		return 'something went wrong. Try again!'

# app = Flask(__name__)
# mail = Mail(app)

# @app.route('/contact')
# def send_email():
# 	email = data["email"]
# 	msg = Message("Hello",
# 		sender = email,
# 		recipients=["idiezag@gmail.com"])
# 	mail.send(msg)


# @app.route('/index.html')
# def home():
# 	# print(url_for('static', filename ='bolt.ico'))
# 	return render_template('index.html')

# @app.route('/about.html')
# def about():
# 	return render_template('about.html')

# @app.route('/works.html')
# def works():
# 	return render_template('works.html')

# @app.route('/work.html')
# def work():
# 	return render_template('work.html')
# # @app.route('/favicon.ico')
# # def blog():
# # 	return 'These are my thoughts on blogs'

# @app.route('/contact.html')
# def contact():
# 	# print(url_for('static', filename ='bolt.ico'))
# 	return render_template('contact.html')

# @app.route('/blog/2024/dogs')
# def blog2():
# 	return 'this is my dog'

