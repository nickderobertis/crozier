

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PatchProjectAutomationConfigBatchSizeExportDefinition_LogTraces(UniversalBaseModel):
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


class PatchProjectAutomationConfigBatchSizeExportDefinition_LogSpans(UniversalBaseModel):
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


class PatchProjectAutomationConfigBatchSizeExportDefinition_BtqlQuery(UniversalBaseModel):
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


PatchProjectAutomationConfigBatchSizeExportDefinition = typing_extensions.Annotated[
    typing.Union[
        PatchProjectAutomationConfigBatchSizeExportDefinition_LogTraces,
        PatchProjectAutomationConfigBatchSizeExportDefinition_LogSpans,
        PatchProjectAutomationConfigBatchSizeExportDefinition_BtqlQuery,
    ],
    pydantic.Field(discriminator="type"),
]
