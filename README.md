# coinbase_pro_api_client

A minimalistic and modular implementation of coinbase pro api client. Make sure to provide valid API key, API secret and passphrase in the yaml file.

```$ python cbpro.py --help                                                                                                                                                                                                     ✔  2601  22:52:58
usage: cbpro.py [-h] --yaml_auth YAML_AUTH [--list_accounts] [--get_account]
                [--account_id ACCOUNT_ID] [--account_history] [--get_holds]
                [--place_order] [--order_size ORDER_SIZE]
                [--order_price ORDER_PRICE] [--cancel_order] [--cancel_all]
                [--list_orders] [--get_order] [--list_files] [--deposit_fund]
                [--deposit_from_cb] [--withdraw_payment] [--withdraw_coinbase]
                [--withdraw_crypto] [--list_payments] [--coinbase_accounts]
                [--create_report] [--start_time START_TIME]
                [--end_time END_TIME] [--get_report_status]
                [--report_id REPORT_ID] [--trailing_volume]

Coinbase Pro client, access Private & Market Data endpoints

optional arguments:
  -h, --help            show this help message and exit
  --yaml_auth YAML_AUTH
                        yaml file with api secret, key and passphrase for
                        authentication
  --list_accounts       list available accounts
  --get_account         get a specific account detail, requires account_id
  --account_id ACCOUNT_ID
                        get a specific account detail
  --account_history     display account history
  --get_holds           get account holds
  --place_order         place a new order
  --order_size ORDER_SIZE
                        place a new order
  --order_price ORDER_PRICE
                        place a new order
  --cancel_order        cancel an order
  --cancel_all          cancel all orders
  --list_orders         list all orders
  --get_order           get an order
  --list_files          list all files
  --deposit_fund        deposit funds from payment method
  --deposit_from_cb     deposit funds from coinbase account
  --withdraw_payment    withdraw funds to payment method
  --withdraw_coinbase   withdraw funds to coinbase
  --withdraw_crypto     withdraw funds to crypto address
  --list_payments       list payment methods
  --coinbase_accounts   list coinbase accounts
  --create_report       create reports of historic information
  --start_time START_TIME
                        create reports of historic information
  --end_time END_TIME   create reports of historic information
  --get_report_status   get report status
  --report_id REPORT_ID
                        get report status
  --trailing_volume     get 30 day trailing volume```
