# Created and maintained by: Minedient
# GPL-3.0 License

import math
import sys, os
from PySide6.QtWidgets import QMessageBox, QApplication, QMainWindow, QFileDialog, QLabel, QDialog, QVBoxLayout, QComboBox, QDialogButtonBox
from PySide6.QtCore import Slot, QTimer
from ultralytics import YOLO
from gui import Ui_MainDialog

# Serial communication related libraries
import serial
import serial.tools.list_ports as list_ports

import cv2
import logging

# Set up logger
logging.basicConfig(level=logging.INFO)

# Disable ultralytics logging
logging.getLogger('ultralytics').setLevel(logging.ERROR)

# Constants
PID_MICROBIT = 516
VID_MICROBIT = 3368
TIMEOUT = 1.0
CONDITIONALS = {
    0: lambda x, y: x > y,
    1: lambda x, y: x >= y,
    2: lambda x, y: x == y,
    3: lambda x, y: x != y,
    4: lambda x, y: x < y,
    5: lambda x, y: x <= y
}
CAM_INDEX = 0 # Default camera index

# Global variables
model = None
end_capture = False
ser = None
# The following are QT components that will be initialized in the main function
runtimelog = None
connnectButton= None

# Function to find the port for the micro:bit
def find_port(pid, vid, baud):
    port = serial.Serial(timeout=TIMEOUT)
    port.baudrate = baud
    ports = list(list_ports.comports())
    logging.info("搜尋Micro:bit中...")
    for p in ports:
        logging.info('Port: {}'.format(p))
        try:
            logging.info('PID: {} VID: {}'.format(p.pid, p.vid))
        except AttributeError:
            continue
        if (p.pid == pid) and (p.vid == vid):
            print('找到目標 PID: {} VID: {} Port: {}'.format(
                p.pid, p.vid, p.device))
            port.port = str(p.device)
            return port
    return None

