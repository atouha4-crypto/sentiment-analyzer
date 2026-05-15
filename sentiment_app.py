
import gradio as gr
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def analyze(text):
    if not text.strip():
        return "الرجاء كتابة نص"
    result = classifier(text)[0]
    stars = int(float(result['label'].split()[0]))
    if stars >= 4:
        feeling = "😊 إيجابي"
    elif stars == 3:
        feeling = "😐 محايد"
    else:
        feeling = "😞 سلبي"
    return f"{feeling} ({stars}/5)"

gr.Interface(fn=analyze, inputs="text", outputs="text", 
             title="كاشف المشاعر",
             description="يدعم العربية والإنجليزية").launch()
