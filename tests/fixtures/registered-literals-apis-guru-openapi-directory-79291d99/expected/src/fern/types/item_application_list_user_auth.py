

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ItemApplicationListUserAuth(UniversalBaseModel):
    """
    User authentication parameters, for clients making a request without an `access_token`. This is only allowed for select clients and will not be supported in the future. Most clients should call /item/import to obtain an access token before making a request.
    """

    fi_username_hash: typing.Optional[str] = pydantic.Field(default=None)
    """
    Account username hashed by FI.
    """

    user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Account username.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
