

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NonfatalFaultTypeDto(UniversalBaseModel):
    """
    AAT and/or the Ably client library should handle this fault seamlessly. Trackable state should be online and publisher should be present within resolvedWithinMillis milliseconds. It's possible the fault will cause a brief Offline blip, but tests should expect to see Trackables Online again before resolvedWithinMillis expires regardless.
    """

    resolved_within_millis: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="resolvedWithinMillis"), pydantic.Field(alias="resolvedWithinMillis")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
