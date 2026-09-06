

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_type_enum import FunctionTypeEnum
from .topic_automation_config_facet_functions_item_type import TopicAutomationConfigFacetFunctionsItemType


class TopicAutomationConfigFacetFunctionsItem(UniversalBaseModel):
    type: typing.Optional[TopicAutomationConfigFacetFunctionsItemType] = None
    id: typing.Optional[str] = None
    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version of the function
    """

    name: typing.Optional[str] = None
    function_type: typing.Optional[FunctionTypeEnum] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
