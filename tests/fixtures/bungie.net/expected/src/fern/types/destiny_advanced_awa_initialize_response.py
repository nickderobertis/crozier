

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyAdvancedAwaInitializeResponse(UniversalBaseModel):
    correlation_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="correlationId"),
        pydantic.Field(
            alias="correlationId",
            description="ID used to get the token. Present this ID to the user as it will identify this specific request on their device.",
        ),
    ] = None
    """
    ID used to get the token. Present this ID to the user as it will identify this specific request on their device.
    """

    sent_to_self: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="sentToSelf"),
        pydantic.Field(
            alias="sentToSelf",
            description="True if the PUSH message will only be sent to the device that made this request.",
        ),
    ] = None
    """
    True if the PUSH message will only be sent to the device that made this request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
