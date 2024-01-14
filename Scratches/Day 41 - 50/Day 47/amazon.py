from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.es/Lady-Tans-Circle-Women-English-ebook/dp/B0BNJM1MHF/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w" \
      "=KlfBB&content-id=amzn1.sym.0a30e528-1d52-494b-a476-0036b426e4e0&pf_rd_p=0a30e528-1d52-494b-a476-0036b426e4e0" \
      "&pf_rd_r=XB8VRVGTVVJTEAWYCF20&pd_rd_wg=BRJU8&pd_rd_r=5f3dda1a-4b1f-4f65-8fbf-8e411727cf3b&pd_rd_i=B0BNJM1MHF"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(url=url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("€")[1]
price_as_float = float(price_without_currency)
print(price_as_float)
