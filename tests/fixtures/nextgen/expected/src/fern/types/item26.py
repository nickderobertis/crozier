

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Item26(UniversalBaseModel):
    id: str
    order_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="orderNumber"), pydantic.Field(alias="orderNumber")
    ]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    order_test_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="orderTestId"), pydantic.Field(alias="orderTestId")
    ]
    diagnosis_code_library_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeLibraryId"), pydantic.Field(alias="diagnosisCodeLibraryId")
    ]
    diagnosis_code_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="diagnosisCodeId"), pydantic.Field(alias="diagnosisCodeId")
    ]
    description: str
    icd9cm_code_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="icd9cmCodeId"), pydantic.Field(alias="icd9cmCodeId")
    ]
    user_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="userDescription"), pydantic.Field(alias="userDescription")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
