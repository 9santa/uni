import json
from json2xml import json2xml # библиотека для конвертации json -> xml

with open("input.json", "r", encoding='utf-8') as file: # открываем готовый json файл
	json_file = json.load(file)

for i in json_file: # для наглядности работы программы, выводим сначала json
	print(i)

xml_file = (json2xml.Json2xml(json_file).to_xml()) # конвертируем json в xml формат

with open("output.xml", "r+", encoding='utf-8') as f: # создаем и записываем xml в новый файл output.xml
    xml_output = f.read()
    f.seek(0)
    f.write(xml_file)
    f.truncate()

print('\n', xml_output) # выводим готовый конвертированный файл xml формата