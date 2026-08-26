

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .data_source_discovery_result_notification_op import DataSourceDiscoveryResultNotificationOp
from .detected_data_source import DetectedDataSource


class DataSourceDiscoveryResultNotification(UniversalBaseModel):
    """
    High-confidence datasource connections discovered by the kernel.

        Attributes:
            request_id: Request ID this responds to.
            sources: Detected datasource connection configurations.
    """

    op: DataSourceDiscoveryResultNotificationOp
    request_id: str
    sources: typing.List[DetectedDataSource]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
