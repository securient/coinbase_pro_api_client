import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class PrivateApi(object):

    def __init__(self, auth, url, proxy):
        self.auth = auth
        self.url = url
        self.proxy = proxy
        self.profile_ids = []
        self.account_ids = []

    def list_accounts(self):
        r = requests.get("{0}/accounts".format(self.url), auth=self.auth, proxies=self.proxy, verify=False)
        aresponse = r.text
        myresponse = json.loads(aresponse)

        for items in myresponse:
            self.profile_ids.append(items['profile_id'].encode('utf-8'))
            self.account_ids.append(items['id'].encode('utf-8'))

        print json.dumps(myresponse, indent=4, sort_keys=True)
        return self.profile_ids, self.account_ids

    def get_account(self, account):
        r = requests.get("{0}/accounts/{1}".format(self.url, account), auth=self.auth, proxies=self.proxy, verify=False)
        bresponse = r.text
        mybresponse = json.loads(bresponse)
        print json.dumps(mybresponse, indent=4, sort_keys=True)

    def account_history(self, account):
        r = requests.get("{0}/accounts/{1}/ledger".format(self.url, account), auth=self.auth, proxies=self.proxy, verify=False)
        bresponse = r.text
        mybresponse = json.loads(bresponse)
        if not mybresponse:
            print "[!] There are no activities to report"
        elif r.status_code != 200 and mybresponse['message'] == "NotFound":
            print "[!] Unable to find the given Account"
        else:
            print json.dumps(mybresponse, indent=4, sort_keys=True)

    def get_holds(self, account):
        r = requests.get("{0}/accounts/{1}/holds'".format(self.url, account), auth=self.auth, proxies=self.proxy, verify=False)
        bresponse = r.text
        mybresponse = json.loads(bresponse)
        if not mybresponse:
            print "[!] There are no holds for the given account"
        elif r.status_code != 200 and mybresponse['message'] == "NotFound":
            print "[!] Unable to find the given Account"
        else:
            print json.dumps(mybresponse, indent=4, sort_keys=True)

    def place_order(self, order):
        r = requests.post("{0}/orders".format(self.url), auth=self.auth, json=order, proxies=self.proxy, verify=False)
        print r.text

    def create_report(self, report):
        r = requests.post("{0}/reports".format(self.url), auth=self.auth, json=report, proxies=self.proxy, verify=False)
        print r.text, r.status_code

    def report_status(self, report_id):
        r = requests.get("{0}/reports/{1}".format(self.url, report_id), auth=self.auth, proxies=self.proxy, verify=False)
        print r.text