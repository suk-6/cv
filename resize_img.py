import imgaug as ia
from imgaug import augmenters as iaa
from files import *
from pascal_voc_writer import Writer
from read_img import *
from xml_parsing import *

ia.seed(1)

dir = '/home/dyserver/aug/images/'
images, annotations = read_train_dataset(dir)

for idx in range(len(images)):
    image = images[idx]
    boxes = annotations[idx][0]

    ia_bounding_boxes = []
    for box in boxes:
        ia_bounding_boxes.append(ia.BoundingBox(
            x1=box[1], y1=box[2], x2=box[3], y2=box[4]))

    bbs = ia.BoundingBoxesOnImage(ia_bounding_boxes, shape=image.shape)

    seq = iaa.Sequential([
        iaa.Multiply((1.2, 1.5)),
        iaa.Affine(
            # translate_px={"x": 40, "y": 60},
            scale=(0.5, 0.7)
        )
    ])

    seq_det = seq.to_deterministic()

    image_aug = seq_det.augment_images([image])[0]
    bbs_aug = seq_det.augment_bounding_boxes([bbs])[0]

    # bounding_box
    new_image = bbs_aug.draw_on_image(image_aug, thickness=5)
    before_image = bbs.draw_on_image(image, thickness=5)

    new_image_file = dir + 'after_' + annotations[idx][2]
    before_image_file = dir + 'before_' + annotations[idx][2]
    cv2.imwrite(new_image_file, new_image)
    cv2.imwrite(before_image_file, before_image)

    h, w = np.shape(image_aug)[0:2]
    voc_writer = Writer(new_image_file, w, h)

    for i in range(len(bbs_aug.bounding_boxes)):
        bb_box = bbs_aug.bounding_boxes[i]
        voc_writer.addObject(boxes[i][0], int(bb_box.x1), int(
            bb_box.y1), int(bb_box.x2), int(bb_box.y2))

    voc_writer.save(dir + 'after_' + annotations[idx][1])
