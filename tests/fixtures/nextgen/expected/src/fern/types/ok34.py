

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok34(UniversalBaseModel):
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    administered_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="administeredDate"), pydantic.Field(alias="administeredDate")
    ]
    group_name: typing_extensions.Annotated[str, FieldMetadata(alias="groupName"), pydantic.Field(alias="groupName")]
    status_code: typing_extensions.Annotated[str, FieldMetadata(alias="statusCode"), pydantic.Field(alias="statusCode")]
    status_message: typing_extensions.Annotated[
        str, FieldMetadata(alias="statusMessage"), pydantic.Field(alias="statusMessage")
    ]
    order_vaccine_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="orderVaccineId"), pydantic.Field(alias="orderVaccineId")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
