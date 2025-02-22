from flask import Flask, render_template, request, redirect, url_for, flash
import os
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')


# # Route to render the upload page
# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST':
#         # Fetch form data
#         exam_type = request.form.get('exam_type')
#         academic_year = request.form.get('academic_year')
#         branch = request.form.get('branch')
#         semester = request.form.get('semester')
#         subject_name = request.form.get('subject_name')
#         exam_date = request.form.get('exam_date')
#         additional_notes = request.form.get('additional_notes')
#         file = request.files.get('file')

#         # You can now process the form data or save it to a database
#         # For demonstration, just print the data to the console
#         print(f"Exam Type: {exam_type}")
#         print(f"Academic Year: {academic_year}")
#         print(f"Branch: {branch}")
#         print(f"Semester: {semester}")
#         print(f"Subject Name: {subject_name}")
#         print(f"Exam Date: {exam_date}")
#         print(f"Additional Notes: {additional_notes}")

#         # Handle file upload
#         if file:
#             file.save(f"static/uploads/{file.filename}")
#             print(f"File saved: {file.filename}")

#         return redirect(url_for('upload_success'))

#     return render_template('upload.html')

# # Success page route after upload
# @app.route('/upload-success')
# def upload_success():
#     return "Paper uploaded successfully!"


@app.route('/exam_papers')
def exam_papers():
    return render_template('Sitare_University_Exam_Papers/find_paper.html')

@app.route('/hackathon_news')
def hackathon_news():
    return render_template('hackathon_news.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

# Route for Contact Us page
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/Sitare_University_Exam_Papers/1st_year')
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


