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







# class UsPlugs:
#     def charge(self):
#         return "Charging"


# class PkPlugs:
#      def charge(self):
#         return "Charging"
     

# class PlugAdapter:
#     def __init__(self, plug):
#         self.plug = plug

#     def charge(self):
#         return self.plug.charge()

#     pass

# us_plug = UsPlugs()
# pk_plug = PkPlugs()

# adapter = PlugAdapter(us_plug)
# print(adapter.charge())  # Output: Charging with US plug

# # Adapter wraps the PK plug
# adapter = PlugAdapter(pk_plug)
# print(adapter.charge())  # Output: Charging with PK plug
