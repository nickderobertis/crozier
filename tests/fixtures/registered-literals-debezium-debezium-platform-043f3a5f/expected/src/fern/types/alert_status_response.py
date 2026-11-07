

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .active_alert_response import ActiveAlertResponse


class AlertStatusResponse(UniversalBaseModel):
    total_firing: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalFiring"), pydantic.Field(alias="totalFiring")
    ] = None
    total_pending: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalPending"), pydantic.Field(alias="totalPending")
    ] = None
    firing_by_severity: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, int]],
        FieldMetadata(alias="firingBySeverity"),
        pydantic.Field(alias="firingBySeverity"),
    ] = None
    active_alerts: typing_extensions.Annotated[
        typing.Optional[typing.List[ActiveAlertResponse]],
        FieldMetadata(alias="activeAlerts"),
        pydantic.Field(alias="activeAlerts"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
