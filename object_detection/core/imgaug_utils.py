import imgaug.augmenters as iaa
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
from tensorflow.python.framework.ops import EagerTensor
import tensorflow as tf
import numpy as np

augseq = iaa.Sequential([
    iaa.Crop(px=(0, 16)), # crop images from each side by 0 to 16px (randomly chosen)
    iaa.Fliplr(0.5), # horizontally flip 50% of the images
    iaa.GaussianBlur(sigma=(0, 3.0)) # blur images with a sigma of 0 to 3.0
])

def augment(image, boxes, labels):
    image_np = image.numpy() if type(image) == EagerTensor else image
    boxes_np = boxes.numpy() if type(boxes) == EagerTensor else boxes
    labels_np = labels.numpy() if type(labels) == EagerTensor else labels
    width, height, _ = image_np.shape
    bbs = []
    for i in range(len(boxes_np)):
        box = boxes_np[i]
        label = labels_np[i]
        bbs.append(BoundingBox(
            x1=box[0]*width, y1=box[1]*height,
            x2=box[2]*width, y2=box[3]*height,
            label=label))
    bbs = BoundingBoxesOnImage(bbs, shape=image_np.shape)
    image_aug, bbs_aug = augseq(image=image_np, bounding_boxes=bbs) # float np.ndarray
    bbs_aug = bbs_aug.remove_out_of_image().clip_out_of_image()
    
    boxes_aug = []
    labels_aug = []
    for bb in bbs_aug:
        boxes_aug.append([bb.x1/width, bb.y1/height, bb.x2/width, bb.y2/height])
        labels_aug.append(bb.label)
    boxes_aug = np.array(boxes_aug)
    labels_aug = np.array(labels_aug)
    
    merge = np.concatenate((image_aug, boxes_aug, labels_aug), axis=None)
    return merge
