
# PolluVision

Visual pollution negatively impacts urban aesthetics and cleanliness, with inadequate regulations, enforcement mechanisms, and awareness campaigns contributing to its persistence. Effective strategies are needed to reduce pollution and enhance street aesthetics in Saudi Arabia.

In PolluVision Artificial intelligence is used to analyze images, identify visual pollution, determine its location, and classify it in terms of its presence or absence. This is in support of the 2030 vision of the Kingdom of Saudi Arabia, developing cities, sustainability, and improving the cultural appearance.


## Dataset

Data name: Urban Visual Pollution Dataset
- The data was obtained from Kaggle.
- Visual Pollution data were specifically obtained from the Kingdom of Saudi Arabia roads.

Source: [![Kaggle]](https://www.kaggle.com/datasets/abhranta/urban-visual-pollution-dataset)

You can access the data after correcting the annotations and labels here:
[![Roboflow]](https://app.roboflow.com/sdaia-xqoon/capstone-avmph/8)


## Model

Using yolov8m to detect pollution in images Training YOLOv8m on the dataset with args: 
- epochs = 100
- image size = 640x640
- conf = 0.45
- iou = 0.4

## Demo
![](https://github.com/BatolG/PolluVision-T5/blob/8ba6082910e9f739737b38a3910d00711e90421b/36402206-b53c-4771-ac95-a00d98d56226.mov)

## Team Members
- Batool Alghamdi
- Abeer Alharbi
- Rawabi Algethami
- Nouf Aldawsari
- Arjwan Alqarni


