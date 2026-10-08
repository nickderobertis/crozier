

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .data_source_connection import DataSourceConnection
from .data_source_connections_notification_op import DataSourceConnectionsNotificationOp


class DataSourceConnectionsNotification(UniversalBaseModel):
    """
    Available data source connections for SQL cells.

        Attributes:
            connections: Available data source connections.
    """

    connections: typing.List[DataSourceConnection]
    op: DataSourceConnectionsNotificationOp

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(DataSourceConnectionsNotification)
