

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BankTransferUser(UniversalBaseModel):
    """
    The legal name and other information for the account holder.
    """

    email_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account holder’s email.
    """

    legal_name: str = pydantic.Field()
    """
    The account holder’s full legal name. If the transfer `ach_class` is `ccd`, this should be the business name of the account holder.
    """

    routing_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account holder's routing number. This field is only used in response data. Do not provide this field when making requests.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
