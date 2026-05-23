from flask import Flask, request, jsonify
import requests, os

app = Flask(__name__)
GEMINI_KEY = os.environ.get("GEMINI_KEY")

@app.route('/bagley', methods=['POST'])
def bagley():
    pergunta = request.json.get('pergunta', '')
    if not GEMINI_KEY:
        return jsonify({"resposta": "Esqueci a chave do Gemini no Render"})
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={GEMINI_KEY}"
    payload = {"contents": [{"parts": [{"text": f"Você é Bagley de Luziânia. Sarcástico, direto, responde em 1 frase curta. Pergunta: {pergunta}"}]}]}
    try:
        r = requests.post(url, json=payload, timeout=10)
        resposta = r.json()['candidates'][0]['content']['parts'][0]['text'].strip()
    except Exception as e:
        resposta = "Render dormiu. Manda de novo pra acordar."
    return jsonify({"resposta": resposta})

@app.route('/')
def home():
    return "Bagley Online - Render"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
