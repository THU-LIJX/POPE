import os
import shutil
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--dataset", type=str, choices=("coco", "aokvqa", "gqa"), required=True)
parser.add_argument("--type", type=str, choices=("adversarial", "popular", "random"), required=True)
parser.add_argument("--data_dir", type=str, required=True)
args = parser.parse_args()

gt_files = [json.loads(line) for line in open(f"annotations/{args.dataset}/{args.dataset}_pope_{args.type}.json", "r")]

os.makedirs(f"images/{args.dataset}/{args.type}", exist_ok=True)

for gt_file in gt_files:
    image_src_path = f"{args.data_dir}/{gt_file['image']}"
    image_dst_path = f"images/{args.dataset}/{args.type}/{gt_file['image']}"
    try:
        shutil.copy2(image_src_path, image_dst_path)
        print(f"Copied: {image_src_path} -> {image_dst_path}")
    except FileNotFoundError:
        print(f"File not found: {image_src_path}")
        raise FileNotFoundError(f"File not found: {image_src_path}")
