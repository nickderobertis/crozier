

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .alert_base_severity import AlertBaseSeverity
from .vent_alert_motor import VentAlertMotor


class VentAlert(UniversalBaseModel):
    """
    A vent changed position.
    """

    vent_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ventId"),
        pydantic.Field(alias="ventId", description="The vent that moved."),
    ] = None
    """
    The vent that moved.
    """

    motor: typing.Optional[VentAlertMotor] = pydantic.Field(default=None)
    """
    The motor that drove the vent.
    """

    outcome_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="outcome.code"),
        pydantic.Field(alias="outcome.code", description="A code for the alert's outcome."),
    ] = None
    """
    A code for the alert's outcome.
    """

    bay: typing.Optional[str] = pydantic.Field(default=None)
    """
    The bay the alert concerns.
    """

    severity: typing.Optional[AlertBaseSeverity] = pydantic.Field(default=None)
    """
    How urgent the alert is.
    """

    sent_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sentAt"),
        pydantic.Field(alias="sentAt", description="When the alert was sent."),
    ] = None
    """
    When the alert was sent.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
