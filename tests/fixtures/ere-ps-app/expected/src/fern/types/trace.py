

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .detail import Detail


class Trace(UniversalBaseModel):
    event_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="eventID"), pydantic.Field(alias="eventID")
    ] = None
    instance: typing.Optional[str] = None
    log_reference: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="logReference"), pydantic.Field(alias="logReference")
    ] = None
    comp_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="compType"), pydantic.Field(alias="compType")
    ] = None
    code: typing.Optional[int] = None
    severity: typing.Optional[str] = None
    error_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="errorType"), pydantic.Field(alias="errorType")
    ] = None
    error_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="errorText"), pydantic.Field(alias="errorText")
    ] = None
    detail: typing.Optional[Detail] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
