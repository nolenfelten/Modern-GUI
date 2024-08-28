import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Browser Widget")
        self.setGeometry(100, 100, 800, 600)
        self.browser = QWebEngineView()
        html_content = """
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Nolen James Felten</title>
            <style>
                .cube-container {
                    display: inline-block;
                    width: 20vw;
                    height: 20vw;
                    perspective: 800px;
                    position: relative;
                    transform: translate(50px, 50px);
                }
                .cube {
                    width: 100%;
                    height: 100%;
                    position: absolute;
                    top: 0;
                    left: 0;
                    transform-style: preserve-3d;
                    animation: rotateCube 10s linear infinite;
                }
                .face {
                    position: absolute;
                    width: 100%;
                    height: 100%;
                    border: 0.25vw solid rgba(125, 195, 25, 0.972);
                    box-sizing: border-box;
                }
                .face1 { background-color: rgba(255, 0, 20, 0.8); transform: rotateY(0deg) translateZ(10vw); }
                .face2 { background-color: rgba(30, 255, 0, 0.8); transform: rotateY(90deg) translateZ(10vw); }
                .face3 { background-color: rgba(0, 0, 0, 0.8); transform: rotateY(180deg) translateZ(10vw); }
                .face4 { background-color: rgba(240, 205, 205, 0.8); transform: rotateY(-90deg) translateZ(10vw); }
                .face5 { background-color: rgba(0, 0, 255, 0.8); transform: rotateX(90deg) translateZ(10vw); }
                .face6 { background-color: rgba(86, 26, 139, 0.8); transform: rotateX(-90deg) translateZ(10vw); }
                @keyframes rotateCube {
                    0% { transform: rotateX(0deg) rotateY(0deg); }
                    100% { transform: rotateX(360deg) rotateY(360deg); }
                }
            </style>
        </head>
        <body>
            <div class="cube-container">
                <div class="cube">
                    <div class="face face1"></div>
                    <div class="face face2"></div>
                    <div class="face face3"></div>
                    <div class="face face4"></div>
                    <div class="face face5"></div>
                    <div class="face face6"></div>
                </div>
            </div>
        </body>
        </html>
        """
        self.browser.setHtml(html_content)
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
