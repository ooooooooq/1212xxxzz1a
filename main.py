from deta import Deta
import requests
import json
import random
import os


# o8n5ib
deta = Deta("c0xo25ol_eHeWqyY39XuqFFKizJYg6D7FRNTmD94D")
users = deta.Base("OM")
counter = 0
errors = 0
print("[+] Starting...")

def get_names(number, country):
    try:
        url = f"https://devappteamcall.site/data/search_name?country={country}"
        payload = {
            'phoneNumber': number
        }
        headers = {
            'Authorization': 'Basic YWEyNTAyOnp1enVBaGgy',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G965N Build/QP1A.190711.020)',
            'Host': 'devappteamcall.site',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '21',
        }
        response = requests.post(url, headers=headers, data=payload)
        # print(response.text)
        if response.json()['errorDesc'] == "no data found":
            return "no data found"
        id_s = response.json()['result']
        jsona = json.loads(id_s)
        return jsona
    except Exception as e:
        raise e


def gen_num(number: str):
    for i in range(0, len(number)):
        if number[i] == "x":
            number = number[:i] + random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]) + number[i + 1:]
    return number


def main_func() -> None:
    global counter
    while 20000 > counter:
        try:
            num = gen_num("9xxxxxxx") or gen_num("7xxxxxxx")
            if users.fetch({"number": num}).count == 0:
                try:
                    names = get_names(num, "OM")
                    if names == "no data found":
                        print("no data found")
                        continue
                    else:
                        for i in range(0, len(names)):
                            users.insert({
                                "number": num,
                                "name": names[i]['Name'],
                            })
                        counter += 1
                        print(f"[+] {counter} - {num}")
                except KeyboardInterrupt:
                    break
                except Exception as e:

                    print(e)
                    continue
            else:
                continue
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(e)
            continue
    print("[+] Done")


if "__main__" == __name__:
    main_func()
