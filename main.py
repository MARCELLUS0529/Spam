import time
import requests
import threading

# The message to send
message = "@everyone"  # Mention yourself

# New list of webhooks
webhook_urls = [
    "https://discord.com/api/webhooks/1336947213817090139/2BByVLW9WO0HhcHSgRHJOz7rL0S2UNOGNDJ2BqJEqNEfiDj2ADapZGyA-UfDv7hyWfY_",
    "https://discord.com/api/webhooks/1336950310874120222/xO3BJIC7jmCFzA2Vyxd9gSBWxCg5dHC5YZyAX8wduibi0jezBi7FFINNMRSF0xImKfE9",
    "https://discord.com/api/webhooks/1336950337818464326/WDIZRCOyMP7rI607YIInk1GRr5CBg9iGPZAvQnChk2XJSe92JOU2g0oGqEdr3-apzHDT",
    "https://discord.com/api/webhooks/1336950349721894953/bKt3S3Jsp3Uayux-5cpwqt5PK80IW-o0SjQAKtouu4AbtmzMNICA_025PDRh73jNXgMd",
    "https://discord.com/api/webhooks/1336950359708536942/XLXXpMO5rKbrNHUutVV0BrsSpSMTdJoz2surayqq40IZOe55JH1GK5RsiwKzK-qbmsrY",
    "https://discord.com/api/webhooks/1336950363420491879/JmOEKRoXaM2nz2LNT7VVfzUoh1TJAXiR9QL4ii7BeRv86lxFU9aLZMLyM4IwKjw8iJs2",
    "https://discord.com/api/webhooks/1337439929629802497/EAxVZUwbOD0Ld4mboYdUpQQDMIpMaga5wEweS5i9iZNO72tlRpDJ-Xq5BKqinqvFZ8HS",
    "https://discord.com/api/webhooks/1337439965327392880/QyKghHDgJYtC_rPxkRej5jSvmRRWHsy2z0pt3OxoW2Cf9rKMVNhiL3BwAGKTBpPpsi7d",
    "https://discord.com/api/webhooks/1336947213817090139/2BByVLW9WO0HhcHSgRHJOz7rL0S2UNOGNDJ2BqJEqNEfiDj2ADapZGyA-UfDv7hyWfY_",

    "https://discord.com/api/webhooks/1337440243703611412/LBMx4Bu9MN4OSwU6I0JrSy8NaxU00Ehpf5H5_LaEqa530k8fLiyyIKj34kc6fRCnSUpx",
    "https://discord.com/api/webhooks/1337440246157017138/BicYmFegzipIYFghnMYdnYqmHXcCdFo3o2Xxv4AFoF6F3ZiMdqUASIZX6oMEFnxHm4VL",

    "https://discord.com/api/webhooks/1337440249315328060/CG9NsNnoVaeUzadX-x3Yn0JDYF4XWqdQqkR06qxRPBiAVIJiZoDfDnF5WV32KVTTlT5w",

    "https://discord.com/api/webhooks/1337440251286917140/xi41lRmPiR8Z9PlUKgJ5Ul3YppRc-Vo-iOR0EjlvGkb1qdI8whyZcu2K6omtI4nCtPEu",
    "https://discord.com/api/webhooks/1337440257708396739/Fv10_lZayZ0c86jrE5ACFkBPMXSq-LVv1B-iemAI85osE-F7gZwuJ16iWY_lH5tWv9we",

    "https://discord.com/api/webhooks/1337440260648337479/X4He9EmyOkW2631FL3p72ddI2faQgQIqXVkHpXg8NKYdrSkrwKzpMYNHxXvWo5sw_AY1",

"https://discord.com/api/webhooks/1337440260648337479/X4He9EmyOkW2631FL3p72ddI2faQgQIqXVkHpXg8NKYdrSkrwKzpMYNHxXvWo5sw_AY1",

    "https://discord.com/api/webhooks/1337440261986582530/j-ULlnoYiU5G6YzhnL4SSsLGEzd3PqZN7NVUc_t25TEgr7GAVaSc1BMt1rNRgsw6YBY0",
    "https://discord.com/api/webhooks/1337441971190497351/slIoP6swrQA8sV4K7GCx0RzS2L9acwVy22SPOf_0AMwKp4fZYJyKAnw48qRl1oTgut4o",
    "https://discord.com/api/webhooks/1337441977595330600/iF-snjwsgN7OeZYPDYRf5rigfcaurLhZ5JEgmVYrgNBzoLQAsA_nMyIAEhxZNFTD0eXs",
    "https://discord.com/api/webhooks/1337441978031538287/B7gsv-aUpwuWnAoy82OAsbc1Ba2sX_AZypzD60mSqiWrUi9tSZ8AySiK_JDvAqn4RlXp",

"https://discord.com/api/webhooks/1337441980434616401/uhs3erUZKIq9YITfUMmvGyxmUPuy2JajW2LOM3gq4R3rjr7QfK5q_aGu_lDQf1YiTNKy",

    "https://discord.com/api/webhooks/1337441982683025448/hVm9qLZO62Q_zdtoweyp7lX3yU69I2gA56Qj-MYSmvG00H8tbDOqHypXC5-gscqvny-X",
    "https://discord.com/api/webhooks/1337441985312718978/9b6dGOnR65vZ-mwMtwkex6WEzCUoPwIPDc9845ox0d-YoX4__iCh1RdoPidfnNdscCMl",

    "https://discord.com/api/webhooks/1337441987166470245/P8nfrnrXsunCYL5bYp2dJVklvJbjeBqmEGjInRkzwyohLwLzZR7bpXdlpgeGGL11WmGk",

    "https://discord.com/api/webhooks/1337441988957569124/pk3fe5aWF2i_sIf75QWiUCu5dIqL-BZY_k046_VDWEOAyvjmUrePoeWbZM_c17Od5wsX",

    "https://discord.com/api/webhooks/1337441991469830164/ukhmALL0bHqCDRMMNB9tt3_Sl4EPbUboGfAxoV5sglQoo-_fz1xgNcubb2a4xS2OA5CJ",

    "https://discord.com/api/webhooks/1337441993084895353/YQfOsaaLoKAEDNGYu18n6z7mDNXgX4E0H-E7a2xxZxeHm_E13f7VaL4kukh4grvDwHSl",

    "https://discord.com/api/webhooks/1337441995588636785/eWSwrCQNXIPskWvHzAPVQ8zTSch4J-_Qry6sL2ZJ7HdRihTBdJWRrzfGMlZTyrB3L7w6",

    "https://discord.com/api/webhooks/1337441996972757002/rmVmhtFFw_VGaKJMoCHsd5NtQGWP7H6waz-nawMHuICWX-iPAb0lrwmTX_h1yV_7Qp3a",

    "https://discord.com/api/webhooks/1337441998738690109/aiTR_hKMD_Wr72Y4U844_r2vzH62-AJSSQPAQDYMi1caqF_vYyjyxU-X55E1vVn4GOU_",
]

# Function to send the message
def send_message(webhook, message):
    payload = {"content": message}
    try:
        response = requests.post(webhook, json=payload)
        if response.status_code == 429:  # Rate limited
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

# Function to send messages to all webhooks simultaneously
def send_messages():
    threads = []
    for webhook in webhook_urls:
        thread = threading.Thread(target=send_message, args=(webhook, message))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

# Main function to send messages every second
def main():
    while True:
        send_messages()  # Send all webhooks at the same time
        time.sleep(2)  # Wait 1 second before sending again

if __name__ == "__main__":
    main()
  
