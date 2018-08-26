import argparse


class UserInput(object):
    """
    This class handles user input from the CLI.
    """

    def __init__(self):

        self.args = argparse.ArgumentParser(description='Coinbase Pro client, access Private & Market Data endpoints')
        self.args.add_argument('--yaml_auth', help='yaml file with api secret, key and passphrase for authentication', required=True)
        self.args.add_argument('--list_accounts', help='list available accounts', required=False, action='store_true')
        self.args.add_argument('--get_account', help='get a specific account detail, requires account_id', required=False, action='store_true')
        self.args.add_argument('--account_id', help='get a specific account detail', required=False)
        self.args.add_argument('--account_history', help='display account history', required=False, action='store_true')
        self.args.add_argument('--get_holds', help='get account holds', required=False, action='store_true')
        self.args.add_argument('--place_order', help='place a new order', required=False, action='store_true')
        self.args.add_argument('--order_size', help='place a new order', required=False)
        self.args.add_argument('--order_price', help='place a new order', required=False)
        self.args.add_argument('--cancel_order', help='cancel an order', required=False, action='store_true')
        self.args.add_argument('--cancel_all', help='cancel all orders', required=False, action='store_true')
        self.args.add_argument('--list_orders', help='list all orders', required=False, action='store_true')
        self.args.add_argument('--get_order', help='get an order', required=False, action='store_true')
        self.args.add_argument('--list_files', help='list all files', required=False, action='store_true')
        self.args.add_argument('--deposit_fund', help='deposit funds from payment method', required=False, action='store_true')
        self.args.add_argument('--deposit_from_cb', help='deposit funds from coinbase account', required=False, action='store_true')
        self.args.add_argument('--withdraw_payment', help='withdraw funds to payment method', required=False, action='store_true')
        self.args.add_argument('--withdraw_coinbase', help='withdraw funds to coinbase', required=False, action='store_true')
        self.args.add_argument('--withdraw_crypto', help='withdraw funds to crypto address', required=False, action='store_true')
        self.args.add_argument('--list_payments', help='list payment methods', required=False, action='store_true')
        self.args.add_argument('--coinbase_accounts', help='list coinbase accounts', required=False, action='store_true')
        self.args.add_argument('--create_report', help='create reports of historic information', required=False, action='store_true')
        self.args.add_argument('--start_time', help='create reports of historic information', required=False)
        self.args.add_argument('--end_time', help='create reports of historic information', required=False)
        self.args.add_argument('--get_report_status', help='get report status', required=False, action='store_true')
        self.args.add_argument('--report_id', help='get report status', required=False)
        self.args.add_argument('--trailing_volume', help='get 30 day trailing volume', required=False, action='store_true')