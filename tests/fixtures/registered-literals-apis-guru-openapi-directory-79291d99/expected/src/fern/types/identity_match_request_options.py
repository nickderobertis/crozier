

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class IdentityMatchRequestOptions(UniversalBaseModel):
    """
    An optional object to filter /identity/match results
    """

    account_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    An array of `account_ids` to perform fuzzy match
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
