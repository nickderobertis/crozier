

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Category(UniversalBaseModel):
    """
    Information about a category
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of a category
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of a category
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
