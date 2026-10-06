

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class QName(UniversalBaseModel):
    namespace_uri: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="namespaceURI"), pydantic.Field(alias="namespaceURI")
    ] = None
    local_part: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="localPart"), pydantic.Field(alias="localPart")
    ] = None
    prefix: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
