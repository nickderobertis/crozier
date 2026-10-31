

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FatalFaultTypeDto(UniversalBaseModel):
    """
    This is a fatal error and should permanently move Trackables to the Failed state. The publisher should not be present in the corresponding channel any more and no further location updates will be published. Tests should check that Trackables reach the Failed state within failedWithinMillis milliseconds.
    """

    failed_within_millis: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="failedWithinMillis"), pydantic.Field(alias="failedWithinMillis")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
