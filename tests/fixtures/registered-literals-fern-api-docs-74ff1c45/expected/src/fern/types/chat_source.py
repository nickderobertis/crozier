

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ChatSource(UniversalBaseModel):
    url: str = pydantic.Field()
    """
    URL of the cited documentation page
    """

    title: str = pydantic.Field()
    """
    Title of the cited documentation page
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
