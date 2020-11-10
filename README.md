# TensorFlowObjectDetectionAPI-with-imgaug

.proto 파일은 다음과 같은 명령으로 .py 파일을 생성하십시오.

`protoc object_detection/proto/*.proto --python_out=.`

pipeline.config에 data_augmentation_options를 다음과 같이 설정하십시오.
```
train_config: {
  data_augmentation_options {
    random_imgaug {
    }
  }
}
```

object_detecton/core/imgaug_utils.py를 열어 augmentation 옵션을 수정하십시오.
```
augseq = iaa.Sequential([
    iaa.Crop(px=(0, 16)), # crop images from each side by 0 to 16px (randomly chosen)
    iaa.Fliplr(0.5), # horizontally flip 50% of the images
    iaa.GaussianBlur(sigma=(0, 3.0)) # blur images with a sigma of 0 to 3.0
    # 여기에 추가
])
```
