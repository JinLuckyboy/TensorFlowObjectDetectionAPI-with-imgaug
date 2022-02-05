import imgaug.augmenters as iaa
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
from tensorflow.python.framework.ops import EagerTensor
import tensorflow as tf
import numpy as np

augseq = iaa.Sequential([
    iaa.Crop(px=(0, 16)), # crop images from each side by 0 to 16px (randomly chosen)
    iaa.Fliplr(0.5), # horizontally flip 50% of the images
    iaa.GaussianBlur(sigma=(0, 3.0)) # blur images with a sigma of 0 to 3.0
], random_order=True)
# """ <- Comment Guide
""" Debug image
every_n_batches = 1
augseq = iaa.Sequential([
    augseq,
    iaa.SaveDebugImageEveryNBatches("debug_image", every_n_batches),
])
# Debug images saved in "{command-line directory}/debug_image/" directory. You must create the directory. If not, it cause error.
# Save a debug plot to a temporary folder every 'every_n_batches' batches.
# https://imgaug.readthedocs.io/en/latest/source/overview/debug.html
"""

def augment(image, boxes, labels):
    image_np = image.numpy().astype(np.uint8) if type(image) == EagerTensor else image
    boxes_np = boxes.numpy() if type(boxes) == EagerTensor else boxes
    labels_np = labels.numpy() if type(labels) == EagerTensor else labels
    width, height, _ = image_np.shape
    bbs = []
    for i in range(len(boxes_np)):
        box = boxes_np[i]
        label = labels_np[i]
        ymin, xmin, ymax, xmax = box
        bbs.append(BoundingBox(
            x1=xmin*width, y1=ymin*height,
            x2=xmax*width, y2=ymax*height,
            label=label))
    bbs = BoundingBoxesOnImage(bbs, shape=image_np.shape)
    image_aug, bbs_aug = augseq(image=image_np, bounding_boxes=bbs) # float np.ndarray
    bbs_aug = bbs_aug.remove_out_of_image().clip_out_of_image()
    
    boxes_aug = []
    labels_aug = []
    for bb in bbs_aug:
        boxes_aug.append([bb.y1/height, bb.x1/width, bb.y2/height, bb.x2/width])
        labels_aug.append(bb.label)
    boxes_aug = np.array(boxes_aug)
    labels_aug = np.array(labels_aug)
    
    merge = np.concatenate((image_aug, boxes_aug, labels_aug), axis=None)
    return merge
