

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LinkedTrackingCategory(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier for the tracking category.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the tracking category.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
