

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok42(UniversalBaseModel):
    id: str
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    order_id: typing_extensions.Annotated[str, FieldMetadata(alias="orderId"), pydantic.Field(alias="orderId")]
    cvx_code: typing_extensions.Annotated[str, FieldMetadata(alias="cvxCode"), pydantic.Field(alias="cvxCode")]
    description: str
    cpt_code: typing_extensions.Annotated[str, FieldMetadata(alias="cptCode"), pydantic.Field(alias="cptCode")]
    sequence_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="sequenceNumber"), pydantic.Field(alias="sequenceNumber")
    ]
    status: str
    lot_number: typing_extensions.Annotated[str, FieldMetadata(alias="lotNumber"), pydantic.Field(alias="lotNumber")]
    administered_year: typing_extensions.Annotated[
        str, FieldMetadata(alias="administeredYear"), pydantic.Field(alias="administeredYear")
    ]
    administered_month: typing_extensions.Annotated[
        str, FieldMetadata(alias="administeredMonth"), pydantic.Field(alias="administeredMonth")
    ]
    administered_day: typing_extensions.Annotated[
        str, FieldMetadata(alias="administeredDay"), pydantic.Field(alias="administeredDay")
    ]
    administered_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="administeredDate"), pydantic.Field(alias="administeredDate")
    ]
    administered_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="administeredTimestamp"), pydantic.Field(alias="administeredTimestamp")
    ]
    administered_by_user_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="administeredByUserId"), pydantic.Field(alias="administeredByUserId")
    ]
    administered_by_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="administeredByName"), pydantic.Field(alias="administeredByName")
    ]
    is_vfc: typing_extensions.Annotated[str, FieldMetadata(alias="isVfc"), pydantic.Field(alias="isVfc")]
    vfc_code: typing_extensions.Annotated[str, FieldMetadata(alias="vfcCode"), pydantic.Field(alias="vfcCode")]
    funding_source_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="fundingSourceCode"), pydantic.Field(alias="fundingSourceCode")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
