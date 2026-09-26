

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account import Account
from .account_list_response_links import AccountListResponseLinks
from .account_list_response_meta import AccountListResponseMeta


class AccountListResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[Account]] = None
    meta: typing.Optional[AccountListResponseMeta] = None
    links: typing.Optional[AccountListResponseLinks] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
