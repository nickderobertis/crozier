

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .state_definition_dto import StateDefinitionDto
from .workflow_configuration_dto_criterion import WorkflowConfigurationDtoCriterion


class WorkflowConfigurationDto(UniversalBaseModel):
    version: str = pydantic.Field()
    """
    Version of the workflow configuration schema
    """

    name: str = pydantic.Field()
    """
    Name of the workflow
    """

    initial_state: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="initialState"),
        pydantic.Field(alias="initialState", description="Initial state for entities in this workflow"),
    ]
    """
    Initial state for entities in this workflow
    """

    states: typing.Dict[str, StateDefinitionDto] = pydantic.Field()
    """
    Map of state codes to state definitions
    """

    desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the workflow
    """

    active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Flag indicating if the workflow is active
    """

    criterion: typing.Optional[WorkflowConfigurationDtoCriterion] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(WorkflowConfigurationDto)
