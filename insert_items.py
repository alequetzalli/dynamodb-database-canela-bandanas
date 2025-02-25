import boto3

# boto3 is the AWS SDK library for Python.
# The "resources" interface allow for a higher-level abstraction than the low-level client interface.
# More details here: http://boto3.readthedocs.io/en/latest/guide/resources.html
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Bandanas')


# The BatchWriteItem API allows us to write multiple items to a table in one request.
with table.batch_writer() as batch:
    batch.put_item(Item={"Color": "hot pink", "Material": "cotton",
        "Shade": "dark::hot pink", "Formats": { "ISBN": "B07VWV4M3R"} })

    batch.put_item(Item={"Color": "red", "Material": "cotton",
        "Shade": "dark::red", "Formats": { "ISBN": "B07VWV4M4R"} })

    batch.put_item(Item={"Color": "black", "Material": "cotton",
        "Shade": "dark::black", "Formats": { "ISBN": "B07VWV4M5R"} })

    batch.put_item(Item={"Color": "soft pink", "Material": "cotton",
        "Shade": "pastel::soft pink", "Formats": { "ISBN": "B07VWV4M6R"} })

    batch.put_item(Item={"Color": "lilac", "Material": "cotton",
        "Shade": "partel::lilac", "Formats": { "ISBN": "B07VWV4M7R"} })
    
    batch.put_item(Item={"Color": "navy blue", "Material": "cotton",
        "Shade": "dark::navy blue", "Formats": { "ISBN": "B07VWV4M9R"} })

    batch.put_item(Item={"Color": "light grey", "Material": "velvet",
        "Shade": "pastel::light grey", "Formats": { "ISBN": "B01VWV4M3R"} })

    batch.put_item(Item={"Color": "baby blue", "Material": "cotton",
        "Shade": "pastel::baby blue", "Formats": { "ISBN": "B02VWV4M3R"} })

    batch.put_item(Item={"Color": "orange", "Material": "velvet",
        "Shade": "dark::orange", "Formats": { "ISBN": "B03VWV4M3R"} })  

    batch.put_item(Item={"Color": "dark purple", "Material": "cotton",
        "Shade": "dark::dark purple", "Formats": { "ISBN": "B04VWV4M3R"} })

    batch.put_item(Item={"Color": "kelly green", "Material": "cotton",
        "Shade": "dark::kelly green", "Formats": { "ISBN": "B05VWV4M3R"} })

    batch.put_item(Item={"Color": "yellow", "Material": "velvet",
        "Shade": "dark::yellow", "Formats": { "ISBN": "B06VWV4M3R"} })

    batch.put_item(Item={"Color": "brown", "Material": "cotton",
        "Shade": "dark::brown", "Formats": { "ISBN": "B08VWV4M3R"} })

    batch.put_item(Item={"Color": "light yellow", "Material": "velvet",
        "Shade": "pastel::light yellow", "Formats": { "ISBN": "B09VWV4M3R"} })

    batch.put_item(Item={"Color": "white", "Material": "cotton",
        "Shade": "pastel::white", "Formats": { "ISBN": "B07VWV5M3R"} })
