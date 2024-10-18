# Data extracted from COCO2014 and GQA for POPE

This repository contains the data extracted from [COCO2014](https://cocodataset.org/#download) and [GQA](https://cs.stanford.edu/people/dorarad/gqa/download.html) for [POPE](https://arxiv.org/abs/2305.10355) to facilitate the research on POPE. For more details about the POPE dataset, please refer to the [official repository](https://github.com/AoiDragon/POPE).

The data is organized as follows:

```
POPE/
    images/
        coco/
            random/
            popular/
            adversarial/
        gqa/
            random/
            popular/
            adversarial/
        gqa/
            random/
            popular/
            adversarial/
    annotations/
        coco/
            coco_pope_random.json
            coco_pope_popular.json
            coco_pope_adversarial.json
        aokvqa/
            aokvqa_pope_random.json
            aokvqa_pope_popular.json
            aokvqa_pope_adversarial.json
        gqa/
            gqa_pope_random.json
            gqa_pope_popular.json
            gqa_pope_adversarial.json
```

## Data Extraction

We also provide the codes and scripts to extract the images subsets from COCO2014 and GQA for POPE.

```
cd POPE
bash extract_pope_subsets.sh $coco_images_dir $gqa_images_dir
```

and the images will be saved in `POPE/images/`.

## License

The repository is licensed under the [MIT License](LICENSE).
