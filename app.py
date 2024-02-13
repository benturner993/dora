# app.py

import html
from flask import Flask, render_template

app = Flask(__name__)

def read_transcription():
    try:
        with open('audio_transcription.txt', 'r') as file:
            transcription = file.read()
            # Replace HTML-encoded characters manually
            transcription = transcription.replace('&#39;', "'")
            return transcription
    except FileNotFoundError:
        return "Transcription not available"

def format_html_list(items):
    html = "<ul>\n"
    for item in items:
        html += f"<li>{item}</li>\n"
    html += "</ul>"
    return html

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule-appointment')
def schedule_appointment():
    return render_template('schedule_appointment.html')

@app.route('/find-out-more')
def find_out_more():
    return render_template('find_out_more.html')

@app.route('/doctor-ai')
def doctor_ai():
    ambient_listening_text = read_transcription()
    smart_help_text = "<ul><li>Advice 1</li><li>Advice 2</li><li>Advice 3</li></ul>"
    screening_summary_text = smart_help_text
    #screening_summary_text = format_html_list(["Screening Item 1", "Screening Item 2", "Screening Item 3"])
    return render_template('doctor_ai.html',
                           ambient_listening_text=ambient_listening_text,
                           smart_help_text=smart_help_text,
                           screening_summary_text=screening_summary_text)

if __name__ == '__main__':
    app.run(debug=True)
