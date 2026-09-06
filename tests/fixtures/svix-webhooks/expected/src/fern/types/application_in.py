

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ApplicationIn(UniversalBaseModel):
    metadata: typing.Optional[typing.Dict[str, str]] = None
    name: str
    throttle_rate: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="throttleRate"),
        pydantic.Field(
            alias="throttleRate",
            description="Maximum messages per second to send to this application's endpoints.\n\nOutgoing messages will be throttled to this rate.",
        ),
    ] = None
    """
    Maximum messages per second to send to this application's endpoints.
    
    Outgoing messages will be throttled to this rate.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional unique identifier for the application
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
