

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .monitor_callback_subscribe import MonitorCallbackSubscribe
from .monitor_parameter_extended_event_param_item import MonitorParameterExtendedEventParamItem
from .monitor_parameter_trigger_param import MonitorParameterTriggerParam


class MonitorParameter(UniversalBaseModel):
    """
    MonitorParameter
    """

    label: str = pydantic.Field()
    """
    Monitor label (usually its name).
    """

    subscribe_param: typing_extensions.Annotated[
        MonitorCallbackSubscribe, FieldMetadata(alias="subscribeParam"), pydantic.Field(alias="subscribeParam")
    ]
    extended_event_param: typing_extensions.Annotated[
        typing.Optional[typing.List[MonitorParameterExtendedEventParamItem]],
        FieldMetadata(alias="extendedEventParam"),
        pydantic.Field(
            alias="extendedEventParam",
            description="Allow to set extra vehicle data (defined in data model) to add to the monitor event\nwhen publishing. The possible values are :\n\n\n|value|description|Related model |\n|----------|:-------------|------:|\n|vehicle.doorsState|Latest known door state (timestamped) before the eventDate|DoorState|\n|vehicle.status|Latest known vehicle status (timestamped) before the eventDate|Status|\n|vehicle.maintenance|Latest known maintenance(timestamped) before the eventDate|Maintenance|\n|vehicle.position|Last vehicle position (timestamped) before the eventDate|Position|\n|vehicle.telemetry${.TelemetryEnum} |Latest known telemetry (timestamped) before the eventDate filtered with type|Telemetry\n|vehicle.alerts|List of active alerts at the eventDate|Alert|\n|vehicle.collisions|Latest known collisions before the eventDate|Collision|\n|vehicle.trip|Trip related to the event that triggers the notification|Trip|\n|vehicle.stolen|Vehicle Stolen context at the eventDate (only returns when vehicle is reported stolen) |Stolen|\n\n\n* For telemetry extension:  \n  * The suffix ```${.TelemetryEnum}``` can be selected to refine with telemetry type (from the TelemetryEnum list). This value (with suffix) can be selected **_several times_** to included suitable telemetry messages with the extention.\n  * Using ```vehicle.telemetry``` without suffix means to include all available telemetries. \n* The set of data will then correspond to the union of extensions used in the request.",
        ),
    ] = None
    """
    Allow to set extra vehicle data (defined in data model) to add to the monitor event
    when publishing. The possible values are :
    
    
    |value|description|Related model |
    |----------|:-------------|------:|
    |vehicle.doorsState|Latest known door state (timestamped) before the eventDate|DoorState|
    |vehicle.status|Latest known vehicle status (timestamped) before the eventDate|Status|
    |vehicle.maintenance|Latest known maintenance(timestamped) before the eventDate|Maintenance|
    |vehicle.position|Last vehicle position (timestamped) before the eventDate|Position|
    |vehicle.telemetry${.TelemetryEnum} |Latest known telemetry (timestamped) before the eventDate filtered with type|Telemetry
    |vehicle.alerts|List of active alerts at the eventDate|Alert|
    |vehicle.collisions|Latest known collisions before the eventDate|Collision|
    |vehicle.trip|Trip related to the event that triggers the notification|Trip|
    |vehicle.stolen|Vehicle Stolen context at the eventDate (only returns when vehicle is reported stolen) |Stolen|
    
    
    * For telemetry extension:  
      * The suffix ```${.TelemetryEnum}``` can be selected to refine with telemetry type (from the TelemetryEnum list). This value (with suffix) can be selected **_several times_** to included suitable telemetry messages with the extention.
      * Using ```vehicle.telemetry``` without suffix means to include all available telemetries. 
    * The set of data will then correspond to the union of extensions used in the request.
    """

    trigger_param: typing_extensions.Annotated[
        MonitorParameterTriggerParam,
        FieldMetadata(alias="triggerParam"),
        pydantic.Field(
            alias="triggerParam",
            description="Monitor trigger-param that allows to compound triggers by applying a boolean expression to evaluate them.",
        ),
    ]
    """
    Monitor trigger-param that allows to compound triggers by applying a boolean expression to evaluate them.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
