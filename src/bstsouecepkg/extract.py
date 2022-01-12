import base64
import re
from datetime import datetime
import requests
import json
from lxml import etree
import urllib.request
from io import BytesIO
import pandas as pd
import pycountry
from geopy.geocoders import Nominatim
import importlib
import time
import os
from abc import ABC, abstractmethod
import boto3
import hashlib
import tabula
#import logging
#logging.basicConfig(level=logging.INFO)

# Extract class
class Extract(ABC):
    def __init__(self):
        self.session = requests.Session()
        self.socket_timeout = 60
        self.CONFIG = importlib.import_module('src.bstsouecepkg.config')
        self.org_schema = importlib.import_module(self.CONFIG.ORG_SCHEMA_PATH).schema
        
        try:
            self.DATA_CACHE = os.environ['DATA_CACHE']
            self.s3_resource = boto3.resource('s3')
            self.bucket = self.s3_resource.Bucket(self.DATA_CACHE)
            self.s3_client = boto3.client('s3')
        except Exception as e:
            print ('graph s3: ' + str(e))
            pass
        
    def Execute(self, searchquery, fetch_type, action, API_BASE_URL):
        '''
        The main function of the class, which returns the final output of the fetcher.
        :param searchquery: the query searched for
        :param fetch_type: the type of content to be returned
        :param action: the action to be performed
        :param API_BASE_URL: base URL of the API
        :return: the final output of the fetcher
        '''
        self.FETCH_TYPE = fetch_type
        self.API_BASE_URL = API_BASE_URL

        if self.FETCH_TYPE is None or self.FETCH_TYPE == "":
            pages = self.getpages(searchquery)

            if pages is not None:
                data = self.__parse_pages(pages)
            else:
                data = []
        else:
            if self.FETCH_TYPE == "graph:shareholders":
                link = base64.b64decode(searchquery).decode('utf-8')
                try:
                    link = ast.literal_eval(link)
                except:
                    pass
                level0, level1 = self.parse(link)
                
                now = datetime.now()
                job_id = str(hashlib.md5(searchquery.strip().encode('utf-8')).hexdigest()) + str(now.timestamp())

                level_0_file_name = job_id + "-level-0.json"
                level_1_file_name = job_id + "-level-1.json"

                level_0_url = level0 # self.__save_graph_in_s3(level_0_file_name, json.dumps(level0, indent=2))
                level_1_url = level1 # self.__save_graph_in_s3(level_1_file_name, json.dumps(level1, indent=2))

                data = {
                    "_links": {
                        "shareholders": [
                            {
                                "level": 0,
                                "href": level_0_url
                            },
                            {
                                "level": 1,
                                "href": level_1_url
                            }
                        ]
                    }
                }
                
            else:
                data = self.__fetchByField(searchquery)
                
        return data
        
    def __get_mapper_file(self):
        '''
        This function accesses the mapper file stored in a pre-configured location.
        :return: the JSON formatted output of the file
        '''
        # ConfigBucket = os.environ['Config_Bucket']
        # schema_mapper = self.s3_client.get_object(Bucket=ConfigBucket, Key='schema_mapper.json')
        # return json.loads(schema_mapper['Body'].read().decode('utf-8'))
        return self.org_schema

    def __save_graph_in_s3(self, file_name, data):
        '''
        This function stores the data provided in a JSON file in configured S3 bucket and generates a presigned URL to access the file.
        :param file_name: the name of the file to be created
        :param data: the data to be stored in the file
        :return: the presigned URL for the created file
        '''
        key = self.NICK_NAME + "/shareholders/graph/" + file_name
        self.bucket.put_object(Key=key, Body=data)
        expire_time = 604800
        response = self.s3_client.generate_presigned_url('get_object', Params={'Bucket': self.DATA_CACHE, 'Key': key}, ExpiresIn=expire_time)
        return response
        
    def __fetchByField(self, link):
        link = base64.b64decode(link).decode('utf-8')
        try:
            res = self.parse(link)
        except:
            pass
        try:
            res = self.parse(json.loads(link.replace("\'", "\"")))
        except:
            pass
        return [res]
        
    def __parse_pages(self, pages):
        '''
        This function iterates over the collected links and parses the data in each. The number of results has been limited to 10.
        :param pages: the links collected based on the search query that is passed
        :return: the list of search results
        '''
        rlist = []
        for link in pages:
            res = self.parse(link)
            if res is not None:
                rlist.append(res)
                if len(rlist) == 10:
                    break
        return rlist
        
