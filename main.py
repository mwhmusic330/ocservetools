import requests
import argparse


IP='127.0.0.1'
PORT='4096'
BASE_URL=f"http://{IP}:{PORT}"
parser = argparse.ArgumentParser(
    prog='ocs',
    description='cli tool for opencode server',
    epilog='idk dude, we just built this.'
)

subparsers = parser.add_subparsers(help='subcommand help')

parser.add_argument('-s', '--status', action='store_true')
parser.add_argument('-a', '--add', action='store_true')
parser.add_argument('-d', '--delete', action='store_true')
parser.add_argument('-l', '--list', action='store_true')

parser_a = subparsers.add_parser('status', help= 'status help')
parser_b = subparsers.add_parser('add', help= 'add help')


def make_request(method: str ='GET', endpoint: str ='') -> dict:
    r = requests.request(method, BASE_URL + endpoint)
    return r.json()

def check_health():
    r = make_request(endpoint="/global/health")
    print(r)

def delete_session(sid):
    s = make_request('DELETE',"rsession/" + sid)
    print(s)

def create_session():
    c = make_request('POST',"/session")
    print(c)

def list_all_sessions():
    ls = make_request(endpoint="/session")
    for item in ls:
        print(f"{item["id"]}, {item["title"]}")

def main():
    args = parser.parse_args()
    if parser_a:
        check_health()
    if parser_b:
        create_session()
    if args.delete:
        delete_session(sid)
    if args.list:
        list_all_sessions()
if __name__ == "__main__":
    main()
