import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

# opening up connection, grabbing the page
uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each container
containers = page_soup.findAll("div", {"class":"item-container"})
print(containers)

file_name = 'products.csv'
f = open(file_name, 'w')
headers = "brand, product_name, shipping\n"
f.write(headers)

for container in containers:
    brand_container = container.findAll('a',{"class":"item-brand"})
    brand = brand_container[0].img["title"]

    product_name = container.a.img["title"]

    shipping_container = container.findAll("li", {'class':'price-ship'})
    shipping = shipping_container[0].text.strip()

    # print('brand:',brand)
    # print('name:',product_name)
    # print('shipping :',shipping)
    # print("\n")

    f.write(brand + ", " + product_name.replace(",", " |") + ", " + shipping + "\n")
f.close()