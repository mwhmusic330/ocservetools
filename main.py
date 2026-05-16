import requests


IP='127.0.0.1'
PORT='4096'
ENDPOINT=f"http://{IP}:{PORT}"

def checke_health():
    r = requests.get(ENDPOINT + "/global/health")
    return r.json()

def delete_session(sid):
    s = requests.delete(ENDPOINT + "/session/" + sid)

def create_session():
    c = requests.post(ENDPOINT + "/session/")
    return c.text()

def list_all_sessions():
    ls = requests.get(ENDPOINT + "/session")
    return ls.json()
def main():
    print(list_all_sessions())
if __name__ == "__main__":
    main()
