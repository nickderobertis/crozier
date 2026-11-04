

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpgradeFromUriRequest(UniversalBaseModel):
    """
    Payload for upgrading a theme from a remote URI.
    """

    uri: str = pydantic.Field()
    """
    remote URI of the theme ZIP file
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
