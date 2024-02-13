# app.py

import html
from flask import Flask, render_template

app = Flask(__name__)

smart_help_text = "<p><strong>Suggested questions to ask your doctor:</strong></p><p></p><ul><li>Can you explain more about the <strong>NHS breast cancer screening program</strong> and how it works?</li><li>What are the <strong>potential risks and benefits</strong> of the <strong>mammogram and needle test</strong>?</li><li>What happens if the results of the <strong>mammogram and needle test</strong> are positive?</li><li>Are there any <strong>lifestyle changes or precautions</strong> I should take while waiting for the screening appointment?</li><li>Can you recommend any <strong>resources or support groups</strong> for breast cancer patients and survivors?</li><li>What are the <strong>treatment options</strong> for breast cancer if the screening results are positive?</li><li>How long does the treatment usually take and what are the <strong>potential side effects</strong>?</li><li>Are there any <strong>alternative or complementary therapies</strong> that can be used in conjunction with conventional treatments?</li></ul>"
screening_summary_text = "<p><strong>Summary:</strong> The doctor has recommended the patient to attend the NHS breast cancer screening program or the Bupa breast cancer screening service due to the symptoms that could be of breast cancer. The screening process involves a mammogram, which is a breast X-ray, and might be uncomfortable but shouldn't hurt. The results should take about a week and the patient can talk to the mammography if they have any questions.</p><p><strong>Next key actions:</strong> The patient should attend the NHS breast cancer screening program or the Bupa breast cancer screening service. The screening process involves a mammogram, which is a breast X-ray, and might be uncomfortable but shouldn't hurt. The results should take about a week and the patient can talk to the mammography if they have any questions.</p>"

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

    return render_template('doctor_ai.html',
                           ambient_listening_text=ambient_listening_text,
                           smart_help_text=smart_help_text,
                           screening_summary_text=screening_summary_text)

if __name__ == '__main__':
    app.run(debug=True)
