

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .amf_event import AmfEvent
from .amf_event_mode import AmfEventMode


class AmfEventSubscription(UniversalBaseModel):
    event_list: typing_extensions.Annotated[
        typing.Optional[typing.List[AmfEvent]], FieldMetadata(alias="eventList"), pydantic.Field(alias="eventList")
    ] = None
    event_notify_uri: typing_extensions.Annotated[
        str, FieldMetadata(alias="eventNotifyUri"), pydantic.Field(alias="eventNotifyUri")
    ]
    notify_correlation_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="notifyCorrelationId"), pydantic.Field(alias="notifyCorrelationId")
    ]
    nf_id: typing_extensions.Annotated[str, FieldMetadata(alias="nfId"), pydantic.Field(alias="nfId")]
    subs_change_notify_uri: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="subsChangeNotifyUri"), pydantic.Field(alias="subsChangeNotifyUri")
    ] = None
    subs_change_notify_correlation_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="subsChangeNotifyCorrelationId"),
        pydantic.Field(alias="subsChangeNotifyCorrelationId"),
    ] = None
    supi: typing.Optional[str] = None
    group_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="groupId"), pydantic.Field(alias="groupId")
    ] = None
    gpsi: typing.Optional[str] = None
    pei: typing.Optional[str] = None
    any_ue: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="anyUE"), pydantic.Field(alias="anyUE")
    ] = None
    options: typing.Optional[AmfEventMode] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
