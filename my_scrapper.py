import requests
from bs4 import BeautifulSoup as soup
import pickle
import os
import my_beautify as mb
import time


class Scrapper:
    def __init__(self):
        self.soup1 = None
        self.main_data_list = []
        self.div_name_list = []
        self.old_main_data_list = []
        self.old_data_name_list = []
        self.new_product_found_index_list = []
        self.new_product_list = []

    def getter(self):
        return self.main_data_list, self.new_product_found_index_list, self.new_product_list

    def request_initiate(self,proxy):
        mb.fname_print("request_initiate")

        if proxy==None:
            response = requests.get('https://www.Cannot mention the sitename.com')
        else:
            response = requests.get('https://www.Cannot mention the sitename.com',proxies=proxy)


        with open('response.html', 'wb') as fp:
            fp.write(response.content)

        with open('response.html') as fp:
            self.soup1 = soup(fp, 'lxml')

    def data_extractor(self):
        mb.fname_print("data_extractor")
        #  fetched all list items each list item contains data for a particular product
        list_of_items = self.soup1.find_all('li', class_='item product product-item')

        # creating list of selected items
        data_brand_list = ['Data Brand']
        self.data_name_list = ['Data Name'] #only this list is needed outside function so declaring as class list rest all are local
        data_position_list = ['Data Position']
        data_price_list = ['Data Price']
        data_image = ['Data Image']
        data_availability = ['Data Availability']

        # self.div_name_list=[]
        div_url_list = []
        variant_url_list = []
        variant_name_list = []

        for i in range(1, len(list_of_items)):
            data_brand_list.append(list_of_items[i].div.a["data-brand"])
            self.data_name_list.append(list_of_items[i].div.a["data-name"])
            data_position_list.append(list_of_items[i].div.a["data-position"])
            data_price_list.append(list_of_items[i].div.a["data-price"])
            data_image.append(list_of_items[i].div.img["src"])
            data_availability.append(list_of_items[i].find("div", {'class': 'stock available'}).text)

            self.div_name_list.append([])
            for x in list_of_items[i].findAll("div", {'class': 'variant'}):
                self.div_name_list[i - 1].append(x)

            div_url_list.append([])
            div_url_list[i - 1].append(list_of_items[i].findAll("div", {'class': 'variant'}))

            variant_name_list.append([])
            for x in self.div_name_list[i - 1]:
                variant_name_list[i - 1].append(x.span.text)

            variant_url_list.append([])
            for x in div_url_list[i - 1][0]:
                variant_url_list[i - 1].append(x.span['data-size-url'])

        # crating a dictionary from variant:

        variant_dict = {variant_name_list[i - 1][j]: variant_url_list[i - 1][j] for j in
                        range(0, len(variant_url_list[i - 1]))}

        # creating 2d list to store all details in one:
        # self.main_data_list = []
        self.main_data_list.append([])
        self.main_data_list[0].append(data_brand_list[0])  # 0
        self.main_data_list[0].append(self.data_name_list[0])  # 1
        self.main_data_list[0].append(data_position_list[0])  # 2
        self.main_data_list[0].append(data_price_list[0])  # 3
        self.main_data_list[0].append(data_image[0])  # 4
        self.main_data_list[0].append(data_availability[0])  # 5
        self.main_data_list[0].append(data_brand_list[0])  # 6
        self.main_data_list[0].append('variant_name_list')  # 7
        self.main_data_list[0].append('variant_url_list')  # 8

        for i in range(1, len(self.data_name_list)):
            self.main_data_list.append([])
            self.main_data_list[i].append(data_brand_list[i])
            self.main_data_list[i].append(self.data_name_list[i])
            self.main_data_list[i].append(data_position_list[i])
            self.main_data_list[i].append(data_price_list[i])
            self.main_data_list[i].append(data_image[i])
            self.main_data_list[i].append(data_availability[i])
            self.main_data_list[i].append(data_brand_list[i])
            self.main_data_list[i].append(variant_name_list[i - 1])
            self.main_data_list[i].append(variant_url_list[i - 1])


    def data_store_retrieve(self):  # writing self.main_data_list to file
        mb.fname_print("data_store_retrieve")

        # will run on first time
        if not os.path.exists('main_data_list.txt'):
            with open('main_data_list.txt', 'wb') as fp:
                pickle.dump(self.main_data_list, fp)

            with open('data_name_list.txt', 'wb') as fp:
                pickle.dump(self.data_name_list, fp)

        with open('main_data_list.txt', 'rb') as fp:
            self.old_main_data_list = pickle.load(fp)

        with open('data_name_list.txt', 'rb') as fp:
            self.old_data_name_list = pickle.load(fp)

        with open('old_main_data_list.txt', 'wb') as fp:
            pickle.dump(self.old_main_data_list, fp)

        with open('old_data_name_list.txt', 'wb') as fp:
            pickle.dump(self.old_data_name_list, fp)

        with open('main_data_list.txt', 'wb') as fp:
            pickle.dump(self.main_data_list, fp)

        with open('self.data_name_list.txt', 'wb') as fp:
            pickle.dump(self.data_name_list, fp)


        with open("Run_time.txt",'a') as fp:
            localtime = time.asctime( time.localtime(time.time()) )
            fp.write("Ran on: :{}\n".format(localtime))




    def new_product_checker(self):
        mb.fname_print("new_product_checker")
        # self.new_product_found_index_list =[]
        # self.new_product_list = []


        if self.data_name_list == self.old_data_name_list:
            print("No new product added")
            new_product_add_flag = 0
            print("Program will shutdown")
            


        else:
            product_already_there_flag == 0

            for i in range(30):
                for j in range(30):
                    if self.data_name_list[i] == self.old_data_name_list[j]:
                        product_already_there_flag = 1
                        break
                    if product_already_there_flag == 0:
                        self.new_product_found_index_list.append(i)

            print("new product are:")
            for x in self.new_product_found_index_list:
                self.new_product_list.append(x)
                print(x)

                # temp test for new product
                ##for i in range(len(main_data_list)):
                ##print(main_data_list[i][x],"\n")
        # ===========================================================
        ##for i in range(len(main_data_list[0])):
        ##print(main_data_list[5][i],"\n")

        ##==========================================





