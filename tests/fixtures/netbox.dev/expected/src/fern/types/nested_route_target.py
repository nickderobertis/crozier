

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NestedRouteTarget(UniversalBaseModel):
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    name: str = pydantic.Field()
    """
    Route target value (formatted in accordance with RFC 4360)
    """

    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
