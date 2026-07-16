

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Attribute(UniversalBaseModel):
    attribute: typing.Optional[str] = None
    description: typing.Optional[str] = None
    expression: typing.Optional[str] = None
    id: typing.Optional[int] = None
    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    String|Number|Boolean
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
