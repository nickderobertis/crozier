

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .control_plane_config_change import ControlPlaneConfigChange


class ControlPlaneConfigHistory(UniversalBaseModel):
    """
    Ordered snapshots of control-plane configuration changes.
    """

    changes: typing.List[ControlPlaneConfigChange] = pydantic.Field()
    """
    Oldest first. A node's pinnedConfigurationID and the cluster's desired
    configurationId both refer to entries here.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
