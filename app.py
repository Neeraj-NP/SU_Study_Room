from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages


# Configuration for file uploads
UPLOAD_FOLDER = 'uploads/'  # Directory where uploaded files will be stored
ALLOWED_EXTENSIONS = {'pdf'}  # Allowed file extensions
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """Check if a file is allowed based on its extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Check if a file is included in the request
        if 'file' not in request.files:
            flash('No file part in the request')
            return redirect(request.url)
        
        file = request.files['file']

        # If no file is selected
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)

        # If the file is valid, save it
        if file and allowed_file(file.filename):
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            flash('File successfully uploaded')
            return redirect(url_for('upload'))
        else:
            flash('Allowed file types are: pdf')
            return redirect(request.url)
    return render_template('upload.html')

@app.route('/exam_papers')
def exam_papers():
    return render_template('Sitare_University_Exam_Papers/find_paper.html')

@app.route('/hackathon_news')
def hackathon_news():
    return render_template('hackathon_news.html')

# @app.route('/upload')
# def upload():
#     return render_template('upload.html')

# Route for Contact Us page
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/first_year')
def first_year():
    return render_template('Sitare_University_Exam_Papers/1st_Year/index.html')

@app.route('/1st_year/internal_assessment')
def internal_assessment():
    return render_template('Sitare_University_Exam_Papers/1st_Year/Internal_Assessment/index.html')

@app.route('/1st_year/internal_assessment/linear_algebra')
def linear_algebra():
    return render_template('Sitare_University_Exam_Papers/1st_Year/Internal_Assessment/linear_algebra.html')

@app.route('/1st_year/internal_assessment/python')
def python():
    return render_template('Sitare_University_Exam_Papers/1st_Year/Internal_Assessment/python.html')

@app.route('/1st_year/internal_assessment/communication')
def communication():
    return render_template('Sitare_University_Exam_Papers/1st_Year/Internal_Assessment/communication.html')

@app.route('/1st_year/end_semester_exam')
def end_semester_exam():
    return render_template('Sitare_University_Exam_Papers/1st_Year/End_Semester_Exam/index.html')

# Route for the 2nd Year Exam Papers
@app.route('/2nd_year')
def second_year():
    return render_template('Sitare_University_Exam_Papers/2nd_Year/index.html')

# Route for the 3rd Year Exam Papers
@app.route('/3rd_year')
def third_year():
    return render_template('Sitare_University_Exam_Papers/3rd_Year/index.html')

# Route for the 4th Year Exam Papers
@app.route('/4th_year')
def fourth_year():
    return render_template('Sitare_University_Exam_Papers/4th_Year/index.html')






if __name__ == '__main__':
    app.run(debug=True)
