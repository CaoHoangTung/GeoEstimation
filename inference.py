import argparse
import logging
import os
import sys

# own imports
import scene_classification
import geo_estimation

# VARIABLES
cur_path = os.path.abspath(os.path.dirname(__file__))


def parse_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-v', '--verbose', action='store_true', help='verbose output')
    parser.add_argument('-i', '--image', type=str, required=True, help='path to image file')
    parser.add_argument(
        '-m',
        '--model',
        type=str,
        default='ISN',
        choices=['ISN', 'base_L', 'base_M'],
        help='Choose from [ISN, base_L, base_M]')
    args = parser.parse_args()
    return args


def main():
    # load arguments
    args = parse_args()

    # define logging level and format
    level = logging.ERROR
    if args.verbose:
        level = logging.DEBUG
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=level)

    # init models
    if args.model == 'ISN':
        # init model for scene_classification
        sc = scene_classification.SceneClassifier()

        # init models for geolocation estimation
        # init ISN for concept 'indoor'
        ge_indoor = geo_estimation.GeoEstimator(
            os.path.join(cur_path, 'models', 'ISN_M_indoor', 'model.ckpt'), scope='indoor')
        # init ISN for concept 'natural'
        ge_natural = geo_estimation.GeoEstimator(
            os.path.join(cur_path, 'models', 'ISN_M_natural', 'model.ckpt'), scope='natural')
        # init ISN for concept 'urban'
        ge_urban = geo_estimation.GeoEstimator(
            os.path.join(cur_path, 'models', 'ISN_M_urban', 'model.ckpt'), scope='urban')
    elif args.model == 'base_L':
        ge_base = geo_estimation.GeoEstimator(os.path.join(cur_path, 'models', 'base_M', 'model.ckpt'))
    elif args.model == 'base_M':
        ge_base = geo_estimation.GeoEstimator(os.path.join(cur_path, 'models', 'base_M', 'model.ckpt'))

    # predict scene label
    if args.model == 'ISN':
        # get scene label
        scene_probabilities = sc.get_scene_probabilities(args.image)
        scene_label = sc.get_scene_label(scene_probabilities)
    else:
        scene_label = -1

    # predict geolocation depending on model and scenery
    if scene_label == -1:
        lat, lng = ge_base.get_prediction(args.image)
    if scene_label == 0:
        lat, lng = ge_indoor.get_prediction(args.image)
    if scene_label == 1:
        lat, lng = ge_natural.get_prediction(args.image)
    if scene_label == 2:
        lat, lng = ge_urban.get_prediction(args.image)

    return 0


if __name__ == '__main__':
    sys.exit(main())