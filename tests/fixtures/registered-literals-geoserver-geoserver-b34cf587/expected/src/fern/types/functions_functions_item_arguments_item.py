

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .functions_functions_item_arguments_item_type_item import FunctionsFunctionsItemArgumentsItemTypeItem


class FunctionsFunctionsItemArgumentsItem(UniversalBaseModel):
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    type: typing.List[FunctionsFunctionsItemArgumentsItemTypeItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
