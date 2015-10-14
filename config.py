#! /usr/bin/python3
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
config_file = '/home/***REMOVED***/sample.conf'
nzb_path = '/home/***REMOVED***/nzb/'

base_dir = '/home/***REMOVED***/post_to_usenet/'
usenet_dir = base_dir +'auto/'
manual_dir = base_dir + 'manual/' # no rename
music_dir = base_dir + 'music/' # different Group
movie_dir = base_dir + 'movies/' # different Group

tv = {
    'dir': base_dir+'tv/',
    'prefix': '[***REMOVED***]',
    'from': '***REMOVED*** <***REMOVED***>',
    'group': 'korea.binaries.tv',
    'server': '***REMOVED***',
    'host': 'newsoo.fr',
}
movie = {
    'dir': base_dir+'movies/',
    'prefix': '[***REMOVED***]',
    'from': '***REMOVED*** <***REMOVED***>',
    'group': 'korea.binaries.movies',
    'server': 'newsoo',
    'host': 'newsoo.fr',
}
music = {
    'dir': base_dir+'music/',
    'prefix': '[***REMOVED***]',
    'from': '***REMOVED*** <***REMOVED***>',
    'group': 'korea.binaries.music.videos',
    'server': '***REMOVED***',
    'host': 'newsoo.fr',
}

