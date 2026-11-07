

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Texture(UniversalBaseModel):
    """
    Player skin/cape texture descriptor.
    """

    url: str
    digest: str = pydantic.Field()
    """
    Base64-encoded raw digest bytes of the texture file.
    """

    metadata: typing.Optional[typing.Dict[str, str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
