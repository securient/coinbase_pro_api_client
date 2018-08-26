import yaml
import sys
from core import UserInput
from authentication import CoinbaseExchangeAuth
from private import PrivateApi

if __name__ == '__main__':
    user_input = UserInput()
    args = user_input.args.parse_args()

    yamlfile = args.yaml_auth
    api_url = 'https://api-public.sandbox.pro.coinbase.com'
    dictfile = open(yamlfile, "rb")
    ymfile = yaml.load(dictfile)
    dictfile.close()
    auth = CoinbaseExchangeAuth(ymfile['cbpro']['api_key'], ymfile['cbpro']['api_secret'], ymfile['cbpro']['passphrase'])
    proxies = {
      'http': 'http://127.0.0.1:8080',
      'https': 'http://127.0.0.1:8080',
    }

    privapi = PrivateApi(auth=auth, url=api_url, proxy=proxies)

    if args.list_accounts:
        privapi.list_accounts()

    if args.get_account:
        if not args.account_id:
            print "[!] Missing Account ID"
        else:
            privapi.get_account(account=args.account_id)

    if args.account_history:
        if not args.account_id:
            print "[!] Missing Account ID"
        else:
            privapi.account_history(account=args.account_id)

    if args.get_holds:
        if not args.account_id:
            print "[!] Missing Account ID"
        else:
            privapi.get_holds(account=args.account_id)

    if args.place_order:
        order = {
            'size': args.order_size,
            'price': args.order_price,
            'side': 'buy',
            'product_id': 'BTC-USD',
        }
        privapi.place_order(order=order)

    if args.create_report:
        report = {
            "type": "account",
            "start_date": args.start_time,
            "end_date": args.end_time,
            "account_id": args.account_id
        }
        privapi.create_report(report=report)

    if args.get_report_status:
        privapi.report_status(report_id=args.report_id)