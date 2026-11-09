

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CaseType(UniversalBaseModel):
    area_of_law: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="areaOfLaw"), pydantic.Field(alias="areaOfLaw")
    ] = None
    area_of_law_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="areaOfLawId"), pydantic.Field(alias="areaOfLawId")
    ] = None
    case_class: typing_extensions.Annotated[str, FieldMetadata(alias="caseClass"), pydantic.Field(alias="caseClass")]
    case_class_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="caseClassId"), pydantic.Field(alias="caseClassId")
    ]
    case_type_group: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="caseTypeGroup"), pydantic.Field(alias="caseTypeGroup")
    ] = None
    case_type_group_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="caseTypeGroupId"), pydantic.Field(alias="caseTypeGroupId")
    ] = None
    case_type_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="caseTypeId"), pydantic.Field(alias="caseTypeId")
    ]
    case_type_tag: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="caseTypeTag"), pydantic.Field(alias="caseTypeTag")
    ] = None
    created_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdDate"),
        pydantic.Field(
            alias="createdDate",
            description="The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS.",
        ),
    ]
    """
    The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS.
    """

    name: typing.Optional[str] = None
    object: str
    sali_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="saliCode"), pydantic.Field(alias="saliCode")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
