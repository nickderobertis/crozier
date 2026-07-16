

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .module_nested_module_bay import ModuleNestedModuleBay


class ComponentNestedModule(UniversalBaseModel):
    device: int
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    module_bay: typing.Optional[ModuleNestedModuleBay] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
