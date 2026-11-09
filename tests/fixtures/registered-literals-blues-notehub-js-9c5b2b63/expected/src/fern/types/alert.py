

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .alert_alert_source import AlertAlertSource
from .alert_data_item import AlertDataItem
from .alert_monitor_type import AlertMonitorType
from .alert_notifications_item import AlertNotificationsItem


class Alert(UniversalBaseModel):
    alert_source: typing.Optional[AlertAlertSource] = pydantic.Field(default=None)
    """
    The source of the alert
    """

    created_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    The time the alert was created
    """

    data: typing.Optional[typing.List[AlertDataItem]] = None
    device_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device UID
    """

    field_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The field name that triggered the alert
    """

    monitor_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Monitor Name
    """

    monitor_type: typing.Optional[AlertMonitorType] = pydantic.Field(default=None)
    """
    The type of monitor that triggered the alert
    """

    monitor_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    Monitor UID
    """

    notifications: typing.Optional[typing.List[AlertNotificationsItem]] = None
    resolved: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, the alert has been resolved
    """

    source: typing.Optional[str] = pydantic.Field(default=None)
    """
    The UID of the source of the alert
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    Alert UID
    """

    value: typing.Optional[float] = pydantic.Field(default=None)
    """
    The value that triggered the alert
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The version of the alert
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
