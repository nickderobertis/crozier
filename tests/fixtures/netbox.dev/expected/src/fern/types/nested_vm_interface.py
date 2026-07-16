

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_virtual_machine import NestedVirtualMachine


class NestedVmInterface(UniversalBaseModel):
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    name: str
    url: typing.Optional[str] = None
    virtual_machine: typing.Optional[NestedVirtualMachine] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
