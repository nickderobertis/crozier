

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .control_plane_config import ControlPlaneConfig
from .control_plane_status import ControlPlaneStatus


class ClusterControlPlane(UniversalBaseModel):
    """
    Read-only view of a cluster's control plane: its persisted configuration
    plus an aggregate runtime status.
    """

    config: ControlPlaneConfig = pydantic.Field()
    """
    The persisted control-plane configuration.
    """

    status: ControlPlaneStatus = pydantic.Field()
    """
    Aggregate runtime status.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
