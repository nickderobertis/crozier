

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SourceContext(UniversalBaseModel):
    """
    SourceContext represents information about the source of a protobuf element, like the file in which it is defined.
    """

    file_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fileName"),
        pydantic.Field(
            alias="fileName",
            description='The path-qualified name of the .proto file that contained the associated protobuf element. For example: "google/protobuf/source_context.proto".',
        ),
    ] = None
    """
    The path-qualified name of the .proto file that contained the associated protobuf element. For example: "google/protobuf/source_context.proto".
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
