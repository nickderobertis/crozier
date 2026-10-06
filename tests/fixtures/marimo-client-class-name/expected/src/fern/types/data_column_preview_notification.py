

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .column_stats import ColumnStats
from .data_column_preview_notification_op import DataColumnPreviewNotificationOp


class DataColumnPreviewNotification(UniversalBaseModel):
    """
    Data column preview with stats and visualization.

        Inherits all ColumnPreview attributes.

        Attributes:
            table_name: Table containing the column.
            column_name: Column being previewed.
    """

    chart_code: typing.Optional[str] = None
    chart_spec: typing.Optional[str] = None
    column_name: str
    error: typing.Optional[str] = None
    missing_packages: typing.Optional[typing.List[str]] = None
    op: DataColumnPreviewNotificationOp
    stats: typing.Optional[ColumnStats] = None
    table_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
