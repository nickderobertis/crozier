

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Item24(UniversalBaseModel):
    id: str
    person_payer_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="personPayerId"), pydantic.Field(alias="personPayerId")
    ]
    payer_id: typing_extensions.Annotated[str, FieldMetadata(alias="payerId"), pydantic.Field(alias="payerId")]
    insured_person_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="insuredPersonId"), pydantic.Field(alias="insuredPersonId")
    ]
    cob: str
    order_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="orderNumber"), pydantic.Field(alias="orderNumber")
    ]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    last_name: typing_extensions.Annotated[str, FieldMetadata(alias="lastName"), pydantic.Field(alias="lastName")]
    first_name: typing_extensions.Annotated[str, FieldMetadata(alias="firstName"), pydantic.Field(alias="firstName")]
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    payer_name: typing_extensions.Annotated[str, FieldMetadata(alias="payerName"), pydantic.Field(alias="payerName")]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
