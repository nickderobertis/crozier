

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .accounts_names_response_data_item import AccountsNamesResponseDataItem


class AccountsNamesResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[AccountsNamesResponseDataItem]] = pydantic.Field(default=None)
    """
    Produces <a href="/data-model/other/#message">Message</a> or <a href="/data-model/accounts/#name">Name</a> data. Corresponds to the <a href="/chifra/accounts/#chifra-names">chifra names</a> command line.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
