

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RestApiResponseMeta(UniversalBaseModel):
    timestamp: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Response timestamp
    """

    request_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="requestId"),
        pydantic.Field(alias="requestId", description="Unique request identifier"),
    ] = None
    """
    Unique request identifier
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
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
