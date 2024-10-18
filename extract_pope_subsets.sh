#!/bin/bash
coco_images_dir=$1
gqa_images_dir=$2

python extract_pope_subsets.py --dataset coco --type adversarial --data_dir $coco_images_dir

python extract_pope_subsets.py --dataset coco --type popular --data_dir $coco_images_dir

python extract_pope_subsets.py --dataset coco --type random --data_dir $coco_images_dir

python extract_pope_subsets.py --dataset aokvqa --type adversarial --data_dir $coco_images_dir

python extract_pope_subsets.py --dataset aokvqa --type popular --data_dir $coco_images_dir

python extract_pope_subsets.py --dataset aokvqa --type random --data_dir $coco_images_dir

python extract_pope_subsets.py --dataset gqa --type random --data_dir $gqa_images_dir

python extract_pope_subsets.py --dataset gqa --type popular --data_dir $gqa_images_dir

python extract_pope_subsets.py --dataset gqa --type adversarial --data_dir $gqa_images_dir
