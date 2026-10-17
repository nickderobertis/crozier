

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PgsodiumConfigResponseOutput(UniversalBaseModel):
    root_key: str = pydantic.Field()
    """
    The pgsodium root key: 32 bytes, hex-encoded (64 characters).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
