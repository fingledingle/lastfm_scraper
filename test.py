import requests
from bs4 import BeautifulSoup
class GetProxy:
    def generate_proxy(self):
        proxy_list = []
        with open("http.txt", "r") as file:
            proxy_ugly = file.readlines()
            for proxies in proxy_ugly:
                proxy = proxies.strip()
                proxy_list.append(proxy)
        return proxy_list










        #DOESNT FUCKING WORK
        # regex = r"[0-9]+(?:\.[0-9]+){3}:[0-9]+"
        # c = requests.get("https://spys.me/proxy.txt")
        # test_str = c.text
        # a = re.finditer(regex, test_str, re.MULTILINE)
        # # with open("proxies_list.txt", 'w') as file:
        # #     for i in a:
        # #         print(i.group(), file=file)
        #
        # d = requests.get("https://free-proxy-list.net/")
        # soup = BeautifulSoup(d.content, 'html.parser')
        # td_elements = soup.select('.fpl-list .table tbody tr td')
        # ips = []
        # ports = []
        # proxy_list = []
        # for j in range(0, len(td_elements), 8):
        #     ips.append(td_elements[j].text.strip())
        #     ports.append(td_elements[j + 1].text.strip())
        #     for ip, port in zip(ips,ports):
        #         proxy = f"{ip}:{port}"
        #         proxy_list.append(proxy)
        # return proxy_list