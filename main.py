import requests
import argparse


IP='127.0.0.1'
PORT='4096'
ENDPOINT=f"http://{IP}:{PORT}"
parser = argparse.ArgumentParser(
    prog='ocs',
    description='cli tool for opencode server',
    epilog='idk dude, we just built this.'
)
parser.add_argument('-s', '--status', action='store_true')
parser.add_argument('-a', '--add', action='store_true')
parser.add_argument('-d', '--delete', action='store_true')
parser.add_argument('-l', '--list', action='store_true')
def check_health():
    r = requests.get(ENDPOINT + "/global/health")
    print(r.json())

def delete_session(sid):
    s = requests.delete(ENDPOINT + "/session/" + sid)
    return s

def create_session():
    c = requests.post(ENDPOINT + "/session")
    return c.json()

def list_all_sessions():
    ls = requests.get(ENDPOINT + "/session")
    data = ls.json()
    for item in data:
        print(f"{item["id"]}, {item["title"]}")

def main():
    args = parser.parse_args()
    if args.status:
        check_health()
    if args.add:
        print(checke_health())
    if args.delete:
        print(checke_health())
    if args.list:
        list_all_sessions()

if __name__ == "__main__":
    main()
