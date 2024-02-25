import sys
from ChatbotGui import ChatbotGUI
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    chatbotGUI = ChatbotGUI()
    chatbotGUI.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
   