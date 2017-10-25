"""
Convert and download data through UniProt API

Initial source: 
- http://www.uniprot.org/help/api
- http://www.uniprot.org/help/api_idmapping

Programmatic access - Retrieving entries via queries
http://www.uniprot.org/help/api_queries

Nice doc on urllib package:
HOWTO Fetch Internet Resources Using The urllib Package
https://docs.python.org/3/howto/urllib2.html

"""

__author__ = "Pierre Poulain"
__version__ = "0.1"
__license__ = "MIT"


import urllib.parse
import urllib.request
from urllib.error import URLError, HTTPError


def convert(ids, format_from, format_to, format_output='tab'):
    """Convert ids from format_from to format_to with UniProt API

    Possible formats (for from and to): http://www.uniprot.org/help/api_idmapping
    
    Possible columns: http://www.uniprot.org/help/uniprotkb_column_names
    """
    url = 'http://www.uniprot.org/uploadlists/'
    params = {
        'from': format_from,
        'to': format_to,
        'format': format_output,
        'columns': 'id,entry name,reviewed,length', 
        'query': ' '.join(ids)
    }
    # Add email address here to help UniProt to debug in case of problem
    contact = 'bob@mail.net'
    headers = {'User-Agent': 'Python bot / '.format(contact)}
    data = urllib.parse.urlencode(params)
    data = data.encode('ascii') # data should be bytes
    req = urllib.request.Request(url, data, headers)
    page = ""
    try:
        response = urllib.request.urlopen(req)
        page = response.read().decode('utf8')
    except HTTPError as e:
        print('Server could not answer.')
        print('Error code: ', e.code)
    except URLError as e:
        print('Fail to reach the server.')
        print('Reason: ', e.reason)
    finally:
        return page


print("\nGet id list only")
print(convert(['17137000', '442614522', '24581010', '349669'], 'P_GI', 'ACC', 'list' ))

print("\nGet ids and a few details")
print(convert(['17137000', '442614522', '24581010', '349669'], 'P_GI', 'ACC', 'tab' ))

print("\nGet all data in txt")
print(convert(['17137000', '442614522'], 'P_GI', 'ACC', 'txt' ))

print("\nGet all data in xml")
print(convert(['17137000', '442614522'], 'P_GI', 'ACC', 'xml' ))


