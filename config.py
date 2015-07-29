#! /usr/bin/python3
import os, logging

script_dir = os.path.dirname(os.path.realpath(__file__))
usenet_dir = '/home/***REMOVED***/post_to_usenet/'
manual_dir = '/home/***REMOVED***/post_to_usenet/manual/' # no rename
music_dir = '/home/***REMOVED***/post_to_usenet/music/' # different Group
FORMAT = '%(asctime)s %(levelname)-8s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('torrent2usenet')
