

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PluginAuthor(UniversalBaseModel):
    """
    Plugin author metadata.
    """

    name: str = pydantic.Field()
    """
    Author display name.
    """

    website: typing.Optional[str] = pydantic.Field(default=None)
    """
    Author website URL.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
