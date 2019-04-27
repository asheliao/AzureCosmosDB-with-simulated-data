import azure.cosmos.cosmos_client as cosmos_client
import numpy as np

config = {
    'ENDPOINT': 'Fill it!',
    'PRIMARYKEY': 'Fill it!',
    'DATABASE': 'CosmosDatabase',
    'CONTAINER': 'CosmosContainer'
}

# Initialize the Cosmos client
client = cosmos_client.CosmosClient(url_connection=config['ENDPOINT'], auth={
                                    'masterKey': config['PRIMARYKEY']})

# Create a database
db = client.CreateDatabase({'id': config['DATABASE']})

# Create container options
options = {
    'offerThroughput': 400
}

container_definition = {
    'id': config['CONTAINER']
}

# Create a container
container = client.CreateContainer(db['_self'], container_definition, options)

