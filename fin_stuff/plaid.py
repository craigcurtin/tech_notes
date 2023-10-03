
#pip install plaid-python

import plaid
from plaid.api import plaid_api

# Available environments are
# 'Production'
# 'Development'
# 'Sandbox'
configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': "6379ff4660579b0013a77c14",
        'secret': "95a8f8027645a1228015b1f6c701d7",
    }
)

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

from plaid.model.country_code import CountryCode
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.products import Products
import time

CLIENT_NAME = 'Plaid Test'

request = LinkTokenCreateRequest(
        products=[Products('auth'), Products('transactions')],
        client_name=CLIENT_NAME,
        country_codes=[CountryCode('GB')],
        language='en',
        user=LinkTokenCreateRequestUser(
            client_user_id=str(time.time())
        )
    )
# create link token
response = client.link_token_create(request)

# assert on response
link_token = response['link_token']



from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.products import Products

SANDBOX_INSTITUTION = 'ins_109508'

pt_request = SandboxPublicTokenCreateRequest(
        institution_id=SANDBOX_INSTITUTION,
        initial_products=[Products('auth')]
    )

pt_response = client.sandbox_public_token_create(pt_request)

exchange_request = ItemPublicTokenExchangeRequest(
    public_token=pt_response['public_token']
)

import plaid
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest

# the public token is received from Plaid Link
exchange_request = ItemPublicTokenExchangeRequest(
    public_token=pt_response['public_token']
)
exchange_response = client.item_public_token_exchange(exchange_request)
access_token = exchange_response['access_token']

from plaid.model.account_type import AccountType
from plaid.model.accounts_get_request import AccountsGetRequest

accounts_request = AccountsGetRequest(
    access_token=access_token
)
accounts_response = client.accounts_get(accounts_request)

account = next(
    acct for acct in accounts_response['accounts'] if acct['type'] == AccountType('depository'))

account_id = account['account_id']

from plaid.model.bank_transfer_create_request import BankTransferCreateRequest
from plaid.model.bank_transfer_network import BankTransferNetwork
from plaid.model.bank_transfer_idempotency_key import BankTransferIdempotencyKey
from plaid.model.bank_transfer_type import BankTransferType
from plaid.model.bank_transfer_user import BankTransferUser
from plaid.model.ach_class import ACHClass
from random import random

bt_request = BankTransferCreateRequest(
        idempotency_key=BankTransferIdempotencyKey(str(random())),
        access_token=access_token,
        account_id=account_id,
        type=BankTransferType('credit'),
        network=BankTransferNetwork('ach'),
        amount='1.00',
        iso_currency_code='USD',
        description='test',
        user=BankTransferUser(legal_name='Firstname Lastname'),
        ach_class=ACHClass('ppd'),
        custom_tag='',
    )

bt_response = client.bank_transfer_create(bt_request)

