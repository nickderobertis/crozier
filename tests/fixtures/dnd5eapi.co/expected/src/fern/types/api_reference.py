

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ApiReference(UniversalBaseModel):
    """
    `APIReference`
    """

    index: typing.Optional[str] = pydantic.Field(default=None)
    """
    Resource index for shorthand searching.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the referenced resource.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the referenced resource.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
