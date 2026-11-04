

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .named_ref import NamedRef
from .pipeline_status import PipelineStatus


class PipelineResponse(UniversalBaseModel):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    description: typing.Optional[str] = None
    source: typing.Optional[NamedRef] = None
    destination: typing.Optional[NamedRef] = None
    transforms: typing.Optional[typing.List[NamedRef]] = None
    log_level: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="logLevel"), pydantic.Field(alias="logLevel")
    ] = None
    log_levels: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="logLevels"), pydantic.Field(alias="logLevels")
    ] = None
    status: typing.Optional[PipelineStatus] = None
    error_message: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="errorMessage"), pydantic.Field(alias="errorMessage")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
