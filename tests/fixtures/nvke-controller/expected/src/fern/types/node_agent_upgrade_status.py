

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .node_agent_upgrade_status_phase import NodeAgentUpgradeStatusPhase


class NodeAgentUpgradeStatus(UniversalBaseModel):
    """
    The active agent upgrade and latest retry error.
    """

    node_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="nodeId"),
        pydantic.Field(alias="nodeId", description="ID of the selected control-plane node."),
    ]
    """
    ID of the selected control-plane node.
    """

    target_version: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="targetVersion"),
        pydantic.Field(alias="targetVersion", description="Exact version accepted for this upgrade."),
    ]
    """
    Exact version accepted for this upgrade.
    """

    method: str = pydantic.Field()
    """
    Installation method from the controller configuration.
    """

    phase: NodeAgentUpgradeStatusPhase = pydantic.Field()
    """
    Pending before installation starts. Running includes retries.
    """

    error_message: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="errorMessage"),
        pydantic.Field(alias="errorMessage", description="Latest failure message while retries continue."),
    ]
    """
    Latest failure message while retries continue.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
