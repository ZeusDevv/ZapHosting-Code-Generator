from urllib import request
import aiohttp, asyncio, sys, os, time
from requests.structures import CaseInsensitiveDict
from aiohttp import ClientSession

url = "https://zap-hosting.com/interface/shop/_ajax/json_getExitIntentCoupon.php"

headers = CaseInsensitiveDict()
headers["accept"] = "application/json, text/javascript, */*; q=0.01"
headers["accept-encoding"] = "gzip, deflate, br"
headers["accept-language"] = "en-GB,en-US;q=0.9,en;q=0.8"
headers["content-length"] = "4"
headers["Content-Type"] = "application/x-www-form-urlencoded"
headers["origin"] = "https://zap-hosting.com"
headers["referer"] = "https://zap-hosting.com/en/"
headers["sec-ch-ua"] = """.Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"""
headers["sec-ch-ua-mobile"] = "?0"
headers["sec-ch-ua-platform"] = """macOS"""
headers["sec-fetch-dest"] = "empty"
headers["sec-fetch-mode"] = "cors"
headers["sec-fetch-site"] = "same-origin"
headers["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
headers["x-requested-with"] = "XMLHttpRequest"
data = "id=2"

class main(object):

    async def request(self):
        try:
            if sys.platform == "linux":
                os.system("clear")
            else:
                os.system("cls")

            print("\033[0m╥\n\033[0m║ \033[4m\033[92mZap Code Generator\n\033[0m║\n\033[0m║ \033[4m\033[34mAmount to generate\n\033[0m║")
            self.gen_amount = input("╚► ")

            if sys.platform == "linux":
                os.system("clear")
            else:
                os.system("cls")

            print("\033[0m╥\n\033[0m║ \033[4m\033[92mZap Code Generator\n\033[0m║\n\033[0m║\033[4m\033[34mProxy Type\033[0m\n\033[0m║\n\033[0m╠► \033[4m1.Auth\033[0m\n\033[0m╠► \033[4m2.No Auth\n\033[0m║")
            self.proxy_type = input("╚► ")

            if self.proxy_type == ("1"):
                proxie_file = open("proxies.txt").read().splitlines()
                for x in proxie_file:
                    user = x.split(":")[0]
                    password = x.split(":")[1]
                    ip = x.split(":")[2]
                    port = x.split(":")[3]
                    self.client_proxy = (f"http://{user}:{password}@{ip}:{port}")
                
            elif self.proxy_type == ("2"):
                proxie_file = open("proxies.txt").read().splitlines()
                for x in proxie_file:
                    ip = x.split(":")[0]
                    port = x.split(":")[1]
                    self.client_proxy = (f"http://{ip}:{port}")
            else:
                print("\nInvalid Proxy Type")
                sys.exit()
            
        except Exception as e:
            print(f"Error Happened -> {e}")

        try:
            if sys.platform == "linux":
                os.system("clear")
            else:
                os.system("cls")
            amount = int(self.gen_amount)
            print(f"\033[0m╥\n\033[0m║ \033[4m\033[92mZap Code Generator\n\033[0m║\n\033[0m╠► Generating {amount} Codes\n\033[0m╨")
            for x in range(amount):
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, data=data, proxy=self.client_proxy, ssl=False) as resp:
                        result = await resp.json(content_type='text/html')
                        code = result["data"]["code"]
                        with open ("codes.txt", "a+") as f:
                            f.write(code + "\n")
                            f.close
                        await aiohttp.ClientSession().close()
            if sys.platform == "linux":
                os.system("clear")
            else:
                os.system("cls")
            print(f"\033[0m╥\n\033[0m║ \033[4m\033[92mZap Code Generator\n\033[0m║\n\033[0m╠► Finished Generating {amount} Codes\n\033[0m╨")

                        
        except Exception as e:
            print(f"Error Happened -> {e}")

if __name__ == "__main__":
    start = main()
    asyncio.run(start.request())