

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .alert_status_change_request_model_dismissal_time_range import AlertStatusChangeRequestModelDismissalTimeRange
from .alert_status_change_request_model_filter import AlertStatusChangeRequestModelFilter


class AlertStatusChangeRequestModel(UniversalBaseModel):
    """
    Model for Alert Status Change Request
    """

    alerts: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Alert IDs
    """

    dismissal_note: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="dismissalNote"),
        pydantic.Field(
            alias="dismissalNote", description="Reason for dismissal (this only applies to the dismiss alerts endpoint)"
        ),
    ] = None
    """
    Reason for dismissal (this only applies to the dismiss alerts endpoint)
    """

    dismissal_time_range: typing_extensions.Annotated[
        typing.Optional[AlertStatusChangeRequestModelDismissalTimeRange],
        FieldMetadata(alias="dismissalTimeRange"),
        pydantic.Field(alias="dismissalTimeRange", description="Dismissal Time Range"),
    ] = None
    """
    Dismissal Time Range
    """

    filter: AlertStatusChangeRequestModelFilter = pydantic.Field()
    """
    Filter
    """

    policies: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Policy IDs
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
