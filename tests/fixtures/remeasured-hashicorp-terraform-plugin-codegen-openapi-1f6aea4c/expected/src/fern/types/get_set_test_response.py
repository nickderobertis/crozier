

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .setnested_schema import SetnestedSchema


class GetSetTestResponse(UniversalBaseModel):
    setnested_prop: typing.Optional[SetnestedSchema] = None
    set_prop: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    This is a set of strings
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
