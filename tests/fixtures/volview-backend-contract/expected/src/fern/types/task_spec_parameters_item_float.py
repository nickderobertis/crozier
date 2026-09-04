

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TaskSpecParametersItemFloat(UniversalBaseModel):
    id: str
    title: typing.Optional[str] = None
    help: typing.Optional[str] = None
    section: typing.Optional[str] = None
    order: typing.Optional[float] = None
    widget: typing.Optional[str] = None
    required: typing.Optional[bool] = None
    min: typing.Optional[float] = None
    max: typing.Optional[float] = None
    step: typing.Optional[float] = None
    default: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
