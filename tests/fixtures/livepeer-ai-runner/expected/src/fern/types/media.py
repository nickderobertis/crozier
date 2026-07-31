

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Media(UniversalBaseModel):
    """
    A media object containing information about the generated media.
    """

    url: str = pydantic.Field()
    """
    The URL where the media can be accessed.
    """

    seed: int = pydantic.Field()
    """
    The seed used to generate the media.
    """

    nsfw: bool = pydantic.Field()
    """
    Whether the media was flagged as NSFW.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
