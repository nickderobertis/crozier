

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ItemImportRequestUserAuth(UniversalBaseModel):
    """
    Object of user ID and auth token pair, permitting Plaid to aggregate a user’s accounts
    """

    auth_token: str = pydantic.Field()
    """
    Authorization token Plaid will use to aggregate this user’s accounts
    """

    user_id: str = pydantic.Field()
    """
    Opaque user identifier
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
