from abc import abstractmethod, ABC


class Core(ABC):

    @abstractmethod
    def xml_data(self):
        pass


class StockData(Core):

    def xml_data(self):
        return "XML Data"
    pass

class XmlToJsonAdapter:

    def __init__(self, stock_data):
        self.stock_data = stock_data


    def convert_xml_to_Json(self):
        xml_data = self.stock_data.xml_data()
        json_data = self.xml_to_json_conversion_logic(xml_data)
        return json_data

    def xml_to_json_conversion_logic(self, xml):
        return ("JSON data")


class Charts(ABC):
    @abstractmethod
    def charts(self):
        pass


# third party lib that excepts Json data

class AnalyticalJsonLib(Charts):
    def charts(self, json_data):
        self.json_data = json_data
        if self.json_data == "JSON data":
            return "Beautiful Charts"


stock_data = StockData()
xml_to_json = XmlToJsonAdapter(stock_data)
converted_xml_to_josn = xml_to_json.convert_xml_to_Json()


analytics = AnalyticalJsonLib()
chart = analytics.charts(converted_xml_to_josn)
print(chart)