### Override this abstract function.
    @abstractmethod
    def getpages(self, searchquery):
        pass
    
    def parse(self, link):
        '''
        This function extracts and maps the data to the BST schema using smaller functions implemented by the user.
        :param link: a single link to extract data for a given entity
        :return: the mapped output of the fetcher
        '''
        try:
            edd = {}
            sholdersl1 = {}
            
            if self.FETCH_TYPE == "" or self.FETCH_TYPE == "overview":
                edd['overview'] = self.get_overview(link)
                return self.__map(edd, link)
                
            if self.FETCH_TYPE == "officership":
                edd['officership'] = self.get_officership(link)
                return self.__map(edd, link)
                
            if self.FETCH_TYPE == "documents":
                edd['documents'] = self.get_documents(link)
                return self.__map(edd, link)
                
            if self.FETCH_TYPE == "subsidiaries":
                edd['subsidiaries'] = self.get_subsidiaries(link)
                return self.__map(edd, link)
                
            if self.FETCH_TYPE == "branches":
                edd['branches'] = self.get_branches(link)
                return self.__map(edd, link)

            if self.FETCH_TYPE == 'Financial_Information':
                edd['Financial_Information'] = self.get_financial_information(link)
                return self.__map(edd, link)
                
            if self.FETCH_TYPE == "graph:shareholders":
                edd, sholdersl1 = self.get_shareholders(link)
                return edd, sholdersl1
                
        except Exception as e:
            print(e)
            return None

### Based on the sections available in the confluence page
### Re-write only the functions required
### Out of the 7 empty function below
    def get_overview(self, link):
        pass
    
    def get_officership(self, link):
        pass
    
    def get_documents(self, link):
        pass
    
    def get_subsidiaries(self, link):
        pass
    
    def get_branches(self, link):
        pass
    
    def get_shareholders(self, link):
        pass
    
    def get_financial_information(self, link):
        pass
    
    def __map(self, edd, link):
        '''
        This function remaps the extracted data based on a configurable file provided while performing a few sanity checks.
        :param edd: the extracted data
        :param link: the link for a specific entity
        :return: the re-mapped output of the fetcher
        '''
        container = {}
        mapper = self.__get_mapper_file()
        
        if self.FETCH_TYPE == "":
            FETCH_TYPE = "overview"
        else:
            FETCH_TYPE = self.FETCH_TYPE
        
        mapper = mapper[FETCH_TYPE]
        edd = edd[FETCH_TYPE]

        if isinstance(edd, list):
            data = []
            for item in edd:
                data.append(self.dict_mapping(mapper, item))
        else:
            data = self.dict_mapping(mapper, edd)
            
        if data:
            container[FETCH_TYPE] = data
            container['_links'] = self.__links(link)
    
        return container
        
    def get_function_based_on_type(self, attr, main_value):
        '''
        This function maps a given attribute to the schema provided.
        :param attr: the schema for the attribute
        :param main_value: the value for the attribute
        :return: the mapped attribute result
        '''
        var_name = var_value = ""
        
        if attr['type'] == "str":
            if isinstance(main_value, str):
                var_name = attr['name']
                var_value = main_value
                
        elif attr['type'] == "list":
            if isinstance(main_value, list):
                var_name = attr['name']
                var_value = main_value
                
        elif attr['type'] == "listOfDict":
            var_value = []
            var_name = attr['name']
            for item in main_value:
                sub_section = self.dict_mapping(attr['keyValue'], item)
                if sub_section:
                    var_value.append(sub_section)
                
        elif attr['type'] == "dict":
            var_name = attr['name']
            sub_section = self.dict_mapping(attr['keyValue'], main_value)
            if sub_section:
                var_value = sub_section
        return var_name, var_value
            
    def dict_mapping(self, key_value, main_value):
        '''
        This function maps a given dict attribute to the schema provided.
        :param key_value: the schema for the attribute
        :param main_value: the value for the attribute
        :return: the mapped dict attribute result
        '''
        sub_section = {}
        for sub_key, sub_value in key_value.items():
            try:
                for inner_key, inner_value in main_value.items():
                    if inner_key.lower() == sub_key.lower():
                        name, val = self.get_function_based_on_type(sub_value, inner_value)
                        sub_section[name] = val
            except Exception as e:
                if sub_value["must"] == 1:
                    print("You have missed a compulsory field: ",sub_key)
        return sub_section
        
    def __links(self, link):
        '''
        This function creates the links to access different sections of the data based on the fetch type.
        :param link: the link for a specific entity
        :return: the links to access different sections of the data
        '''
        data = {}
        base_url = self.NICK_NAME
        link = str(link)
        link2 = base64.b64encode(link.encode('utf-8'))
        link2 = (link2.decode('utf-8'))
        data_keys = ['overview', "officership", "documents", "subsidiaries", "branches", "graph:shareholders", "Financial_Information"]
        for d_key in data_keys:
            if d_key in self.fields:
                data[d_key] = {
                        "method": "GET",
                        "url": f"{self.API_BASE_URL}?source={base_url}&url={link2}&fields={d_key}"
                }
        return data

