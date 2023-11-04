from typing import Optional

import requests
import urllib.parse
import xml.etree.ElementTree as ET


def get_lyrics(artist: str, song: str) -> Optional[str]:
    r = requests.get(
        f"http://api.chartlyrics.com/apiv1.asmx/SearchLyric?artist={urllib.parse.quote_plus(artist)}&song={urllib.parse.quote_plus(song)}")
    root = ET.fromstring(r.text)

    # Iterate through each "SearchLyricResult" element
    for search_lyric_result in root:
        lyric_id = None
        lyric_checksum = None
        for x in search_lyric_result:
            if x.tag.endswith('LyricId'):
                lyric_id = x.text
            elif x.tag.endswith('LyricChecksum'):
                lyric_checksum = x.text
        if lyric_id is None or lyric_checksum is None:
            continue
        else:
            r = requests.get(
                f"http://api.chartlyrics.com/apiv1.asmx/GetLyric?lyricId={urllib.parse.quote_plus(lyric_id)}&lyricChecksum={urllib.parse.quote_plus(lyric_checksum)}")
            root2 = ET.fromstring(r.text)
            for n in root2:
                if n.tag.endswith("}Lyric"):
                    return n.text
    return None

