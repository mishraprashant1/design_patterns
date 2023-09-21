import json
import xml.etree.ElementTree as et  # Python's built-in XML library


# Existing XML data source
class XMLDataSource:
    def get_data(self):
        # Simulate XML data retrieval
        xml_data = """<stock_data>
                        <stock>
                            <symbol>AAPL</symbol>
                            <price>150.32</price>
                        </stock>
                        <stock>
                            <symbol>GOOGL</symbol>
                            <price>2700.45</price>
                        </stock>
                    </stock_data>"""
        return xml_data


# 3rd-party analytics library that works with JSON data
class AnalyticsLibrary:
    def analyze_data(self, json_data):
        # Simulate data analysis
        print("Analyzing JSON data:")
        print(json_data)


# Adapter to convert XML data to JSON for the analytics library
class XMLToJSONAdapter:
    def __init__(self, xml_data_source):
        self.xml_data_source = xml_data_source

    def get_json_data(self):
        xml_data = self.xml_data_source.get_data()
        root = et.fromstring(xml_data)
        stock_list = []

        for stock_element in root.findall('stock'):
            symbol = stock_element.find('symbol').text
            price = float(stock_element.find('price').text)
            stock_data = {'symbol': symbol, 'price': price}
            stock_list.append(stock_data)

        return json.dumps(stock_list)


# Client code
xml_data_source = XMLDataSource()
adapter = XMLToJSONAdapter(xml_data_source)
json_data = adapter.get_json_data()

analytics = AnalyticsLibrary()
analytics.analyze_data(json_data)
