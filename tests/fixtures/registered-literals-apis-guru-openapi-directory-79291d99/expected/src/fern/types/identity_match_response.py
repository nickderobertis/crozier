

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_identity_match_score import AccountIdentityMatchScore
from .item import Item
from .request_id import RequestId


class IdentityMatchResponse(UniversalBaseModel):
    """
    IdentityMatchResponse defines the response schema for `/identity/match`
    """

    accounts: typing.List[AccountIdentityMatchScore] = pydantic.Field()
    """
    The accounts for which Identity match has been requested
    """

    item: Item
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
