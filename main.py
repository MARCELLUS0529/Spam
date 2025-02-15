import time
import requests
import threading

message = "@everyone"

webhook_urls = [
    "https://discord.com/api/webhooks/1340455482636369972/Y4JF1a2g04ig9Pz2DojZddT6BCxj1_lZ3umgXcA3MuEnZQr9QwbyWmey0pJuQeH844Vb",
    "https://discord.com/api/webhooks/1340455503754694737/MOXaUqPOI3n5L4_kYfn900WuhW9tfD5SUnAA6gGH8Ilb35eyLALWX0nrsX_uV9if0u4b",
    "https://discord.com/api/webhooks/1340455504543219762/aIg-epCPHo54uXfr5y-KysGDTPGfmjsklsFu0Ql-sdq-vljCZC9uXkgwiQ2sYXEPk3is",
    "https://discord.com/api/webhooks/1340455505356918785/HTLfIM_XT2DvvpKCgIz-GFOnc5IOwpKttMf2rmdp7cN-5Gp6sWvDlSv4z5GCXUtClPl5",
    "https://discord.com/api/webhooks/1340455506266947764/WgzTO1c1oYXyNdYl0NPb0KnT7cwh1sTvAaMML4D2ly__HsEaQE815lWt9egnxQEqO2ti",
    "https://discord.com/api/webhooks/1340455506761879673/CMLhRDjAZANJHCU9J9-x1mueTqjKlO4O-xI-vkyQDt9x1GamEEjHIMRc7vg-Ioan5vca",
    "https://discord.com/api/webhooks/1340455507533631550/V45m1WksRfl9nMYvPTwYiwCV9zQG-sMKdbJ3ZSWDuebSkTFxpDMIGbP3EK0q86X3bY-t",
    "https://discord.com/api/webhooks/1340455508448116779/VLOP5iB6h39ysoXdecg30e74r9nLstG4_szCrjURFXoi87ToOA8OdtkJ8BkGy92xNBhI",
    "https://discord.com/api/webhooks/1340455509127467072/2hTvrOU3EyP_Ba8wt64l2bmvfBtbUh1HskKsQ2n5XJahe5OeQSo5P8rpPLtzgebiUGbB",

    "https://discord.com/api/webhooks/1340455509999751198/KvhHrPs6SuRe_Ki8mfkO8TyEt1stc2qyxASb39IiU80s3sBTDpQoNAtN9ePW7hnITfuF",
    "https://discord.com/api/webhooks/1340455510863904869/vYimVoeSDU9O99QTah8of9eLU821fawn5L1ZWqrhIoX7i0zzrMaeCuZcsPwaBWkxpCr-",

    "https://discord.com/api/webhooks/1340456878198493204/wW0QZ6rr6L-QiNxn_Tt6QXJVjK5wVUBvmS-2umwXDYS-4KwygmIWSqlA_ITtX9SLIQ8v",

    "https://discord.com/api/webhooks/1340456883982434426/TWqzKwxFMD8qVkzry2DAjWtPM2A604mf2tzXmtPHkmSW52UCIcP8_xvY_j3-66cqPBPB",
    "https://discord.com/api/webhooks/1340456887522693261/ogyibZPLApr-AHejUxY_78UoBqn3boG63_hqeWxrLFu3zH_i1vDjHMpnTViMSF-j1eH1",

    "https://discord.com/api/webhooks/1340456889753927701/my2cE1jw397bGzIASywCeH9N5kXt461GVszE2uO0Hr9fwA0Df5xi4f6WVFe4htk1-Y2B",

"https://discord.com/api/webhooks/1340456895512576162/kF6iiA2yfr3RDzwH1F2wqsnN7zR6encpfdsVHE91FkrWcmqh-qQdldLh757H06ozshm6",

    "https://discord.com/api/webhooks/1340456900138893554/cuC5aHgzZCe-iTZotR3wX4ODsNQKzN0bafveaLE6o79MQM3f0uD0baUXq4H60iTOzXuU",
    "https://discord.com/api/webhooks/1340456959639289947/sqszySycwvQJDPkZmNvTP6Rpzyekz2gFoX1zvGEnL24PlTXOtj29hWpGkFrNarBQS9Nj",
    "https://discord.com/api/webhooks/1340456960994181251/hWjPcWhpTbO0-f92awnP2Z84IuUZlpKHVynqYZHET5-9G8ua8-BnrtkwywNp3l-9eVWX",
    "https://discord.com/api/webhooks/1340456961451495444/8UtiDzmjpRxp2g7KLs6K9xkc-jJkI62CY3IRU3_PoraGdDNc1HE5ZcYOOs14U8g53W9i",

"https://discord.com/api/webhooks/1340456961959006289/v9AiJPq3SfZ_r8-0umaJ0H9eUK16G74NOrhnNJrHw74scncsgEmqFS5iAZ9ttqxgrNIl",

    "https://discord.com/api/webhooks/1340456962676097185/43g2gijgrS8N0-Zsno_Z80KNRrB0jxARh9OCyM7ziJWLenDrTPtkGEzgJLWlSgnKJDfy",
    "https://discord.com/api/webhooks/1340456963649175594/RouKznDTRIHvzQSjIOhfRsxRu2injNd8g6uL0EDsOvynsnvCHDL4l6_Qfj6vCNErTk-l",

    "https://discord.com/api/webhooks/1340456965033295912/jrbI0a_-N0GpcVKU1vEpdhcInxWxS8rh2i0p16e8CAxKUllbkiVkdaRg97BcUAuF7XRo",

    "https://discord.com/api/webhooks/1340456965653926030/-Pdqqi507Ewq25LAv1DvAG3o4d8libcvptRCeHMXEYoFgSYO-znQby5LBlOpcy6V_w0G",

    "https://discord.com/api/webhooks/1340457855740018800/AODvYi9KWVgw5-4US8lEFmrdv1g41YMLz7OL4HCUTmLduxtvP2SR6LMOZqgGOUWee62e",

    "https://discord.com/api/webhooks/1340457856654250044/Tkl7IDpzmg4s2-uN4a1RHttHLz-hNCIV52H6wgTduaQDtxkf6qAwZ3ApRvc6gyF4VvHK",

    "https://discord.com/api/webhooks/1340457857283522661/Wf_OuvqAMglsYG0Paurq0GcwigpvduN58yWIbT8z5CVcIuVoyYyIr-bHZHq-FCi5R4iP",

    "https://discord.com/api/webhooks/1340457857832714280/2DamneQCfR5s1Ar0PcSbGf5t4-HcvPRzfgTHEj3lKrauSFA89O0sD28szaJTG8pjQKVj",

    "https://discord.com/api/webhooks/1340457857283522661/Wf_OuvqAMglsYG0Paurq0GcwigpvduN58yWIbT8z5CVcIuVoyYyIr-bHZHq-FCi5R4iP",
]

def send_message(webhook, message):
    payload = {"content": message}
    try:
        response = requests.post(webhook, json=payload)
        if response.status_code == 429:
            print(f"Rate limited on {webhook}, retrying...")
            return False
        elif response.status_code != 204:
            print(f"Failed to send message to {webhook}. Status code: {response.status_code}")
            return False
        else:
            print(f"Message sent to {webhook}")
            return True
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return False

def send_messages():
    threads = []
    for webhook in webhook_urls:
        thread = threading.Thread(target=send_message, args=(webhook, message))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

def main():
    while True:
        send_messages()
        time.sleep(2)

if __name__ == "__main__":
    main()
  
