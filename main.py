import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit

class ChatbotGUI(QWidget):
    def __init__(self): 
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.chatDisplay = QTextEdit()
        self.chatDisplay.setReadOnly(True)
        self.layout.addWidget(self.chatDisplay)

        self.messageInput = QLineEdit()
        self.messageInput.setPlaceholderText("Type your message here...")
        self.layout.addWidget(self.messageInput)

        self.sendButton = QPushButton("Send")
        self.sendButton.clicked.connect(self.sendMessage)
        self.layout.addWidget(self.sendButton)

        self.setLayout(self.layout)
        self.setWindowTitle("Chatbot")

    def sendMessage(self):
        userMessage = self.messageInput.text()
        if userMessage:
            self.chatDisplay.append("You: " + userMessage)

            botResponse = self.generateResponse(userMessage)
            self.chatDisplay.append("Bot: " + botResponse)

            self.messageInput.clear()

    def generateResponse(self, userMessage):
        return "This is a placeholder response for now"
    

def main():
    app = QApplication(sys.argv)
    chatbotGUI = ChatbotGUI()
    chatbotGUI.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
    

