

import typing

from .credit_card_credential_response import CreditCardCredentialResponse
from .password_credential_response import PasswordCredentialResponse
from .secret_credential_response import SecretCredentialResponse

CredentialResponseCredential = typing.Union[
    PasswordCredentialResponse, CreditCardCredentialResponse, SecretCredentialResponse
]
