

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .alert_base_severity import AlertBaseSeverity


class VentClosedAlert(UniversalBaseModel):
    """
    A vent closed fully.
    """

    closed_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="closedBy"), pydantic.Field(alias="closedBy")
    ] = None
    outcome_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="outcome.code"), pydantic.Field(alias="outcome.code")
    ] = None
    gauge_reading: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="gaugeReading"), pydantic.Field(alias="gaugeReading")
    ] = None
    motor: typing.Optional[str] = None
    vent_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ventId"),
        pydantic.Field(alias="ventId", description="The vent that moved."),
    ] = None
    """
    The vent that moved.
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
