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

subparsers = parser.add_subparsers(dest='command', help='subcommand help')

parser.add_argument('-d', '--delete')
parser.add_argument('-m', '--message')
parser.add_argument('-l', '--list', action='store_true')

parser_status = subparsers.add_parser('status', help= 'status help')
parser_add = subparsers.add_parser('add', help= 'add help')
parser_statusall = subparsers.add_parser('all', help= 'all help')
parser_test = subparsers.add_parser('test', help= 'all help')


def make_request(method: str ='GET', endpoint: str ='', data=None) -> dict:
    r = requests.request(method, BASE_URL + endpoint, json=data)
    return r.json()

def find_session_id(slug: str) -> str:
    ls = make_request(endpoint="/session")
    slug = slug.lower()
    for item in ls:
        if item["slug"] == slug:
            return item["id"]
    return "slug not found"

def check_health() -> None:
    r = make_request(endpoint="/global/health")
    print(r)

def delete_session(sid: str) -> None:
    s = make_request('DELETE',"/session/" + sid)
    print(s)

def create_session() -> None:
    c = make_request('POST',"/session")
    print(c)

def send_message_wait(sid: str, message: str) -> None:
    data = {"parts": [{"type": "text", "text": message}]}
    c = make_request('POST',f"/session/{sid}/message", data=data)
    for item in c:
        print(item)

def status_sessions() -> None:
    ss = make_request(endpoint="/session/status")
    print(ss)

def list_all_sessions() -> None:
    ls = make_request(endpoint="/session")
    for item in ls:
        print(f'{item["slug"]}, {item["title"]}')

def main():
    args = parser.parse_args()
    if args.command == 'status':
        check_health()
    if args.command == 'add':
        create_session()
    if args.command == 'all':
        status_sessions()
    if args.delete:
        sid = find_session_id(args.delete)
        delete_session(sid)
    if args.message:
        slug = input("Input slug here:").lower()
        sid = find_session_id(slug)
        send_message_wait(sid, args.message)

    if args.list:
        list_all_sessions()
    if args.command == 'test':
       slug = input("Input slug here:").lower()
       sid = find_session_id(slug)
       send_message_wait(sid)
if __name__ == "__main__":
    main()
