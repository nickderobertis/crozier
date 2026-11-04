

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nsi_connections_item_core import NsiConnectionsItemCore


class NsiConnectionsItem(UniversalBaseModel):
    """
    A 5G service connections. Each connection contains a core and a radio endpoint. The endpoints are selected from the platform fanctions repository of the Slice Manager
    """

    core: typing.Optional[NsiConnectionsItemCore] = pydantic.Field(default=None)
    """
    The Core part of the 5G service connection
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
