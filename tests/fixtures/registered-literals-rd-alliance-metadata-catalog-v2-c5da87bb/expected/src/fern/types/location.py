

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Location(UniversalBaseModel):
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the Web resource. Normalized specifications hosted by the MSC should be specified using a relative URL.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    A keyword describing the type of resource. Valid keywords may be obtained from the `locations` endpoint.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
