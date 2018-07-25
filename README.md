# Geolocation Estimation of Photos using a Hierarchical Model and Scene Classification
This is the official GitHub page for the paper:

> Eric Müller-Budack, Kader Pustu-Iren, Ralph Ewerth:
"Geolocation Estimation of Photos using a Hierarchical Model and Scene Classification".
Forthcoming: *European Conference on Computer Vision (ECCV).* Munich, 2018.

# Content

This repository contains:
* Meta information for the MP-16 training dataset
([mp16_places365.csv](https://github.com/TIBHannover/GeoEstimation/releases/download/v1.0/mp16_places365.csv))
as well as the Im2GPS ([im2gps_places365.csv](meta/im2gps_places365.csv)) and
Im2GPS3k ([im2gps3k_places365.csv](meta/im2gps3k_places365.csv)) test datasets:
    - Relative image path containing the Flickr-ID
    - Flickr Author-ID
    - Ground-truth latitude
    - Ground-truth longitude
    - Predicted scene label in *S_3*
    - Predicted scene label in *S_16*
    - Predicted scene label in *S_365*
    - Probability for *S_3* concept *indoor*
    - Probability for *S_3* concept *natural*
    - Probability for *S_3* concept *urban*
* List of geographical cells for all partitionings:
    - coarse: [cells_50_1000.csv](geo-cells/cells_50_1000.csv)
    - middle: [cells_50_2000.csv](geo-cells/cells_50_2000.csv)
    - fine: [cells_50_5000.csv](geo-cells/cells_50_5000.csv)
* Results for the reported approaches on both test datasets <approach_parameters.csv>:
    - Relative image path containing the Flickr-ID
    - Ground-truth latitude
    - Predicted latitude
    - Ground-truth longitude
    - Predicted longitude
    - Great-circle distance (GCD)

# Images

The (list of) image files for training and testing can be found on the following links:
* MP-16: http://multimedia-commons.s3-website-us-west-2.amazonaws.com/
* Im2GPS: http://graphics.cs.cmu.edu/projects/im2gps/
* Im2GPS-3k: https://github.com/lugiavn/revisiting-im2gps

# Geographical Cell Partitioning

The geographical cell labels are extracted using the *S2 geometry library*:
https://code.google.com/archive/p/s2-geometry-library/

The python implementation *s2sphere* can be found on:
http://s2sphere.readthedocs.io/en/

The geographical cells can be visualized on:
http://s2.sidewalklabs.com/regioncoverer/

# Scene Classification

The scene labels and probabilities are extracted using the *Places365 ResNet 152 model* from:
https://github.com/CSAILVision/places365

In order to generate the labels for the superordinate scene categories the *Places365 hierarchy* is used:
http://places2.csail.mit.edu/download.html

# Model

All models were trained using TensorFlow

* Baseline approach for middle partitioning: TODO
* Multi-partitioning baseline approach: TODO
* Multi-partitioning Individual Scenery Network for *S_3* concept *indoor*: TODO
* Multi-partitioning Individual Scenery Network for *S_3* concept *natural*: TODO
* Multi-partitioning Individual Scenery Network for *S_3* concept *urban*: TODO

We are currently working on a deploy source code.

# LICENSE

This work is published under the GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. For details please check the
LICENSE file in the repository.
