

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok68(UniversalBaseModel):
    medication_history_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="medicationHistoryId"), pydantic.Field(alias="medicationHistoryId")
    ]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    pbm_id: typing_extensions.Annotated[str, FieldMetadata(alias="pbmId"), pydantic.Field(alias="pbmId")]
    source: str
    drug_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="drugDescription"), pydantic.Field(alias="drugDescription")
    ]
    ndc_id: typing_extensions.Annotated[str, FieldMetadata(alias="ndcId"), pydantic.Field(alias="ndcId")]
    quantity: str
    days_supply: typing_extensions.Annotated[str, FieldMetadata(alias="daysSupply"), pydantic.Field(alias="daysSupply")]
    directions: str
    refills: str
    is_substitution_allowed: typing_extensions.Annotated[
        str, FieldMetadata(alias="isSubstitutionAllowed"), pydantic.Field(alias="isSubstitutionAllowed")
    ]
    last_fill_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="lastFillDate"), pydantic.Field(alias="lastFillDate")
    ]
    written_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="writtenDate"), pydantic.Field(alias="writtenDate")
    ]
    note: str
    prior_authorization_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="priorAuthorizationStatus"), pydantic.Field(alias="priorAuthorizationStatus")
    ]
    pharmacy_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="pharmacyName"), pydantic.Field(alias="pharmacyName")
    ]
    pharmacy_address_line1: typing_extensions.Annotated[
        str, FieldMetadata(alias="pharmacyAddressLine1"), pydantic.Field(alias="pharmacyAddressLine1")
    ]
    pharmacy_city: typing_extensions.Annotated[
        str, FieldMetadata(alias="pharmacyCity"), pydantic.Field(alias="pharmacyCity")
    ]
    pharmacy_state: typing_extensions.Annotated[
        str, FieldMetadata(alias="pharmacyState"), pydantic.Field(alias="pharmacyState")
    ]
    pharmacy_zip: typing_extensions.Annotated[
        str, FieldMetadata(alias="pharmacyZip"), pydantic.Field(alias="pharmacyZip")
    ]
    pharmacy_phone_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="pharmacyPhoneNumber"), pydantic.Field(alias="pharmacyPhoneNumber")
    ]
    prescriber_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="prescriberName"), pydantic.Field(alias="prescriberName")
    ]
    prescriber_address_line1: typing_extensions.Annotated[
        str, FieldMetadata(alias="prescriberAddressLine1"), pydantic.Field(alias="prescriberAddressLine1")
    ]
    prescriber_city: typing_extensions.Annotated[
        str, FieldMetadata(alias="prescriberCity"), pydantic.Field(alias="prescriberCity")
    ]
    prescriber_state: typing_extensions.Annotated[
        str, FieldMetadata(alias="prescriberState"), pydantic.Field(alias="prescriberState")
    ]
    prescriber_zip: typing_extensions.Annotated[
        str, FieldMetadata(alias="prescriberZip"), pydantic.Field(alias="prescriberZip")
    ]
    prescriber_phone_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="prescriberPhoneNumber"), pydantic.Field(alias="prescriberPhoneNumber")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
