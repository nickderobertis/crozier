

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ErrorErrorInnererror(UniversalBaseModel):
    code: typing.Optional[str] = None
    date: typing.Optional[dt.datetime] = None
    request_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="request-id"), pydantic.Field(alias="request-id")
    ] = None
    client_request_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="client-request-id"), pydantic.Field(alias="client-request-id")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
