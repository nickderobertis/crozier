

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Item20(UniversalBaseModel):
    id: str
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    cvx_code: typing_extensions.Annotated[str, FieldMetadata(alias="cvxCode"), pydantic.Field(alias="cvxCode")]
    name: str
    reasons: typing.List[str]
    start_date: typing_extensions.Annotated[str, FieldMetadata(alias="startDate"), pydantic.Field(alias="startDate")]
    end_date: typing_extensions.Annotated[str, FieldMetadata(alias="endDate"), pydantic.Field(alias="endDate")]
    comment: str
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    create_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestamp"), pydantic.Field(alias="createTimestamp")
    ]
    modified_by: typing_extensions.Annotated[str, FieldMetadata(alias="modifiedBy"), pydantic.Field(alias="modifiedBy")]
    modify_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifyTimestamp"), pydantic.Field(alias="modifyTimestamp")
    ]
    practice_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="practiceName"), pydantic.Field(alias="practiceName")
    ]
    excluded_by: typing_extensions.Annotated[str, FieldMetadata(alias="excludedBy"), pydantic.Field(alias="excludedBy")]
    is_deleted: typing_extensions.Annotated[str, FieldMetadata(alias="isDeleted"), pydantic.Field(alias="isDeleted")]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
