

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NestedDeviceRole(UniversalBaseModel):
    device_count: typing.Optional[int] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    name: str
    slug: str
    url: typing.Optional[str] = None
    virtualmachine_count: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
