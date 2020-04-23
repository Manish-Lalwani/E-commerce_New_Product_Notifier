import discord
from discord import Webhook, RequestsWebhookAdapter, File
import my_beautify as mb


class DiscordWebhook1:
    def __init__(self):
        mb.fname_print("Constructor")
        self.webhook_id = 701461143214096504
        self.webhook_token = 'ZclvwnGvQEbn2Y2XugIlhIcdJEVFJX5tRkJUe6GS-jdfE9NtYX-lBY38ceSMKn01xB-z'
        self.webhook_obj = None
        self.embed = None
        self.product_list = None

    def authenticate(self):
        mb.fname_print("authenticate")
        # Create webhook object
        self.webhook_obj = Webhook.partial(id=self.webhook_id, token=self.webhook_token,
                                            adapter=RequestsWebhookAdapter())
        
    def set_embed_new(self,main_data_list,x): #x is new product index
        mb.fname_print("set_embed_new")
        self.embed = discord.Embed(title="From Site: Doubleclutch.it ", description="Product: {} Price: {}".format(main_data_list[x][1],main_data_list[x][3]), color=0x00ff00)
        #for x in new_product_index_list:
        self.embed.set_thumbnail(url=main_data_list[x][4])
       
        for x,y in zip(main_data_list[x][7],main_data_list[x][8]):
            self.embed.add_field(name=x, value='[ATC]({})'.format(y), inline=True)


        self.embed.set_footer(text="End of the message...Have a nice day")
        self.embed.set_author(name="New Product Notification...!")



    def send(self):
        mb.fname_print("send")
        self.webhook_obj.send(embed=self.embed)

