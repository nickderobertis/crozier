

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .demo_field import DemoField


class DemoVersion(UniversalBaseModel):
    """
    One Lance version of a dataset — its number, time, and schema at that version.
    """

    fields: typing.Optional[typing.List[DemoField]] = None
    timestamp: typing.Optional[str] = None
    version: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
