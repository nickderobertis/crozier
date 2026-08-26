

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .app_config import AppConfig
from .cell_config import CellConfig
from .cell_id import CellId
from .consumer_capabilities import ConsumerCapabilities
from .kernel_capabilities_notification import KernelCapabilitiesNotification
from .kernel_ready_notification_op import KernelReadyNotificationOp
from .layout_config import LayoutConfig


class KernelReadyNotification(UniversalBaseModel):
    """
    Kernel ready for execution. First notification sent at startup.

        Attributes:
            cell_ids: Cell IDs in order.
            codes: Source code for each cell.
            names: Cell names/titles.
            layout: Notebook layout config.
            configs: Per-cell configuration.
            resumed: Whether resumed from previous session.
            ui_values: Previous UI element values if resumed.
            last_executed_code: Last executed code per cell if resumed.
            last_execution_time: Last execution time per cell if resumed.
            app_config: Application configuration.
            kiosk: Whether running in kiosk mode.
            capabilities: Available kernel capabilities.
            auto_instantiated: Whether cells already executed (run mode).
    """

    app_config: AppConfig
    auto_instantiated: typing.Optional[bool] = None
    capabilities: KernelCapabilitiesNotification
    cell_ids: typing.List[CellId]
    codes: typing.List[str]
    configs: typing.List[CellConfig]
    consumer_capabilities: ConsumerCapabilities
    kiosk: bool
    last_executed_code: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    last_execution_time: typing.Optional[typing.Dict[str, typing.Optional[float]]] = None
    layout: typing.Optional[LayoutConfig] = None
    names: typing.List[str]
    op: KernelReadyNotificationOp
    resumed: bool
    ui_values: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
