

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateProjectAutomationConfigBtqlExportExportDefinition_LogTraces(UniversalBaseModel):
    """
    The definition of what to export
    """

    type: typing.Literal["log_traces"] = "log_traces"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CreateProjectAutomationConfigBtqlExportExportDefinition_LogSpans(UniversalBaseModel):
    """
    The definition of what to export
    """

    type: typing.Literal["log_spans"] = "log_spans"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CreateProjectAutomationConfigBtqlExportExportDefinition_BtqlQuery(UniversalBaseModel):
    """
    The definition of what to export
    """

    type: typing.Literal["btql_query"] = "btql_query"
    btql_query: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


CreateProjectAutomationConfigBtqlExportExportDefinition = typing_extensions.Annotated[
    typing.Union[
        CreateProjectAutomationConfigBtqlExportExportDefinition_LogTraces,
        CreateProjectAutomationConfigBtqlExportExportDefinition_LogSpans,
        CreateProjectAutomationConfigBtqlExportExportDefinition_BtqlQuery,
    ],
    pydantic.Field(discriminator="type"),
]
