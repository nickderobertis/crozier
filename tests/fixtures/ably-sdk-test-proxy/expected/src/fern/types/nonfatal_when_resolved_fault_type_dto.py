

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NonfatalWhenResolvedFaultTypeDto(UniversalBaseModel):
    """
    This is a non-fatal error, but will persist until the POST /fault-simulations/{id}/resolve endpoint has been called. Trackable states should be offline during the fault within offlineWithinMillis milliseconds maximum. When the fault is resolved, Trackables should return online within onlineWithinMillis milliseconds maximum.
    """

    offline_within_millis: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="offlineWithinMillis"), pydantic.Field(alias="offlineWithinMillis")
    ] = None
    online_within_millis: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="onlineWithinMillis"), pydantic.Field(alias="onlineWithinMillis")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