# GetPages class        
class GetPages():
    def __init__(self):
        self.session = requests.Session()
        self.browser_header = {
            'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
            'Accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        }
        self.CONFIG = importlib.import_module('src.bstsouecepkg.config')
        # self.proxies = self.CONFIG.PROXIES
        
        self.selenium_webnito_url = self.CONFIG.selenium_webnito_url
        # if not self.proxies:
        #     self.proxies = {
        #         "http": None,
        #         "https": None
        #     }

        # self.ssl_path = self.CONFIG.SSL_PATH
        # if not self.ssl_path:
        #     self.ssl_path = True

        #self.logger = logging.getLogger(__name__)
        
    def get_content(self, url, headers=None, data=None, method='GET', verify=None, params=None, cookies=None, proxies=None, json=None,timeout=None, webnito=False, stream=False):
        content = {}
        if webnito == "selenium":
            url = self.selenium_webnito_url.replace('{}', url)
        try:
            if method == 'GET':
                r = self.session.get(url, headers=headers, data=data, verify=verify, params=params, cookies=cookies, proxies=proxies, timeout=timeout, stream=stream)
                content = r
            elif method == 'POST':
                r = self.session.post(url, headers=headers, data=data, json=json, verify=verify, params=params, cookies=cookies, proxies=proxies, timeout=timeout, stream=stream)
                content = r

            # logging.info('Proxy: ' + str(r.connection.proxy_manager))
            # print('Proxy: ' + str(r.connection.proxy_manager))
        except Exception as e:
            print(e)
            pass
        return content
        
    def get_tree(self, url, headers=None, data=None, method='GET', verify=None, params=None, cookies=None, proxies=None, json=None,timeout=None, webnito=False, stream=False):
        tree = None
        try:
            content = self.get_content(url, headers=headers, data=data, verify=verify, params=params, cookies=cookies, proxies=proxies, timeout=timeout, stream=stream, method=method)
            tree = etree.HTML(content.content)
        except Exception as e:
            print(e)
            pass
        return tree
        
    def get_file(self, xpath, url, headers=None, data=None, method='GET', file_base_url=None):
        fd = None
        try:
            if url is not None:
                tree = self.get_tree(url, headers=headers, data=data, method=method)
                file_url = file_base_url + tree.xpath(xpath)[0].attrib['href']
            else:
                file_url = file_base_url
            file_url = file_url.replace(" ", "%20")
            fd = urllib.request.urlopen(file_url)
        except Exception as e:
            pass
        return fd
        
    def get_content_webnito(self, link, stype):
        content = None
        try:
            if stype == 'webnito':
                link2 = base64.b64encode(link.encode('utf-8'))
                link2 = (link2.decode('utf-8'))
                url = 'https://webnito.xara.ai/?url=' + link2 + '&stype=webnito'
                r = self.session.get(url)
                content = r.json()['content']
            elif stype == 'selenium':
                url = 'https://webnito.xara.ai/?url=' + link + '&stype=selenium'
                r = self.session.get(url, headers=self.browser_header)
                content = r.content
        except Exception as e:
            print(e)
            pass
        return content
        
    def get_tree_webnito(self, link, stype):
        tree = None
        try:
            content = self.get_content_webnito(link, stype)
            tree = etree.HTML(content)
        except Exception as e:
            print(e)
            pass
        return tree
            
    def getpages_xpath(self, xpath, url, headers=None, data=None, method='GET'):
        link_list = []
        try:
            tree = self.get_tree(url, headers=headers, data=data, method=method)
            links = tree.xpath(xpath)
            for link in links:
                link_list.append(link.attrib['href'])
        except Exception as e:
            print(e)
            pass
        return link_list
        
    def getpages_api(self, url, headers=None, data=None, method='GET', verify=None, params=None, cookies=None, proxies=None,json_data=None, timeout=None, webnito=False, stream=False):
        json_obj = None
        try:
            content = self.get_content(url, headers=headers, data=data, verify=verify, params=params, cookies=cookies,proxies=proxies, timeout=timeout, stream=stream, method=method, json=json_data)
            json_obj = json.loads(content.content)
        except Exception as e:
            print(e)
            pass
        return json_obj
    
    def getpages_csv(self, searchquery, search_column, xpath, url, headers=None, data=None, method='GET', file_base_url=None):
        df = None
        try:
            fd = self.get_file(xpath, url, headers=headers, data=data, method=method)
            df = pd.read_csv(BytesIO(fd.read()), header=1)
            df = df[df[search_column].str.lower().str.contains(searchquery.lower(), na=False)]
        except Exception as e:
            print(e)
            pass
        return df
    
    def getpages_excel(self, searchquery, search_column, xpath, url, headers=None, data=None, method='GET', file_base_url=None):
        df = None
        try:
            fd = fd = self.get_file(xpath, url, headers=headers, data=data, method=method)
            df = pd.read_excel(BytesIO(fd.read()), header=1)
            df = df[df[search_column].str.lower().str.contains(searchquery.lower(), na=False)]
        except Exception as e:
            print(e)
            pass
        return df
    
    def getpages_pdf(self, searchquery, search_column, xpath=None, url=None, headers=None, data=None, method='GET', file_base_url=None, multiple_tables=True, pages='all', stream=True, area=None):
        df = None
        try:
            fd = self.get_file(xpath, url, headers=headers, data=data, method=method, file_base_url=file_base_url)
            df = tabula.read_pdf(BytesIO(fd.read()), multiple_tables=multiple_tables, pages=pages, stream=stream, area=area)
        except Exception as e:
            print(e)
            pass
        return df

# Parse class    
class Parse():
    def get_country(self, address, result_type):
        location = None
        try:
            geolocator = Nominatim(user_agent="http")
            location = geolocator.geocode(address, language="en", timeout=10)
            query = address
            if location is None:
                while True:
                    query = list(filter(None, query.split(',')))
                    if len(query) > 0:
                        query = ', '.join(query[1:])
                        location = geolocator.geocode(query, language="en", timeout=10)
                    else:
                        query = ''
                    if location is not None or query == '':
                        break
        except:
            pass
        if location is not None:
            location = location.address.split(', ')[-1]
            if result_type == 'country':
                result = location
            elif result_type == 'country_code':
                result = pycountry.countries.get(name=location).alpha_2
        return result
        
    def get_date(self, date_string, date_format):
        return str(datetime.strptime(date_string, date_format).date())