

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .callback_subscribe import CallbackSubscribe


class MonitorCallbackSubscribe(CallbackSubscribe):
    refresh_event: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="refreshEvent"),
        pydantic.Field(
            alias="refreshEvent",
            description="Define the period (in sec.) between two refresh events. The refresh-events are sent when the condition of the monitor is satisfied (Trigger -> toggled true). A kind of periodic reminder.",
        ),
    ] = None
    """
    Define the period (in sec.) between two refresh events. The refresh-events are sent when the condition of the monitor is satisfied (Trigger -> toggled true). A kind of periodic reminder.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
