

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .alert_data_item_alert_source import AlertDataItemAlertSource
from .alert_data_item_source_type import AlertDataItemSourceType


class AlertDataItem(UniversalBaseModel):
    alert_source: typing.Optional[AlertDataItemAlertSource] = pydantic.Field(default=None)
    """
    The source of the alert
    """

    source: typing.Optional[str] = pydantic.Field(default=None)
    """
    The UID of the source of the alert
    """

    source_type: typing.Optional[AlertDataItemSourceType] = pydantic.Field(default=None)
    """
    The type of source.
    """

    source_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The UID of the source of the alert
    """

    value: typing.Optional[float] = pydantic.Field(default=None)
    """
    The value that triggered the alert
    """

    when: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time the alert was created
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
