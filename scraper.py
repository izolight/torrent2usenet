#! /usr/bin/python3
import urllib.request as rq
import re, sqlite3, os, time, sys, config, logging

FORMAT = '%(asctime)s %(levelname)-8s %(message)s'
DRAMA = 'http://www.tobest2.net/bbs/board.php?bo_table=torrent_kortv_drama'
ENT = 'http://www.tobest2.net/bbs/board.php?bo_table=torrent_kortv_ent'
DOCU = 'http://www.tobest2.net/bbs/board.php?bo_table=torrent_kortv_social'
MOVIES = 'http://www.tobest2.net/bbs/board.php?bo_table=torrent_movie_kor'
#F_TV = 'http://www.tosarang2.net/bbs/board.php?bo_table=torrent_engtv_drama'

logging.basicConfig(format=FORMAT,filename='/var/log/t2u/scraper.log',level=logging.DEBUG)
logger = logging.getLogger('torrent2usenet')

def open_site(url):
	req = rq.Request(url)
	req.add_header('User-agent', 'Mozilla/5.0')
	content = rq.urlopen(req).readall().decode('utf-8')

	return content

def get_links(url):
	content = open_site(url)
	link_re = re.compile(r"class=\"td_subject\">\s*.+?wr_id=(\d{1,6})")
	link_ids = re.findall(link_re,content)

	return link_ids

def extract_magnet(url):
	content = open_site(url)	
	magnet_re = re.compile(r"(magnet:\?xt=urn:btih:)(\w{40})")
	magnet = re.search(magnet_re, content)
	torrent_hash = magnet.group(2)
	magnet_link = magnet.group()

	return torrent_hash, magnet_link

def is_in_db(torrent_hash):
	conn = sqlite3.connect(config.script_dir + '/downloads.db')
	c = conn.cursor()
	c.execute("SELECT * FROM downloads WHERE hash = '%s'" % torrent_hash)
	if (c.fetchone()):		
		conn.close()
		return True
	conn.close()
	return False

def convert_and_move(magnet_link, torrent_hash,deluge=True,folder='movies'):
	if deluge:
		os.system("deluge-console 'add %s'" % magnet_link)
	else:
		os.system("/home/***REMOVED***/torrent2usenet/mag2tor.sh '%s' /opt/rtorrent/watch/%s" % (magnet_link,folder))

	conn = sqlite3.connect(config.script_dir + '/downloads.db')
	c = conn.cursor()
	c.execute("INSERT INTO downloads VALUES ('%s')" % torrent_hash)
	conn.commit()
	conn.close()

def grab_magnets(url, deluge=True, folder='movies'):
#	logger.info('Checking for new links in %s' % url)
#	print(url)
	link_ids = get_links(url)
	for link_id in link_ids:
		link = url + '&wr_id=' + link_id
#		logger.info('Link is %s' % link)
#		print(link_id)
		t_hash, m_link = extract_magnet(link)
		if (is_in_db(t_hash)):
#			logger.info('Hash found in db %s moving to next URL' % t_hash)
			time.sleep(3)
			break
		else:
			logger.info('Adding magnet to deluge %s' % m_link)
			convert_and_move(m_link, t_hash, deluge, folder)
			time.sleep(3)

grab_magnets(DRAMA)
grab_magnets(ENT)
grab_magnets(DOCU)
grab_magnets(MOVIES, False, 'movies')
#grab_magnets(F_TV, False, 'tv')
