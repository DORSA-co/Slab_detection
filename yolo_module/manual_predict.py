import torch
import copy
from models.common import DetectMultiBackend
from utils.torch_utils import select_device

from utils.general import non_max_suppression,scale_boxes
import numpy as np
import cv2
from utils.dataloaders import IMG_FORMATS, VID_FORMATS, LoadImages
from matplotlib import pyplot as plt



from pathlib import Path
import os
import glob
from utils.augmentations import letterbox
from ultralytics.utils.plotting import Annotator, colors, save_one_box



SHOW = False

class model:

    def __init__(self,data,conf_thres=0.25,iou_thres=0.45,weights='best_number_detection.pt',device='cpu'):
        
        self.cuda_device = device
        batch = 1
        CUDA_IDX = 0
        self.dnn=False,
        self.data = data
        self.half = False
        self.weights = weights
        self.augment=False  # augmented inference
        self.visualize=False  # visualize features

        self.conf_thres=conf_thres # confidence threshold
        self.iou_thres=iou_thres# NMS IOU threshold
        self.max_det=1000  # maximum detections per image
        self.classes=None # filter by class: --class 0, or --class 0 2 3
        self.agnostic_nms=True  # class-agnostic NMS
        self.device = select_device(self.cuda_device)
        self.yolo_model = DetectMultiBackend(self.weights, device=self.device, dnn=self.dnn, data=self.data, fp16=self.half)
        self.stride, self.names, self.pt = self.yolo_model.stride, self.yolo_model.names, self.yolo_model.pt


    def set_weight_path(self,path):
        self.weights = path
        self.set_model()


    def set_conf_iou(self,conf,iou):
        self.conf_thres = conf
        self.iou_thres = iou
        self.set_model()

    def set_model(self):
        self.yolo_model = DetectMultiBackend(self.weights, device=self.device, dnn=self.dnn, data=self.data, fp16=self.half)

    def get_names(self):
        return self.names

    def run(self,image):

        tensor_ = torch.from_numpy(image)
        tensor_ = tensor_.to(self.device) / 255

        if SHOW:
            img = tensor_.cpu().data.numpy()
            img = img[0]
            img = np.moveaxis(img, [0,1,2], [2,0,1])
            cv2.imshow('a',img)
            cv2.waitKey(0)

        pred = self.yolo_model(tensor_, augment=self.augment, visualize=self.visualize)
        predictions = non_max_suppression(pred, self.conf_thres, self.iou_thres, self.classes, self.agnostic_nms, max_det=self.max_det)
        return predictions,tensor_



    def draw(self,pred,org_image,create_image,names,save_crop=False,hide_conf=False,save_img=True,hide_labels=False):
        s=''
        # Process predictions
        im = create_image


        for i, det in enumerate(pred):  # per image
            # p, im0, frame = path, im0s.copy(), getattr(dataset, 'frame', 0)
            im0 = org_image
            # p = Path(p)  # to Path
            # save_path = str(save_dir / p.name)  # im.jpg
            # txt_path = str(save_dir / 'labels' / p.stem) + ('' if dataset.mode == 'image' else f'_{frame}')  # im.txt
            # s += '%gx%g ' % im.shape[2:]  # print string
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
            s += '%gx%g ' % im.shape[2:]  # print string

            # imc = im0.copy() if save_crop else im0  # for save_crop
            annotator = Annotator(im0, line_width=4, example=str(names))
            if len(det):
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_boxes(im.shape[2:], det[:, :4], im0.shape).round()

                # Print results
                for c in det[:, 5].unique():
                    n = (det[:, 5] == c).sum()  # detections per class
                    s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

                # Write results
                for *xyxy, conf, cls in reversed(det):
                    c = int(cls)  # integer class
                    label = names[c] if hide_conf else f'{names[c]}'
                    confidence = float(conf)
                    confidence_str = f'{confidence:.2f}'

                    # if save_csv:
                    #     write_to_csv(p.name, label, confidence_str)

                    # if save_txt:  # Write to file
                    #     xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                    #     line = (cls, *xywh, conf) if save_conf else (cls, *xywh)  # label format
                    #     with open(f'{txt_path}.txt', 'a') as f:
                    #         f.write(('%g ' * len(line)).rstrip() % line + '\n')

                    if save_img :  # Add bbox to image
                        c = int(cls)  # integer class
                        label = None if hide_labels else (names[c] if hide_conf else f'{names[c]} {conf:.2f}')
                        annotator.box_label(xyxy, label, color=colors(c, True))
                    # if save_crop:
                    #     save_one_box(xyxy, imc, file=save_dir / 'crops' / names[c] / f'{p.stem}.jpg', BGR=True)

                    im0 = annotator.result()

                    if SHOW:

                        p ='test'
                        cv2.namedWindow(str(p), cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)  # allow window resize (Linux)
                        cv2.resizeWindow(str(p), im0.shape[1], im0.shape[0])
                        cv2.imshow(str(p), im0)
                        cv2.waitKey(0)  # 1 millisecond
        return im0




    def predict(self,temp_img,draw=False,size=(640,160)):

        image_org = temp_img
        # if size:
        #     image = cv2.resize(image_org,size).astype('float32')  # should be relative
        # image = np.moveaxis(image , (0,1,2),(1,2,0))

    
        temp_img = letterbox(temp_img, (640,640), stride=32, auto=True)[0]  # padded resize
        temp_img = temp_img.transpose((2, 0, 1))[::-1]  # HWC to CHW, BGR to RGB
        temp_img = np.ascontiguousarray(temp_img)  # contiguous
        im = np.asarray([temp_img])




        output,im= self.run(im)
        








        if draw:
            image = self.draw(copy.deepcopy(output),image_org,im,self.get_names(), hide_conf=True)
        else:
            image = None

        #for det in output:
        output = output[0]
        output[:, :4] = scale_boxes(im.shape[2:], output[:, :4], image.shape).round()



        output = output.cpu().data.numpy()
        return output,image


if __name__ == '__main__':
    import sys
    sys.path.append('uiFiles')
    sys.path.append('yolo_module')
    m = model(data='yolo_module/slab.yaml',weights='yolo_module/best_number_detection.pt', iou_thres=0.1, conf_thres=0.25)
    #m.set_conf_iou(0.25,0.2)
    image_org = cv2.imread('1.png')
    pred,img = m.predict(image_org,draw=True)
    print(pred)
    cv2.imshow('a',img)
    cv2.waitKey(0)

    m = model(data='slab.yaml')
    #m.set_conf_iou(0.25,0.45)
    image_org = cv2.imread('images/2.png')
    pred,img = m.predict(image_org,draw=True)
    print(pred)
    cv2.imshow('a',img)
    cv2.waitKey(0)

    # m = model(data='slab.yaml',weights='best_slab_detection.pt')
    # m.set_conf_iou(0.25,0.3)
    # image_org = cv2.imread('2.png')
    # pred,img = m.predict(image_org,draw=True)
    # print(pred)
    # cv2.imshow('a',img)
    # cv2.waitKey(0)

    # image_org = cv2.imread('all_images/2.png')
    # pred,img = m.predict(image_org,draw=True)
    # print(pred)

    # cv2.imshow('a',img)
    # cv2.waitKey(0)