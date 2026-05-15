import requests


IP='127.0.0.1'
PORT='4096'
ENDPOINT=f"http://{IP}:{PORT}"

def checke_health():
    r = requests.get(ENDPOINT + "/global/health")
    return r.json()

def delete_session(sid):
    s = requests.delete(ENDPOINT + "/session/" + sid)

def main():
    print(checke_health())
if __name__ == "__main__":
    main()
