from configparser import RawConfigParser
import ast

rcp = RawConfigParser()
rcp.read('./config/config.cfg')
Connect_list = rcp.get('zkConfig', 'Connect_list')

list_list = ast.literal_eval(Connect_list)
num = len(list_list)
a = {123:123}
b = 'ASD : FBG SSD'
print(b.replace(' ',''))
# print(a.values())
# for aa in a:
#     print(aa)