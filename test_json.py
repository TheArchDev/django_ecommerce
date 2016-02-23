import requests
url_all_products = "http://127.0.0.1:8000/products/?format=json"

json_data_all_products = requests.get(url_all_products).json()

print "\nall products json:", json_data_all_products

url_individual_product = "http://127.0.0.1:8000/products/3/?format=json"

json_data_individual_product = requests.get(url_individual_product).json()

print "\ninvidual product number 3 json:", json_data_individual_product