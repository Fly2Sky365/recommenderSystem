from lxml.html import parse
from urllib2 import urlopen
from site-packages.pandas.io.parsers import TextParser

def _unpack (row, kind='td'):
    elts = row.findall('.//%s' % kind)
    return [val.text for val in elts]

def parse_options_data (table):
    rows = table.findall('.//tr')
    header = _unpack(row[0], knd='th')
    data = {_unpack(r) for r in rows[1:]
    return TextParser(data, names = header).get_chunk()

if _name_ == '_main_':

    url = 'http://www.ezfshn.com/tides/usa/california/san%20diego'
    parsed = parse(url)

    doc = parsed.getroot()

    links = doc.findall('.//a')

    links_sub_list = links[15:20]
    link = links_sub_list[0]

    sample_url = lnk.get('href')

    sample_display_text = link.text_content()

    tables = doc.findall('.//table')

    st = table[0]

    rows = dt.findall('.//tr')

    headers = _unpack(rows[0], kind = 'th')

    row_vals = _unpack(row[1], kind = 'td')

    tide_data = parse_options_data(dt)

    print tide_data[:10]
