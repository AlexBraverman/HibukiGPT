from flask import Flask, render_template, request
import openai

app = Flask(__name__)
API_KEY = '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'
openai.api_key=API_KEY
messages = []
system_message = "answer questions"
messages.append({"role":"system","content":system_message})


@app.route('/', methods=['GET', 'POST'])
def index():
    age = None
    reply = ""
    if request.method == 'POST':
        user_input = request.form.get('age')
        if user_input.strip() != "":
            messages.clear()  # Clear previous messages
            messages.append({"role": "user", "content": user_input})

            system_message = "Your job will be to tell a heartfelt story that is around 100 words. Your story should be rated PG, with not too much violence or graphic details. Try to limit any themes that revolve around death. Here is the basic context for the story: " + user_input
            messages.append({"role": "system", "content": system_message})

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            reply = response["choices"][0]["message"]["content"]
            print(reply)
    return render_template('index.html', age=reply)


if __name__ == '__main__':
    app.run(debug=True)
    
    