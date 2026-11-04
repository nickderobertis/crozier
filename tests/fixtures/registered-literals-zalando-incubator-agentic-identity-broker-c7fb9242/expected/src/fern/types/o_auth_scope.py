

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OAuthScope(UniversalBaseModel):
    scope_value: str = pydantic.Field()
    """
    OAuth2 scope identifier
    """

    description: str = pydantic.Field()
    """
    Human-readable scope description
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
