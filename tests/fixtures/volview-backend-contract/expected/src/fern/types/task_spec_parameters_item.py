

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .task_spec_parameters_item_enum_default import TaskSpecParametersItemEnumDefault
from .task_spec_parameters_item_enum_options_item import TaskSpecParametersItemEnumOptionsItem


class TaskSpecParametersItem_Int(UniversalBaseModel):
    kind: typing.Literal["int"] = "int"
    id: str
    title: typing.Optional[str] = None
    help: typing.Optional[str] = None
    section: typing.Optional[str] = None
    order: typing.Optional[float] = None
    widget: typing.Optional[str] = None
    required: typing.Optional[bool] = None
    min: typing.Optional[int] = None
    max: typing.Optional[int] = None
    step: typing.Optional[int] = None
    default: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TaskSpecParametersItem_Float(UniversalBaseModel):
    kind: typing.Literal["float"] = "float"
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


class TaskSpecParametersItem_String(UniversalBaseModel):
    kind: typing.Literal["string"] = "string"
    id: str
    title: typing.Optional[str] = None
    help: typing.Optional[str] = None
    section: typing.Optional[str] = None
    order: typing.Optional[float] = None
    widget: typing.Optional[str] = None
    required: typing.Optional[bool] = None
    default: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TaskSpecParametersItem_Bool(UniversalBaseModel):
    kind: typing.Literal["bool"] = "bool"
    id: str
    title: typing.Optional[str] = None
    help: typing.Optional[str] = None
    section: typing.Optional[str] = None
    order: typing.Optional[float] = None
    widget: typing.Optional[str] = None
    required: typing.Optional[bool] = None
    default: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TaskSpecParametersItem_Enum(UniversalBaseModel):
    kind: typing.Literal["enum"] = "enum"
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


class TaskSpecParametersItem_SourceRef(UniversalBaseModel):
    kind: typing.Literal["sourceRef"] = "sourceRef"
    id: str
    title: typing.Optional[str] = None
    help: typing.Optional[str] = None
    section: typing.Optional[str] = None
    order: typing.Optional[float] = None
    widget: typing.Optional[str] = None
    required: typing.Optional[bool] = None
    accepts: typing.List[str]
    multiple: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TaskSpecParametersItem_Bounds(UniversalBaseModel):
    kind: typing.Literal["bounds"] = "bounds"
    id: str
    title: typing.Optional[str] = None
    help: typing.Optional[str] = None
    section: typing.Optional[str] = None
    order: typing.Optional[float] = None
    widget: typing.Optional[str] = None
    required: typing.Optional[bool] = None
    default: typing.Optional[typing.List[typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


TaskSpecParametersItem = typing_extensions.Annotated[
    typing.Union[
        TaskSpecParametersItem_Int,
        TaskSpecParametersItem_Float,
        TaskSpecParametersItem_String,
        TaskSpecParametersItem_Bool,
        TaskSpecParametersItem_Enum,
        TaskSpecParametersItem_SourceRef,
        TaskSpecParametersItem_Bounds,
    ],
    pydantic.Field(discriminator="kind"),
]
