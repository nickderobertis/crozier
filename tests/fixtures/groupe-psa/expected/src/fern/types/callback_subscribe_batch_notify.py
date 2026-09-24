

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CallbackSubscribeBatchNotify(UniversalBaseModel):
    """

    Notification batch of events defined by a time window and batch size. If this field is not set, the callback will post only one event by call.

      * **At least, the ```size``` parameter should be provided.**
      * **If the time window is not set then the default value will be applied.**
    """

    size: int = pydantic.Field()
    """
    Batch size (positive value and not zero).
    """

    time_window: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="timeWindow"),
        pydantic.Field(alias="timeWindow", description="Notification batch window size (expressed in seconds)."),
    ] = None
    """
    Notification batch window size (expressed in seconds).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
