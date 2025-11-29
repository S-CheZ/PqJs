import os
import sys
import argparse
from PySide6.QtCore import QTimer, QCoreApplication
from PySide6.QtWebEngineCore import QWebEnginePage,QWebEngineSettings
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow, QLabel, QPushButton


class ConsoleWebEnginePage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.console_messages = []
    
    def javaScriptConsoleMessage(self, level, message, line_number, source_id):
        """重写此方法以捕获JavaScript控制台消息"""
        level_str = {
            QWebEnginePage.JavaScriptConsoleMessageLevel.InfoMessageLevel: "INFO",
            # QWebEnginePage.JavaScriptConsoleMessageLevel.WarningMessageLevel: "WARNING",
            # QWebEnginePage.JavaScriptConsoleMessageLevel.ErrorMessageLevel: "ERROR"
        }.get(level, "UNKNOWN")
        
        console_msg = message
        self.console_messages.append(console_msg)

        super().javaScriptConsoleMessage(level, message, line_number, source_id)


class JSInjector(QWebEngineView):
    def __init__(self, js_to_inject,url=""):
        super().__init__()
        
        # 使用自定义的WebEnginePage来捕获控制台输出
        self.page_instance = ConsoleWebEnginePage(self)
        self.setPage(self.page_instance)
        


        # 启用 localStorage 和相关设置
        settings = self.page().settings()
        settings.setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        settings.setAttribute(QWebEngineSettings.JavascriptCanOpenWindows, True)
        settings.setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
        settings.setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)

        self.html_content = html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title></title>
            </head>
            <body>
            </body>
            </html>
        """
        self.js_to_inject = js_to_inject
        self.page().loadFinished.connect(self.on_load_finished)
        
        if url=="":
            self.setHtml(self.html_content)
        else:
            self.page().load(url)
        
    def on_load_finished(self, ok):
        if ok:
            QTimer.singleShot(500, self.inject_js)
        else:
            QCoreApplication.quit()
            
    def inject_js(self):
        self.page().runJavaScript(self.js_to_inject, self.on_js_executed)
        
    def on_js_executed(self, result):
        
        QTimer.singleShot(100, self.show_console_output)
        
    def show_console_output(self):
        print("---sig---")
        if self.page_instance.console_messages:
            for i, msg in enumerate(self.page_instance.console_messages, 1):
                print(msg)

        QCoreApplication.quit()
        
       
class webView(QWidget):
    def __init__(self,injector):
        super(webView, self).__init__()

        self.layout = QVBoxLayout(self)
        self.injector=injector
        # 创建按钮来打开开发者工具
        self.dev_tools_button = QPushButton("打开开发者工具")
        self.dev_tools_button.clicked.connect(self.open_dev_tools)
        self.layout.addWidget(self.dev_tools_button)
        
        self.dev_tools_window=None

        self.layout.addWidget(injector)

    def open_dev_tools(self):
        # 如果开发者工具窗口不存在，创建它
        if not self.dev_tools_window:
            from PySide6.QtWebEngineWidgets import QWebEngineView
            self.dev_tools_window = QWebEngineView()
            self.dev_tools_window.setWindowTitle("开发者工具")
            self.injector.page().setDevToolsPage(self.dev_tools_window.page())
        
        self.dev_tools_window.show()
        self.dev_tools_window.activateWindow()
if __name__ == "__main__":
    os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--ignore-gpu-blocklist --enable-webgl --enable-accelerated-2d-canvas"

   
     # 创建解析器
    parser = argparse.ArgumentParser(description='')
    
    # 添加位置参数（必需参数）
    parser.add_argument('input_file', help='js文件路径')


    # 添加位置参数（必需参数）
    parser.add_argument('-url', help='目标网站',default="")
    
    
    # 解析参数
    args = parser.parse_args()

    app = QApplication(sys.argv)
    print(args.input_file)
    # javascript = open(args.input_file,"r+",encoding="utf-8").read()
    javascript = open(args.input_file,"r+",encoding="utf-8").read()
    
    # 创建注入器实例
    injector = JSInjector(javascript,args.url)
    
    sys.exit(app.exec())