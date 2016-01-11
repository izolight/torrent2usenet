#! /usr/bin/python3
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
config_file = '/home/***REMOVED***/.gopoststuff.conf'
nzb_path = '/home/***REMOVED***/nzb/'

base_dir = '/home/***REMOVED***/post_to_usenet/'

tv = {
    'dir': base_dir+'tv/',
    'prefix': '[***REMOVED***]',
    'from': '***REMOVED*** <***REMOVED***>',
    'group': 'korea.binaries.tv',
    'server': 'newsoo',
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
    'dir': base_dir+'mv/',
    'prefix': '[***REMOVED***]',
    'from': '***REMOVED*** <***REMOVED***>',
    'group': 'korea.binaries.music.videos',
    'server': 'newsoo',
    'host': 'newsoo.fr',
}
manual = {
    'dir': base_dir+'manual/',
    'prefix': '[***REMOVED***]',
    'from': '***REMOVED*** <***REMOVED***>',
    'group': 'alt.binaries.multimedia.korean',
    'server': 'newsoo',
    'host': 'newsoo.fr',
}
jap = {
    'dir': base_dir+'jap/',
    'prefix': '[***REMOVED***]',
    'from': '***REMOVED*** <***REMOVED***>',
    'group': 'alt.binaries.multimedia.japanese',
    'server': 'newsoo',
    'host': 'newsoo.fr',
}
album = {
    'dir': base_dir+'music/album/',
    'prefix': '[***REMOVED***]',
    'from': '***REMOVED*** <***REMOVED***>',
    'group': 'alt.binaries.multimedia.korean',
    'server': 'newsoo',
    'host': 'newsoo.fr',
}
single = {
    'dir': base_dir+'music/single/',
    'prefix': '[***REMOVED***]',
    'from': '***REMOVED*** <***REMOVED***>',
    'group': 'alt.binaries.multimedia.korean',
    'server': 'newsoo',
    'host': 'newsoo.fr',
}

