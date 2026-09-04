

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .task_spec_parameters_item_enum_default import TaskSpecParametersItemEnumDefault
from .task_spec_parameters_item_enum_options_item import TaskSpecParametersItemEnumOptionsItem


class TaskSpecParametersItemEnum(UniversalBaseModel):
    id: str
    title: typing.Optional[str] = None
    help: typing.Optional[str] = None
    section: typing.Optional[str] = None
    order: typing.Optional[float] = None
    widget: typing.Optional[str] = None
    required: typing.Optional[bool] = None
    options: typing.List[TaskSpecParametersItemEnumOptionsItem]
    default: typing.Optional[TaskSpecParametersItemEnumDefault] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
