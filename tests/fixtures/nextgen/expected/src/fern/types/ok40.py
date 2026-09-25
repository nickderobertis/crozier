

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok40(UniversalBaseModel):
    id: str
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    person_payer_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="personPayerId"), pydantic.Field(alias="personPayerId")
    ]
    payer_id: typing_extensions.Annotated[str, FieldMetadata(alias="payerId"), pydantic.Field(alias="payerId")]
    insured_person_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="insuredPersonId"), pydantic.Field(alias="insuredPersonId")
    ]
    cob: str
    order_id: typing_extensions.Annotated[str, FieldMetadata(alias="orderId"), pydantic.Field(alias="orderId")]
    payer_name: typing_extensions.Annotated[str, FieldMetadata(alias="payerName"), pydantic.Field(alias="payerName")]
    insured_person_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="insuredPersonName"), pydantic.Field(alias="insuredPersonName")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
