# TensorFlowObjectDetectionAPI-with-imgaug

Support Language
- Korean
- English

.proto 파일로부터 다음과 같은 명령으로 .py 파일을 생성하십시오.

Create .py file from .proto file using following command.
`protoc object_detection/proto/*.proto --python_out=.`

pipeline.config에 data_augmentation_options를 다음과 같이 설정하십시오.

Set data_augmentation_options in pipeline.config as follows.
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

object_detection/core/imgaug_utils.py를 열어 augmentation 옵션을 수정하십시오.

Open object_detection/core/imgaug_utils.py and Edit augmentation options.

```python
augseq = iaa.Sequential([
    iaa.Crop(px=(0, 16)), # crop images from each side by 0 to 16px (randomly chosen)
    iaa.Fliplr(0.5), # horizontally flip 50% of the images
    iaa.GaussianBlur(sigma=(0, 3.0)) # blur images with a sigma of 0 to 3.0
    # 여기에 추가
])
```

참고가 될만한 사이트:
- https://github.com/tensorflow/models/tree/master/research/object_detection
- https://github.com/aleju/imgaug
- https://imgaug.readthedocs.io/en/latest/source/overview_of_augmenters.html

2020년 11월 7일 github.com/tensorflow/models master브런치를 기준으로 제작되었습니다.
