import openai
from sk import my_sk
openai.api_key = my_sk


def generateResponse(self, userMessage):
    self.chatDisplay.append('')
    stream = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[{"role": "user", "content": userMessage}],
        stream=True,
    )

    message = ''

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            message += chunk.choices[0].delta.content
    
    self.chatDisplay.append(f'Bot: {message}')
    self.chatDisplay.append('')

