

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .field_cardinality import FieldCardinality
from .field_kind import FieldKind
from .option import Option


class Field(UniversalBaseModel):
    """
    A single field of a message type.
    """

    cardinality: typing.Optional[FieldCardinality] = pydantic.Field(default=None)
    """
    The field cardinality.
    """

    default_value: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="defaultValue"),
        pydantic.Field(
            alias="defaultValue", description="The string value of the default value of this field. Proto2 syntax only."
        ),
    ] = None
    """
    The string value of the default value of this field. Proto2 syntax only.
    """

    json_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="jsonName"),
        pydantic.Field(alias="jsonName", description="The field JSON name."),
    ] = None
    """
    The field JSON name.
    """

    kind: typing.Optional[FieldKind] = pydantic.Field(default=None)
    """
    The field type.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The field name.
    """

    number: typing.Optional[int] = pydantic.Field(default=None)
    """
    The field number.
    """

    oneof_index: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="oneofIndex"),
        pydantic.Field(
            alias="oneofIndex",
            description="The index of the field type in Type.oneofs, for message or enumeration types. The first type has index 1; zero means the type is not in the list.",
        ),
    ] = None
    """
    The index of the field type in Type.oneofs, for message or enumeration types. The first type has index 1; zero means the type is not in the list.
    """

    options: typing.Optional[typing.List[Option]] = pydantic.Field(default=None)
    """
    The protocol buffer options.
    """

    packed: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to use alternative packed wire representation.
    """

    type_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="typeUrl"),
        pydantic.Field(
            alias="typeUrl",
            description='The field type URL, without the scheme, for message or enumeration types. Example: "type.googleapis.com/google.protobuf.Timestamp".',
        ),
    ] = None
    """
    The field type URL, without the scheme, for message or enumeration types. Example: "type.googleapis.com/google.protobuf.Timestamp".
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
