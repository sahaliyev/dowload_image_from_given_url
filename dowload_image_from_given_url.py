import os
import random
from os.path import splitext, basename
from urllib.parse import urlparse
from user_agents import user_agents  # constant file contains some user agents
import requests


class DownloadImage:
    def __init__(self):
        self.extension_dict = {
            'image/apng': '.apng',
            'image/bmp': '.bmp',
            'image/gif': '.gif',
            'image/png': '.png',
            'image/jpeg': '.jpg',
            'image/svg+xml': '.svg',
            'image/tiff': '.tif',
            'image/x-icon': '.ico',
            'image/webp': '.webp'
        }

    @staticmethod
    def get_random_user_agent():
        return random.choice(user_agents)  # for every request different user agent will be selected

    @staticmethod
    def get_file_name(url):
        parsed_url = urlparse(url)
        file_name, file_extension = splitext(basename(parsed_url.path))
        return file_name

    def get_file_content_and_extension_from_content_type(self, url):
        response = requests.get(url, headers={'User-Agent': self.get_random_user_agent()})
        if response.status_code != 200:
            raise Exception(f"{url} is not parsed: Request error!")
        content_type = response.headers['content-type']
        try:
            extension = self.extension_dict[content_type]
        except KeyError:
            extension = None
        content = response.content
        return extension, content

    def main(self, url):
        path = r'C:\Sahil'
        file_extension, content = self.get_file_content_and_extension_from_content_type(url)
        file_name = self.get_file_name(url)
        name_and_extension = file_name + file_extension
        full_path_to_file = os.path.join(path, name_and_extension)
        with open(full_path_to_file, "wb") as fw:
            fw.write(content)
        print(f"{file_name} saved on directory {full_path_to_file}")


if __name__ == '__main__':
    url = 'https://i.ytimg.com/vi/MPV2METPeJU/maxresdefault.jpg'
    DownloadImage().main(url)
