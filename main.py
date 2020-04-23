from my_scrapper import Scrapper
from my_discord import DiscordWebhook1
import time



if __name__ == '__main__':

	delay = int(input("Enter delay between each run in seconds eg: 3 for 3seconds:"))
	proxy_ip = input("Enter proxy ip and port in format eg: https://192.168.1:8080 or leave blank :")
	proxy = None

	if len(proxy_ip) > 0:
		proxy = {"https" : proxy_ip}

	sc1 = Scrapper()
	dw1 = DiscordWebhook1()
	dw1.authenticate()

	while 1:

		sc1.request_initiate(proxy)
		sc1.data_extractor()
		sc1.data_store_retrieve()
		sc1.new_product_checker()
		main_data_list, new_product_found_index_list, new_product_list = sc1.getter()

		if len(new_product_found_index_list) > 0:
			#print("new product are:")
			for x in new_product_found_index_list:
				#new_product_list.append(x)
				print(x)
				dw1.set_embed_new(main_data_list,x)
				dw1.send()

		seconds = delay
		print("seconds are :",seconds)
		while seconds >0:
			print("{} seconds left".format(seconds))
			time.sleep(1)
			seconds = seconds -1

   




