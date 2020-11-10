import imgaug.augmenters as iaa
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
from tensorflow.python.framework.ops import EagerTensor
import tensorflow as tf
import numpy as np

# import imgaug as ia
# from matplotlib import pyplot as plt
# import os.path
augseq = iaa.Sequential([
    iaa.Crop(px=(0, 16)), # crop images from each side by 0 to 16px (randomly chosen)
    iaa.Fliplr(0.5), # horizontally flip 50% of the images
    iaa.GaussianBlur(sigma=(0, 3.0)) # blur images with a sigma of 0 to 3.0
])

def augment(image, boxes, labels):
    # print("==========image.name(augment)", image.name)
    # print("==========boxes", boxes)
    # print("==========labels", labels)
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
    
    # image_aug = image_aug.astype(np.uint8)
    # print(image_aug)
    # print(type(image_aug))
    # if type(image_aug) == np.ndarray:
        # i = 0
        # file = f"output/output-{i}.jpg"
        # while os.path.isfile(file):
            # i += 1
            # file = f"output/output-{i}.jpg"
        # np.save(f"output/output{i}", image_aug)
        # ia.imshow(image_aug)
        # print(image_aug/255)
        # plt.imshow(image_aug/255)
        # plt.savefig(file)
    # else:
        # print(image_aug)
        # print(type(image_aug))
        # print("===============\n"*10)
    
    # image_aug = image_aug.astype(np.uint8)
    
    # image_aug = image_aug.reshape(-1)
    # boxes_aug = boxes_aug.reshape(-1)
    # labels_aug = labels_aug.reshape(-1)
    
    merge = np.concatenate((image_aug, boxes_aug, labels_aug), axis=None)
    return merge
    
    # im = tf.get_default_graph().get_tensor_by_name("Squeeze_3:0")
    # print(im)
    # tf.assign(image, image_aug)
    # tf.assign(boxes, boxes_aug)
    # tf.assign(labels, labels_aug)
    # return 0
    
    # image_aug = image_aug.astype(np.float32)
    # boxes_aug = boxes_aug.astype(np.float32)
    # labels_aug = labels_aug.astype(np.int32)
    
    # image_aug = [int(i) for i in image_aug.tobytes()]
    # boxes_aug = [int(i) for i in boxes_aug.tobytes()]
    # labels_aug = [int(i) for i in labels_aug.tobytes()]
    
    # dataset = tf.data.Dataset.from_tensor_slices([image_aug, boxes_aug, labels_aug])
    
    # print(f"image {image}{image.shape}/{image_aug}{image_aug.shape}")
    # print(f"boxes {boxes}{boxes.shape}/{boxes_aug}{np.shape(boxes_aug)}")
    # print(f"labels {labels}{labels.shape}/{labels_aug}{np.shape(labels_aug)}")
    # print(f"[image_aug, boxes_aug, labels_aug] {[image_aug, boxes_aug, labels_aug]}")
    # print(f"[image, boxes, labels] {[image, boxes, labels]}")
    # return [(image_aug + b'\xff' + boxes_aug + b'\xff' + labels_aug)]
    # return {image: image_aug, boxes: boxes_aug, labels: labels_aug}
    # return [(image, boxes, labels)]
    # return (image, boxes, labels)
    # return dataset

def test(image, boxes, labels, dataset):
    # image = np.frombuffer(bytes(image), dtype=np.float32)
    # boxes = np.frombuffer(bytes(boxes), dtype=np.float32)
    # labels = np.frombuffer(bytes(labels), dtype=np.int32)
    print(f"image: {image} {image.shape}")
    print(f"boxes: {boxes}{boxes.shape}")
    print(f"labels: {labels}{labels.shape}")
    # print(f"result: {result}{result.shape}")
    
