

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .book_name import BookName
from .protoform_conformance_v1book_state import ProtoformConformanceV1BookState


class ProtoformConformanceV1Book(UniversalBaseModel):
    name: typing.Optional[BookName] = None
    uid: typing.Optional[str] = None
    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ]
    create_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createTime"), pydantic.Field(alias="createTime")
    ] = None
    update_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="updateTime"), pydantic.Field(alias="updateTime")
    ] = None
    isbn: str = pydantic.Field()
    """
    ISBN-13; the protobuf CEL rule validates its check digit.
    """

    input_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="inputToken"), pydantic.Field(alias="inputToken")
    ] = None
    note: typing.Optional[str] = None
    etag: typing.Optional[str] = None
    state: typing.Optional[ProtoformConformanceV1BookState] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
