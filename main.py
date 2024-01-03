import sys
sys.path.append('uiFiles')
sys.path.append('yolo_module')
import os
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import(
    Qt, 
    QPoint
)
from PySide6 import QtWidgets, QtCore, QtGui
from uiFiles.main_UI import Ui_MainWindow
import cv2
import numpy as np
from Mouse import MouseEvent, mouseHandeler
from yolo_module.manual_predict import model
from PIL import Image, ImageEnhance


from yolo_module.utils.augmentations import letterbox






SIDE_BUTTONS_SELECT = 'background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #3A6073, stop: 0.029 #3A6073, stop: 0.03 rgba(120, 146, 223, 40), stop: 1 rgba(120, 146, 223, 40));'
SIDE_BUTTONS_NOT_SELECT = ''
IMAGES_FORMATS = ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']

# pyside6-rcc .\uiFiles\resource.qrc -o .\uiFiles\resource_rc.py
# pyside6-uic .\uiFiles\main_UI.ui -o .\uiFiles\main_UI.py 

base_dir = os.path.dirname(os.path.abspath(__file__))

class mainUI(QMainWindow):
    x=0

    def __init__(self):
        super(mainUI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.set_window_flags()
        self.connect_top_frame_btns()
        self.connect_side_frame_btns()

        self.connect_image_page_objects()
        self.connect_drawing_page_objects()

        self.ui.stackedWidget.currentChanged.connect(self.change_side_frame_btns)

        self.state = 'draw'
        self.image_org = cv2.imread('slab.png')
        self.draw_layer = np.zeros( self.image_org.shape, dtype=np.uint8)

        self.mouse = mouseHandeler()
        self.mouse.connect_all(self.ui.drawing_label, self.draw)
        self.show_draw_image()

        QtGui.QShortcut(QtGui.QKeySequence(Qt.Key_Left), self, activated=self.keyboard_move_left)
        QtGui.QShortcut(QtGui.QKeySequence(Qt.Key_Right), self, activated=self.keyboard_move_right)

        self.images_list = []
        self.images_index = -1

        self.slabs_list = []
        self.slabs_index = -1

        self.current_image = None
        self.current_slab = None

        self.yolo_slab = model(
            data='yolo_module\\slab.yaml',
            conf_thres=0.25,
            iou_thres=0.3,
            weights='best_slab.pt',
            device='cpu'
        )

        self.yolo_ocr = model(
            data='yolo_module\\slab.yaml',
            conf_thres=0.15,
            iou_thres=0.3,
            weights='best_ocr.pt',
            device='cpu'
        )

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = QPoint(event.position().x(),event.position().y())
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == Qt.LeftButton:

            self.move(self.pos() + QPoint(event.scenePosition().x(),event.scenePosition().y()) - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

    def set_window_flags(self):
        flags = Qt.WindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlags(flags)

    def connect_top_frame_btns(self):
        self.ui.minimize_btn.clicked.connect(self.minimize)
        self.ui.maximize_btn.clicked.connect(self.maximize_minimize)
        self.ui.close_btn.clicked.connect(self.close_win)

    def connect_side_frame_btns(self):
        self.ui.side_image_btn.clicked.connect(self.show_image_page)
        self.ui.side_drawing_btn.clicked.connect(self.show_drawig_page)

    def connect_image_page_objects(self):
        self.ui.open_folder_btn.clicked.connect(self.open_folder)
        self.ui.open_file_btn.clicked.connect(self.open_file)

        self.ui.full_next_btn.clicked.connect(self.full_next_image)
        self.ui.full_prev_btn.clicked.connect(self.full_prev_image)

        self.ui.single_next_btn.clicked.connect(self.single_next_slab)
        self.ui.single_prev_btn.clicked.connect(self.single_prev_slab)

    def connect_drawing_page_objects(self):
        self.ui.drawing_clear_btn.clicked.connect(self.clear_drawing)
        self.ui.drawing_detect_btn.clicked.connect(self.detect_drawing)

    def keyboard_move_left(self):
        if self.ui.stackedWidget.currentWidget() == self.ui.image_page:
            if self.ui.tabWidget.currentWidget() == self.ui.full_view_tab:
                self.ui.full_prev_btn.click()
            elif self.ui.tabWidget.currentWidget() == self.ui.single_view_tab:
                self.ui.single_prev_btn.click()

    def keyboard_move_right(self):
        if self.ui.stackedWidget.currentWidget() == self.ui.image_page:
            if self.ui.tabWidget.currentWidget() == self.ui.full_view_tab:
                self.ui.full_next_btn.click()
            elif self.ui.tabWidget.currentWidget() == self.ui.single_view_tab:
                self.ui.single_next_btn.click()

    def minimize(self):
        self.showMinimized()
    
    def maximize_minimize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def close_win(self):
        self.close()

    def clear_drawing(self):
        self.draw_layer = np.zeros_like(self.draw_layer)
        self.show_draw_image()

    def detect_drawing(self):
        # self.images_list.insert(self.images_index + 1, self.res_draw.copy())
        # self.full_next_image()
        # self.ui.stackedWidget.setCurrentWidget(self.ui.image_page)

        self.clear_images_list()
        self.insert_image_into_list(self.res_draw.copy())
        self.full_next_image()

        self.show_image_page()

    def change_stylesheet(self, obj, style):
        obj.setStyleSheet(style)

    def show_image_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.image_page)

    def show_drawig_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.drawing_page)

    def change_side_frame_btns(self, index):
        side_btns = [self.ui.side_image_btn,
                    self.ui.side_drawing_btn
                    ]
        
        for i, btn in enumerate(side_btns):
            if i==index:
                self.change_stylesheet(btn, SIDE_BUTTONS_SELECT)
            else:
                self.change_stylesheet(btn, SIDE_BUTTONS_NOT_SELECT)

    def show_draw_image(self,):
        alpha = 0.84
        self.res_draw = cv2.addWeighted(self.image_org, alpha, self.draw_layer, 1 - alpha, gamma=0)
        # policy = self.ui.drawing_label.sizePolicy()
        # policy.setVerticalPolicy(QtWidgets.QSizePolicy.Policy.Expanding)
        # policy.setHorizontalPolicy(QtWidgets.QSizePolicy.Policy.Expanding)
        # self.ui.drawing_label.setSizePolicy(policy)

        self.draw_pixmap = self.set_label_image(self.ui.drawing_label, self.res_draw)
        #self.fit_label_to_pixmap(self.ui.drawing_label, self.draw_pixmap)
    
    def draw(self, e:MouseEvent):
        if e.is_left_btn():
            self.state = 'draw'
        elif e.is_right_btn():
            self.state = 'clean'


        if e.is_move():
            ph, pw = self.draw_pixmap.height(), self.draw_pixmap.width()
            lh, lw = self.ui.drawing_label.height(), self.ui.drawing_label.width()
            ih, iw = self.draw_layer.shape[:2]
            offset_x = int((lw - pw) / 2)
            offset_y = int((lh - ph) / 2)
            x,y = e.get_postion()
            x = int((x - offset_x) / pw * iw)
            y = int((y - offset_y) / ph * ih)
            # h,w = self.draw_layer.shape[:2]
            # x  = int(x * w)
            # y  = int(y * h)
            if self.state == 'draw':
                self.draw_layer = cv2.circle(self.draw_layer, (x,y), 5, (150,255,255), thickness=-1)
            
            elif self.state == 'clean':
                self.draw_layer = cv2.circle(self.draw_layer, (x,y), 15, (0,0,0), thickness=-1)


        self.show_draw_image()

    def set_label_image(self, lbl: QtWidgets.QLabel, image) -> QtGui.QPixmap:

        if isinstance(image, str):
            image = cv2.imread(image)        

        #resie image to fix in label
        img_h, img_w = image.shape[:2]
        lbl_h, lbl_w = lbl.height()-10, lbl.width()-10


        
        scale = min(lbl_h/img_h, lbl_w/img_w)

        image = cv2.resize(image, None, fx= scale, fy=scale)
        

        #color image
        if len(image.shape)==3:
            #alpha channel image
            if image.shape[2] ==4:
                qformat=QtGui.QImage.Format_RGBA8888
            else:
                qformat=QtGui.QImage.Format_RGB888          

        #grayscale image
        if len(image.shape) == 2:
            qformat=QtGui.QImage.Format_Grayscale8

        img = QtGui.QImage(image.data,
            image.shape[1],
            image.shape[0], 
            image.strides[0], # <--- +++
            qformat)
        
        img = img.rgbSwapped()
        pixmap = QtGui.QPixmap.fromImage(img)
        lbl.setPixmap(pixmap)
        lbl.setAlignment(QtCore.Qt.AlignCenter)

        return pixmap
    
    def fit_label_to_pixmap(self, lbl: QtWidgets.QLabel, pixmap:QtGui.QPixmap):
        lbl.setFixedSize(pixmap.size())

    def insert_image_into_list(self, image: np.ndarray):
        self.images_list.append(image)

    def clear_images_list(self):
        self.images_list = []
        self.images_index = -1

    def insert_slab_into_list(self, image: np.ndarray):
        self.slabs_list.append(image)

    def clear_slabs_list(self):
        self.slabs_list = []
        self.slabs_index = -1

    def open_file(self):
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')
        if fname:
            if os.path.splitext(fname)[-1] in IMAGES_FORMATS:
                img = cv2.imread(fname)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                self.insert_image_into_list(img)

                self.images_index = len(self.images_list) - 1
                self.show_full_image()

    def open_folder(self):
        self.clear_images_list()
        dir_path = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select Folder', '', QtWidgets.QFileDialog.ShowDirsOnly)
        if dir_path:
            fnames = os.listdir(dir_path)
            for fname in fnames:
                if os.path.splitext(fname)[-1] in IMAGES_FORMATS:
                    img = cv2.imread(os.path.join(dir_path, fname))
                    self.insert_image_into_list(img)

        self.full_next_image()
    
    def predict_slabs(self, img:np.ndarray):
        img_temp = img.copy()
        # img_temp = cv2.cvtColor(img.copy(),cv2.COLOR_BGR2RGB)        
        results, res_img = self.yolo_slab.predict(img_temp, draw=True, size=(640,544) )
        # res_img = cv2.cvtColor(res_img,cv2.COLOR_RGB2BGR)
        results_box:list = results[:,:4].astype(np.int32).tolist()
        results_box.sort(key=lambda pred:pred[1])
        border  = 10
        h,w = img.shape[:2]
        self.clear_slabs_list()
        for result in results_box:
            x1,y1,x2,y2,*other = result
            x1 = max(x1-border, 0)
            x2 = min(x2+border, w)
            y1 = max(y1-border, 0)
            y2 = min(y2+border, h)
            if abs(x2-x1) < 200 or abs(y2-y1)<80 :
                continue
            single_slab_img = img[y1:y2, x1:x2]
            self.slabs_list.append(single_slab_img)


            #---------------------------------------------------
            _, number = self.predict_ocr(single_slab_img)
            # Using cv2.putText() method 
            res_img = cv2.putText(res_img, number, (x1 + 10,int((y1 + y2)/2)), cv2.FONT_HERSHEY_SIMPLEX ,  
                            3, (0, 0, 255) , 2, cv2.LINE_AA)
            #---------------------------------------------------

        return res_img
    
    def predict_ocr(self, img:np.ndarray):
        temp_img = img.copy()
        # img_temp = cv2.cvtColor(img.copy(),cv2.COLOR_BGR2RGB)
        results, res_img = self.yolo_ocr.predict(temp_img, draw=True, size=False )
        # res_img = cv2.cvtColor(res_img,cv2.COLOR_RGB2BGR)

        results:list = results.tolist()
        results.sort(key=lambda pred:pred[0])
        numbers = list(map(lambda x:str(int(x[-1])), results))
        numbers_str = ''.join(numbers)

        return res_img, numbers_str
    
    def image_eq(self, img):
        image = Image.fromarray(img)
        enhancer = ImageEnhance.Contrast(image)
        factor = 4 # Increase the contrast by adjusting the factor (1.0 is unchanged)
        enhanced_image = enhancer.enhance(factor)

        # Convert PIL image to NumPy array
        img = np.array(enhanced_image)
        # cv2.imshow('img', img)
        # cv2.waitKey(10)
        return img
        
    def full_next_image(self):
        self.slabs_list = []
        self.slabs_index=-1

        if self.images_list:
            self.images_index+=1
            if self.images_index == len(self.images_list):
                self.images_index=0

            self.show_full_image()
            
    def full_prev_image(self):
        self.slabs_list = []
        self.slabs_index=-1

        if self.images_list:
            self.images_index-=1
            if self.images_index < 0:
                self.images_index=len(self.images_list)-1
            
            self.show_full_image()

    def show_full_image(self):
        self.current_image = self.images_list[self.images_index]

        res_img = self.predict_slabs(self.current_image)
        self.set_label_image(self.ui.full_image_label, res_img)
        self.single_next_slab()
    
    def single_next_slab(self):
        if self.slabs_list:
            self.slabs_index+=1
            if self.slabs_index == len(self.slabs_list):
                self.slabs_index=0
            
            self.show_single_slab()

    def single_prev_slab(self):
        if self.slabs_list:
            self.slabs_index-=1
            if self.slabs_index < 0:
                self.slabs_index=len(self.slabs_list)-1

            self.show_single_slab()        

    def show_single_slab(self):
        self.current_slab = self.slabs_list[self.slabs_index]
        self.set_label_image(self.ui.single_image_label, self.current_slab)

        res_img, numbers_str = self.predict_ocr(self.current_slab)
        self.ui.slab_number_lbl.setText(numbers_str)

        self.set_label_image(self.ui.single_image_label, res_img)


if __name__ == "__main__":

    # m = model(data='yolo_module/slab.yaml',weights='yolo_module/best_number_detection.pt', iou_thres=0.1, conf_thres=0.25)
    # #m.set_conf_iou(0.25,0.2)
    # image_org = cv2.imread('1.png')
    # pred,img = m.predict(image_org,draw=True)
    # print(pred)
    # cv2.imshow('a',img)
    # cv2.waitKey(0)

    app = QApplication([])
    window = mainUI()
    window.show()
    # window.showMaximized()
    app.exec()
    