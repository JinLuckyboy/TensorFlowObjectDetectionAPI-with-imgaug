# TensorFlowObjectDetectionAPI-with-imgaug

Support Language
- Korean
- English

---
Release v1.2
===
Updated to last version of tf object detection API

## INSTALLATION

1- Clone this repo

`git clone https://github.com/JinLuckyboy/TensorFlowObjectDetectionAPI-with-imgaug.git`

2- Clone tensorflow models repo

`git clone https://github.com/tensorflow/models.git`

3- Replace manually the files inside this folder repo into the Object Detection folder `models/research/object_detection` or run this file to do it automatically (both repos need to be in the same folder):

```
cd TensorFlowObjectDetectionAPI-with-imgaug
chmod +x install.sh
./install.sh
```

4- Install object detection API normally (creating the .protos first)

.proto 파일로부터 다음과 같은 명령으로 .py 파일을 생성하십시오.

```
cd ../models/research
protoc object_detection/protos/*.proto --python_out=.
cp object_detection/packages/tf2/setup.py .
python -m pip install --use-feature=2020-resolver .

# Verify installation was done correctly
python object_detection/builders/model_builder_tf2_test.py
```

You need to have imgaug installed `pip install imgaug` in order for everything to work.

If installation was sucessfull, you should get no errors and OK after finish



## HOW TO USE

---
Use augmentation
===
pipeline.config에 data_augmentation_options를 다음과 같이 설정하십시오.

Set data_augmentation_options in pipeline.config as follows (that applies for each model you are training)

```yaml
train_config: {
  data_augmentation_options {
    random_imgaug {
      random_coef: 0.0
      # random_coef: [0, 1] 사이의 숫자를 가지며, 0이면 항상 적용하고, 1이면 항상 원본 이미지를 사용합니다. 이 옵션은 선택이므로 지워도 되며, 기본값은 0.0입니다.
      # random_coef: This option have a number between [0, 1]. If it is 0, augmented image is always used. If it is 1, original image is always used. It can be deleted. default: 0.0
    }
  }
}
```

---
Add augmentation options
===
object_detection/core/imgaug_utils.py를 열어 augmentation 옵션을 수정하십시오.

Open object_detection/core/imgaug_utils.py and Edit augmentation options.

Refer to imgaug documentation to get all possible augmentation options

```python
augseq = iaa.Sequential([
    iaa.Crop(px=(0, 16)), # crop images from each side by 0 to 16px (randomly chosen)
    iaa.Fliplr(0.5), # horizontally flip 50% of the images
    iaa.GaussianBlur(sigma=(0, 3.0)) # blur images with a sigma of 0 to 3.0
    # 여기에 추가
])
```

REMEMBER!! Each time you change the augmentation options for `imgaug_utils.py` you MUST uninstall-reinstall object detection API for changes to take effect. 
You can do it yourself or use the script `./repack.sh` for simplicity.

---
참고가 될만한 사이트:

Recommanded Site:
- https://github.com/tensorflow/models/tree/master/research/object_detection
- https://github.com/aleju/imgaug
- https://imgaug.readthedocs.io/en/latest/source/overview_of_augmenters.html

---
2022년 01월 19일 github.com/tensorflow/models master브런치를 기준으로 제작되었습니다.

This is made based 2022-01-19 github.com/tensorflow/models master branch.
