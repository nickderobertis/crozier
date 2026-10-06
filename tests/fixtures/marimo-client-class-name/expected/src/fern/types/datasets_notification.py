

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .data_table import DataTable
from .datasets_notification_clear_channel import DatasetsNotificationClearChannel
from .datasets_notification_op import DatasetsNotificationOp


class DatasetsNotification(UniversalBaseModel):
    """
    Available datasets for data explorer.

        Attributes:
            tables: Available data tables/datasets.
            clear_channel: If set, clears tables from this channel first.
    """

    clear_channel: typing.Optional[DatasetsNotificationClearChannel] = None
    op: DatasetsNotificationOp
    tables: typing.List[DataTable]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
