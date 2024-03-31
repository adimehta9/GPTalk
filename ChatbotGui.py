from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit
from chatbotLogic import generateResponse

class ChatbotGUI(QWidget):
    def __init__(self): 
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setMinimumWidth(1000)
        self.setMinimumHeight(800)

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

    def keyPressEvent(self, e):
        if e.key()  == Qt.Key_Return or e.key() == Qt.Key_Enter:
            self.sendMessage()
        else:
            super().keyPressEvent(e)
            
    def sendMessage(self):
        userMessage = self.messageInput.text()
        if userMessage:
            self.chatDisplay.append("You: " + userMessage)

            generateResponse(self, userMessage)

            self.messageInput.clear()

    
    

 

