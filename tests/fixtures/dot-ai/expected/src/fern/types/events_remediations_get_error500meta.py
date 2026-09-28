

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EventsRemediationsGetError500Meta(UniversalBaseModel):
    timestamp: str = pydantic.Field()
    """
    ISO 8601 timestamp of the response
    """

    request_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="requestId"),
        pydantic.Field(alias="requestId", description="Unique request identifier for tracing"),
    ] = None
    """
    Unique request identifier for tracing
    """

    version: str = pydantic.Field()
    """
    API version
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
