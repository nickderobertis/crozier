

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ReportEnvelopeMeter(UniversalBaseModel):
    status: typing.Optional[str] = None
    interface: typing.Optional[str] = None
    protocol: typing.Optional[str] = None
    logical_name: typing.Optional[str] = None
    vendor: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
