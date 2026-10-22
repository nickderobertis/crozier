

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RangeFacet(UniversalBaseModel):
    property: typing.Optional[str] = pydantic.Field(default=None)
    """
    Property which this searches in.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human readable name of the facet.
    """

    min: typing.Optional[int] = None
    max: typing.Optional[int] = None
    step: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
