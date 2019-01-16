#!/usr/bin/env python

"""

                  888
                  888
                  888
88888b.   .d88b.  88888b.   .d88b.  888  888
888 "88b d88""88b 888 "88b d88""88b `Y8bd8P'
888  888 888  888 888  888 888  888   X88K
888  888 Y88..88P 888 d88P Y88..88P .d8""8b.     http://nobox.io
888  888  "Y88P"  88888P"   "Y88P"  888  888     http://github.com/noboxio

Author: Brian McGinnis
Date: 6/23/17
"""

import json
import watson_developer_cloud
#from watson_developer_cloud import AssistantV1


class Assistant:

    def __init__(self, usr, pas, workspace):
        self.convo = watson_developer_cloud.AssistantV1(
            username=usr,
            password=pas,
            url='https://gateway.watsonplatform.net/assistant/api',
            version='2018-07-10')
        self.workspace_id = workspace

    def sendMessage(self, message):
        response = self.convo.message(
            workspace_id=self.workspace_id,
            input={'text': message}).get_result()
        jsn = json.loads(json.dumps(response))
        #print(jsn)
        return jsn['output']['text'][0]

# con = conversation('154b5b29-d1ca-4ff2-be09-c33c5e1d9e20' , 'pmNftYlpvMS8','9ef80568-2a3b-4790-a8e0-363c0bc7d237')
# respon = con.sendMessage("LOVE ME JERRY")
# print(respon)
