

import typing

from .custom_identifier import CustomIdentifier
from .email_address import EmailAddress
from .government_id_number import GovernmentIdNumber
from .telephone_number import TelephoneNumber

RequiredAuthItemItem = typing.Union[TelephoneNumber, EmailAddress, GovernmentIdNumber, CustomIdentifier]
