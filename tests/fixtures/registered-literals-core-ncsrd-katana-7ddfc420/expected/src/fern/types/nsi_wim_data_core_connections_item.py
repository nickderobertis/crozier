

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nsi_wim_data_core_connections_item_core import NsiWimDataCoreConnectionsItemCore
from .nsi_wim_data_core_connections_item_radio import NsiWimDataCoreConnectionsItemRadio


class NsiWimDataCoreConnectionsItem(UniversalBaseModel):
    """
    The endpoints of the connections
    """

    core: typing.Optional[NsiWimDataCoreConnectionsItemCore] = pydantic.Field(default=None)
    """
    The core part of the radio connection
    """

    radio: typing.Optional[NsiWimDataCoreConnectionsItemRadio] = pydantic.Field(default=None)
    """
    The core part of the radio connection
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
