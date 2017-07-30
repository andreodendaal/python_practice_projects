import requests


def main():

    url = 'https://talkpython.fm/'
    try:
        resp = requests.get(url)
    # print(resp)

    if resp.status_code != 200:
        print("Error processing {}, code {}".format(url, resp.status_code))
        return

    print(resp.text[:500])

if __name__ == '__main__':
    main()