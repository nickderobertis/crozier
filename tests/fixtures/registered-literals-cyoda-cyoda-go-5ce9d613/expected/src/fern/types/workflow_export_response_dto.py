

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .workflow_configuration_dto import WorkflowConfigurationDto


class WorkflowExportResponseDto(UniversalBaseModel):
    entity_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="entityName"),
        pydantic.Field(alias="entityName", description="The name of the entity model"),
    ]
    """
    The name of the entity model
    """

    model_version: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="modelVersion"),
        pydantic.Field(alias="modelVersion", description="The version number of the entity model"),
    ]
    """
    The version number of the entity model
    """

    workflows: typing.List[WorkflowConfigurationDto] = pydantic.Field()
    """
    Collection of workflow configurations for the entity model
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(WorkflowExportResponseDto)
