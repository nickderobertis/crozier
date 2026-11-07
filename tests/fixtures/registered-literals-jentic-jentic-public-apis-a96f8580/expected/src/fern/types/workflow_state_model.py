

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WorkflowStateModel_NotStarted(UniversalBaseModel):
    state: typing.Literal["not_started"] = "not_started"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class WorkflowStateModel_Completed(UniversalBaseModel):
    state: typing.Literal["completed"] = "completed"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class WorkflowStateModel_InProgress(UniversalBaseModel):
    state: typing.Literal["in_progress"] = "in_progress"
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class WorkflowStateModel_NotApplicable(UniversalBaseModel):
    state: typing.Literal["not_applicable"] = "not_applicable"
    message: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


WorkflowStateModel = typing_extensions.Annotated[
    typing.Union[
        WorkflowStateModel_NotStarted,
        WorkflowStateModel_Completed,
        WorkflowStateModel_InProgress,
        WorkflowStateModel_NotApplicable,
    ],
    pydantic.Field(discriminator="state"),
]
