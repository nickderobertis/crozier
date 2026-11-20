

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetHeadersRequestResponse(UniversalBaseModel):
    raw_headers: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="rawHeaders"),
        pydantic.Field(alias="rawHeaders"),
    ] = None
    typed_headers: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="typedHeaders"), pydantic.Field(alias="typedHeaders")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
