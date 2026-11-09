

import typing

from .depository_account_subtype import DepositoryAccountSubtype

DepositoryAccountSubtypes = typing.List[DepositoryAccountSubtype]
"""
An array of account subtypes to display in Link. If not specified, all account subtypes will be shown. For a full list of valid types and subtypes, see the [Account schema](https://plaid.com/docs/api/accounts#account-type-schema). 
"""
