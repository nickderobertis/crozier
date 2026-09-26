

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .block_type import BlockType
from .question_field import QuestionField


class Question(UniversalBaseModel):
    id: typing.Optional[str] = None
    type: typing.Optional[BlockType] = None
    title: typing.Optional[str] = None
    is_title_modified_by_user: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isTitleModifiedByUser"),
        pydantic.Field(alias="isTitleModifiedByUser"),
    ] = None
    form_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="formId"), pydantic.Field(alias="formId")
    ] = None
    is_deleted: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDeleted"), pydantic.Field(alias="isDeleted")
    ] = None
    number_of_responses: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="numberOfResponses"), pydantic.Field(alias="numberOfResponses")
    ] = None
    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None
    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ] = None
    fields: typing.Optional[typing.List[QuestionField]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
