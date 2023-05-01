import warcio
from bs4 import BeautifulSoup
from kademlia.network import Server


def extract_content(response):
    # Extract the HTML content from the HTTP response
    html = response.raw_stream.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()
	

def create_dataset():
	# Connect to the Kademlia DHT network
	node = Server()
	node.listen(8468)
	node.bootstrap([('localhost', 8468)])
	i = 0
	# Parse the WARC files and extract the web page content
	for filename in ['CC-MAIN-2022-04']:
		with open(filename + '.warc.gz', 'rb') as f:
			for record in warcio.archiveiterator.ArchiveIterator(f):
				# if i == 0:
				# 	i += 1
				# 	continue
				if record.rec_type == 'response':
					url = record.rec_headers.get_header('WARC-Target-URI')
					print(vars(record))
					print(url)
					content = extract_content(record)
					print(content)
					# Store the key-value pair in the Kademlia DHT
					node.set(url, content)

if __name__ == '__main__':
    create_dataset()