def draw_box(frame, box, names):
    x1, y1, x2, y2 = box.xyxy[0]
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values
    confidence = math.ceil((box.conf[0]*100))/100
    label = names[int(box.cls)]
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)
    y = y1 - 15 if y1 - 15 > 15 else y1 + 15
    cv2.putText(frame, f"{label}: {confidence:.2f}", (x1, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Get the label counts from the results (all)
def get_label_counts(results, frame):
    label_counts = {}
    for result in results:
        boxes = result.boxes
        for box in boxes:
            # if confidence is less than 0.5, ignore the box
            if box.conf[0] < 0.5:
                continue

            # Draw bounding boxes
            draw_box(frame, box, model.names)

            # Get the label name
            label = model.names[int(box.cls)]
            if label in label_counts:
                label_counts[label] += 1
            else:
                label_counts[label] = 1
    return label_counts
    
def counter_logic(type1Counter, type2Counter):
    r1 = window.ui.relationComboBox.currentIndex()
    r2 = window.ui.relationComboBox_2.currentIndex()
    n1 = window.ui.numberSpinBox.value()
    n2 = window.ui.numberSpinBox_2.value()
    l = window.ui.logicComboBox.currentIndex()

    #logging.info("Type 1 Counter: {}, Type 2 Counter: {}".format(type1Counter, type2Counter))
    type1Result = CONDITIONALS.get(r1, lambda x, y: False)(type1Counter, n1)

    #logging.info("Type 1: {}, Relation 1: {}, Number 1: {}, Logic: {}, Type 2: {}, Relation 2: {}, Number 2: {}".format(t1, r1, n1, l, t2, r2, n2))
    if l == 0:
        return type1Result
    else:
        type2Result = CONDITIONALS.get(r2, lambda x, y: False)(type2Counter, n2)
        return type1Result or type2Result if l == 1 else type1Result and type2Result

def list_available_cameras():
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    return arr

def prepare_and_send_command_text(text, type1, type2, color):
    text = text.replace("%1", str(type1)).replace("%2", str(type2))
    window.ui.label_7.setText('發送指令：{}'.format(text))
    window.ui.label_7.setStyleSheet("color: {}".format(color))
    ser.write(str(text).encode())

@Slot()
def on_loadModelButton_clicked():
    global model
    # Open a file dialog to select the model file
    model_file, _ = QFileDialog.getOpenFileName(
        None, "選擇模型文件", "", "Model Files (*.pt)"
    )
    if model_file:
        logging.info(f"已選擇模型: {model_file}")
        # Load the model
        model = YOLO(model_file)
        logging.info("正在嘗試加載模型……")
        # Update the label
        window.ui.modelLabel.setText(f'已加載模型：{os.path.basename(model_file)}')

        # Extract Model Informations
        names = model.names

        # Clear previous items
        window.ui.typeComboBox.clear()
        window.ui.typeComboBox_2.clear()

        # Add the model names to the combobox for selection
        for name in names.values():
            window.ui.typeComboBox.addItem(name)
            window.ui.typeComboBox_2.addItem(name)
        
        window.ui.typeComboBox.setCurrentIndex(0)
        window.ui.typeComboBox_2.setCurrentIndex(0)
        
        logging.info("模型標籤已加載到組合框中。")
    else:
        logging.info("沒有選擇模型")

@Slot()
def start_detection():
    global model, end_capture, ser
    if model is None or ser is None:
        error_message = "請先加載模型！" if model is None else "請先連接到micro:bit！"
        logging.error(error_message)
        # Show a message box
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(error_message)
        msg.setWindowTitle("提示")
        msg.exec()
        return
    
    logging.info("初始化中……請稍候……")
    
    # Reset the flag
    end_capture = False

    cap = cv2.VideoCapture(CAM_INDEX)
    
    if not cap.isOpened():
        logging.error("無法打開選擇的攝像頭設備")
        return
    
    logging.info("開始收集數據")

    old1, old2 = 0, 0

    while not end_capture:
        ret, frame = cap.read()
        if not ret:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Error)
            msg.setText("讀取幀時出錯！")
            msg.setWindowTitle("錯誤")
            msg.exec()
            logging.error("讀取幀時出錯！")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = model(rgb_frame)

        label_counts = get_label_counts(results, frame)
        type1Counter, type2Counter = label_counts.get(window.ui.typeComboBox.currentText(), 0), label_counts.get(window.ui.typeComboBox_2.currentText(), 0)

        if type1Counter != old1 or type2Counter != old2:
            # Only update if either of the counters have changed
            if counter_logic(type1Counter, type2Counter):
                # Send a signal here
                prepare_and_send_command_text(window.ui.lineEdit.text(), type1Counter, type2Counter, "green")
                #logging.info("符合條件，將會發送指令：{} 到micro:bit".format(command_text))

                # Send the command to the micro:bit
            elif window.ui.hasNegate.isChecked():
                #Get the command of the else condition
                prepare_and_send_command_text(window.ui.lineEdit_2.text(), type1Counter, type2Counter, "red")
                #logging.info("符合else條件，將會發送指令：{} 到micro:bit".format(command_text))
            old1, old2 = type1Counter, type2Counter


        cv2.imshow('Video captured', frame)
    
        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    logging.info("停止收集數據")

    ser.write('0'.encode())

    # Release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()   

@Slot()
def on_stopButton_clicked():
    global end_capture
    end_capture = True

@Slot()
def on_connectButton_clicked():
    global ser
    ser = find_port(PID_MICROBIT, VID_MICROBIT, 115200)
    if ser is None:
        logging.error("無法找到目標設備，請確保micro:bit已連接到電腦或試一個新的micro:bit。")
        return
    else:
        # Terminate the connection and re-enstablish it
        logging.info("正在重新連接到目標設備……")
        ser.close()
    ser.open()
    ser.write('0'.encode())
    logging.info("已連接到目標設備")

@Slot()
def on_manualButton_clicked():
    if ser is None:
        logging.error("請先把電腦連接到micro:bit！")
        return
    command_text = window.ui.lineEdit.text()
    ser.write(str(command_text).encode())
    logging.info("已發送手動指令：{}".format(command_text))

# Custom logger class to log to the text browser
class TextBrowserLogger(logging.Handler):
    def __init__(self, textBrowser):
        super(TextBrowserLogger, self).__init__()
        self.textBrowser = textBrowser

    def emit(self, record):
        self.textBrowser.append(self.format(record))

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainDialog()
        self.ui.setupUi(self)

        # Add a logger to the text browser
        logger = TextBrowserLogger(self.ui.runtimeLogger)
        logging.getLogger().addHandler(logger)

        # Connect the button to the slot
        self.ui.loadModelButton.clicked.connect(on_loadModelButton_clicked)
        self.ui.startButton.clicked.connect(start_detection)
        self.ui.stopButton.clicked.connect(on_stopButton_clicked)
        self.ui.connectButton.clicked.connect(on_connectButton_clicked)
        self.ui.manualButton.clicked.connect(on_manualButton_clicked)

        # Detect enter key press in the line edit
        self.ui.lineEdit.returnPressed.connect(on_manualButton_clicked)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    # Initialize the QT components here
    runtimelog = window.ui.runtimeLogger
    connnectButton = window.ui.connectButton

    # Show the window
    window.show()

    logging.info("歡迎使用物品偵測模型與micro:bit連結器！")
    logging.info("請先加載模型，然後點擊開始按鈕開始偵測。")
    logging.info("在開始之前，請確保micro:bit已連接到電腦，並按下\"連接到micro:bit\"按鈕。")
    logging.info("您可以在下方設置條件，當條件符合時，將會發送指令到micro:bit。")
    logging.info("請在micro:bit上加載對應的程式，方能正確解析指令。")

    sys.exit(app.exec())