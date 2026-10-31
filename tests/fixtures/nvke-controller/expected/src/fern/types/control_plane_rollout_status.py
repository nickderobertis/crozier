

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .control_plane_rollout_change import ControlPlaneRolloutChange


class ControlPlaneRolloutStatus(UniversalBaseModel):
    """
    Control-plane nodes only. Drift is computed on the release and
    the Kubernetes version. Resolve pinnedConfigurationID and desiredConfigurationID
    with GET /clusters/{clusterID}/control-plane/configHistory.
    """

    pending: bool = pydantic.Field()
    """
    The node differs from the desired configuration.
    """

    actionable: bool = pydantic.Field()
    """
    The node can be replaced now.
    """

    changes: typing.Optional[typing.List[ControlPlaneRolloutChange]] = pydantic.Field(default=None)
    """
    Each with field, from, to as plain strings. Drift is computed on the release and the Kubernetes version.
    """

    pinned_configuration_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pinnedConfigurationID"),
        pydantic.Field(alias="pinnedConfigurationID", description="Configuration the node was built from."),
    ] = None
    """
    Configuration the node was built from.
    """

    desired_configuration_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="desiredConfigurationID"),
        pydantic.Field(alias="desiredConfigurationID", description="Configuration the node should move to."),
    ] = None
    """
    Configuration the node should move to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
