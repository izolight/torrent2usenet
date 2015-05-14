#! /usr/bin/python3
import urllib.request as rq
import re, sqlite3, os, shutil, time, sys

DRAMA = 'http://www.torrentbest.net/bbs/board.php?bo_table=torrent_kortv_drama'
ENT = 'http://www.torrentbest.net/bbs/board.php?bo_table=torrent_kortv_ent'
TEMP = 'http://www.torrentbest.net/bbs/board.php?bo_table=torrent_kortv_ent&page=2'

def open_site(url):
	req = rq.Request(url)
	req.add_header('User-agent', 'Mozilla/5.0')
	content = rq.urlopen(req).readall().decode('utf-8')

	return content

def get_links(url):
#	print('Getting links from: %s' % url)
	content = open_site(url)
	
	link_re = re.compile(r"class=\"subject\">\s*.{0,55}wr_id=(\d{5})")
	link_ids = re.findall(link_re,content)

	return link_ids

def extract_magnet(url):
#	print('Extracting magnets from: %s' % url)
	content = open_site(url)
	
	magnet_re = re.compile(r"(magnet:\?xt=urn:btih:)(\w{40})")
	magnet = re.search(magnet_re, content)
	torrent_hash = magnet.group(2)
	magnet_link = magnet.group()

	return torrent_hash, magnet_link

def is_in_db(torrent_hash):
	conn = sqlite3.connect('/home/***REMOVED***/downloads.db')
	c = conn.cursor()
	c.execute("SELECT * FROM downloads WHERE hash = '%s'" % torrent_hash)
	if (c.fetchone()):		
		conn.close()
#		print('%s found in DB' % torrent_hash)
		return True
	conn.close()
	return False

def convert_and_move(magnet_link, torrent_hash):
	print("Converting: %s" % magnet_link)
	os.system("aria2c '%s'" % magnet_link)
#	os.system('/home/***REMOVED***/mag2tor.sh ' + magnet_link)
#	shutil.move('/home/***REMOVED***/meta-' + torrent_hash + '.torrent', '/home/***REMOVED***/downloads/watch/')
	conn = sqlite3.connect('/home/***REMOVED***/downloads.db')
	c = conn.cursor()
	c.execute("INSERT INTO downloads VALUES ('%s')" % torrent_hash)
	conn.commit()
	conn.close()

def grab_magnets(url):
	link_ids = get_links(url)
	for link_id in link_ids:
		link = url + '&wr_id=' + link_id
		t_hash, m_link = extract_magnet(link)
		if (is_in_db(t_hash)):
#			print('sleeping 5 secs')		
			time.sleep(3)
			break
		else:
			convert_and_move(m_link, t_hash)
#			print('sleeping 5 secs')		
			time.sleep(3)

grab_magnets(DRAMA)
grab_magnets(ENT)
#grab_magnets(TEMP)

sys.exit()

