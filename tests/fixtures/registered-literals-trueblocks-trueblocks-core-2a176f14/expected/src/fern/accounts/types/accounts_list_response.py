

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .accounts_list_response_data_item import AccountsListResponseDataItem


class AccountsListResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[AccountsListResponseDataItem]] = pydantic.Field(default=None)
    """
    Produces <a href="/data-model/accounts/#appearance">Appearance</a>, <a href="/data-model/accounts/#bounds">Bounds</a> or <a href="/data-model/accounts/#monitor">Monitor</a> data. Corresponds to the <a href="/chifra/accounts/#chifra-list">chifra list</a> command line.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
