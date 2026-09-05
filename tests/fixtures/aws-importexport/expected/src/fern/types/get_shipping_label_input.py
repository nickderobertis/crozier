

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_version import ApiVersion
from .city import City
from .company import Company
from .country import Country
from .job_id_list import JobIdList
from .name import Name
from .phone_number import PhoneNumber
from .postal_code import PostalCode
from .state_or_province import StateOrProvince
from .street1 import Street1
from .street2 import Street2
from .street3 import Street3


class GetShippingLabelInput(UniversalBaseModel):
    job_ids: typing_extensions.Annotated[JobIdList, FieldMetadata(alias="jobIds"), pydantic.Field(alias="jobIds")]
    name: typing.Optional[Name] = None
    company: typing.Optional[Company] = None
    phone_number: typing_extensions.Annotated[
        typing.Optional[PhoneNumber], FieldMetadata(alias="phoneNumber"), pydantic.Field(alias="phoneNumber")
    ] = None
    country: typing.Optional[Country] = None
    state_or_province: typing_extensions.Annotated[
        typing.Optional[StateOrProvince],
        FieldMetadata(alias="stateOrProvince"),
        pydantic.Field(alias="stateOrProvince"),
    ] = None
    city: typing.Optional[City] = None
    postal_code: typing_extensions.Annotated[
        typing.Optional[PostalCode], FieldMetadata(alias="postalCode"), pydantic.Field(alias="postalCode")
    ] = None
    street1: typing.Optional[Street1] = None
    street2: typing.Optional[Street2] = None
    street3: typing.Optional[Street3] = None
    api_version: typing_extensions.Annotated[
        typing.Optional[ApiVersion], FieldMetadata(alias="APIVersion"), pydantic.Field(alias="APIVersion")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
