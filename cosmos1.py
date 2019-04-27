import azure.cosmos.cosmos_client as cosmos_client
from random import randint
import datetime
import time

config = {
    'ENDPOINT': 'Fill it!',
    'PRIMARYKEY': 'Fill it!',
    'DATABASE': 'CosmosDatabase',
    'CONTAINER': 'CosmosContainer'
}

# Initialize the Cosmos client
client = cosmos_client.CosmosClient(url_connection=config['ENDPOINT'], auth={
                                    'masterKey': config['PRIMARYKEY']})

#Time
ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'
for i in range('simulated number'):
    item = client.CreateItem("put your container['_self'] here as a string", {
        'id': str(i),
        'time': datetime.datetime.now().strftime(ISOTIMEFORMAT),
        'Sunshine': 'Yes',
        'Humidity': randint('simulated range'),
        'Tempture': randint('simulated range')
        }
    )
    print("Device", i, "infomation successfully uploaded!")
    # Pause 2 seconds then continue
    time.sleep(2)