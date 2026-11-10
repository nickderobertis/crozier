

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .live_activity_options_alert import LiveActivityOptionsAlert
from .live_activity_options_dismissal_date import LiveActivityOptionsDismissalDate
from .live_activity_options_expiration import LiveActivityOptionsExpiration
from .live_activity_options_priority import LiveActivityOptionsPriority
from .live_activity_options_stale_date import LiveActivityOptionsStaleDate
from .live_activity_options_timestamp import LiveActivityOptionsTimestamp


class LiveActivityOptions(UniversalBaseModel):
    alert: typing.Optional[LiveActivityOptionsAlert] = None
    attributes_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="attributesType"), pydantic.Field(alias="attributesType")
    ] = None
    attributes: typing.Optional[typing.Dict[str, typing.Any]] = None
    timestamp: typing.Optional[LiveActivityOptionsTimestamp] = None
    stale_date: typing_extensions.Annotated[
        typing.Optional[LiveActivityOptionsStaleDate],
        FieldMetadata(alias="staleDate"),
        pydantic.Field(alias="staleDate"),
    ] = None
    dismissal_date: typing_extensions.Annotated[
        typing.Optional[LiveActivityOptionsDismissalDate],
        FieldMetadata(alias="dismissalDate"),
        pydantic.Field(alias="dismissalDate"),
    ] = None
    expiration: typing.Optional[LiveActivityOptionsExpiration] = None
    priority: typing.Optional[LiveActivityOptionsPriority] = None
    ttl: typing.Optional[int] = None
    collapse_id: typing.Optional[str] = None
    relevance_score: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="relevanceScore"), pydantic.Field(alias="relevanceScore")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
