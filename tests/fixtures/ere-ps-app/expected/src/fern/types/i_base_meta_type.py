

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .date import Date
from .i_base_coding import IBaseCoding
from .i_primitive_type_string import IPrimitiveTypeString


class IBaseMetaType(UniversalBaseModel):
    empty: typing.Optional[bool] = None
    format_comments_pre: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="formatCommentsPre"),
        pydantic.Field(alias="formatCommentsPre"),
    ] = None
    format_comments_post: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="formatCommentsPost"),
        pydantic.Field(alias="formatCommentsPost"),
    ] = None
    last_updated: typing_extensions.Annotated[
        typing.Optional[Date], FieldMetadata(alias="lastUpdated"), pydantic.Field(alias="lastUpdated")
    ] = None
    profile: typing.Optional[typing.List[IPrimitiveTypeString]] = None
    security: typing.Optional[typing.List[IBaseCoding]] = None
    tag: typing.Optional[typing.List[IBaseCoding]] = None
    version_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="versionId"), pydantic.Field(alias="versionId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
