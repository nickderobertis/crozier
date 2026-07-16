

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class HsAlgoSettings(UniversalBaseModel):
    """
    Settings for an HMAC + SHA signing algorithm
    """

    secret: str = pydantic.Field()
    """
    The secret value for the HMAC function
    """

    size: int = pydantic.Field()
    """
    Size for SHA function. can be 256, 384 or 512
    """

    type: str = pydantic.Field()
    """
    String with value HSAlgoSettings
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
