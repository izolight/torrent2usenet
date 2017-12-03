#! /usr/bin/python3
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
config_file = '/path/to/.gopoststuff.conf'
nzb_path = '/path/to/nzb/'

base_dir = '/path/to/post_to_usenet/'

tv = {
    'dir': base_dir+'tv/',
    'prefix': 'YOURPREFIX',
    'from': 'YOUR POSTERNAME',
    'group': 'korea.binaries.tv',
    'server': 'YOUR USENETSERVER',
    'host': 'YOUR USENETHOST',
}
movie = {
    'dir': base_dir+'movies/',
    'prefix': 'YOURPREFIX',
    'from': 'YOUR POSTERNAME',
    'group': 'korea.binaries.movies',
    'server': 'YOUR USENETSERVER',
    'host': 'YOUR USENETHOST',
}
music = {
    'dir': base_dir+'mv/',
    'prefix': 'YOURPREFIX',
    'from': 'YOUR POSTERNAME',
    'group': 'korea.binaries.music.videos',
    'server': 'YOUR USENETSERVER',
    'host': 'YOUR USENETHOST',
}
manual = {
    'dir': base_dir+'manual/',
    'prefix': 'YOURPREFIX',
    'from': 'YOUR POSTERNAME',
    'group': 'alt.binaries.multimedia.korean',
    'server': 'YOUR USENETSERVER',
    'host': 'YOUR USENETHOST',
}
jap = {
    'dir': base_dir+'jap/',
    'prefix': 'YOURPREFIX',
    'from': 'YOUR POSTERNAME',
    'group': 'alt.binaries.multimedia.japanese',
    'server': 'YOUR USENETSERVER',
    'host': 'YOUR USENETHOST',
}
album = {
    'dir': base_dir+'music/album/',
    'prefix': 'YOURPREFIX',
    'from': 'YOUR POSTERNAME',
    'group': 'alt.binaries.multimedia.korean',
    'server': 'YOUR USENETSERVER',
    'host': 'YOUR USENETHOST',
}
single = {
    'dir': base_dir+'music/single/',
    'prefix': 'YOURPREFIX',
    'from': 'YOUR POSTERNAME',
    'group': 'alt.binaries.multimedia.korean',
    'server': 'YOUR USENETSERVER',
    'host': 'YOUR USENETHOST',
}

