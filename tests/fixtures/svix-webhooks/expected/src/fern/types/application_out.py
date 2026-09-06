

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ApplicationOut(UniversalBaseModel):
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    id: str
    metadata: typing.Dict[str, str]
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

    uid: typing.Optional[str] = None
    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
