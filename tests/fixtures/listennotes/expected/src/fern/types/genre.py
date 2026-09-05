

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Genre(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Genre id
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Genre name.
    """

    parent_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Parent genre id.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
