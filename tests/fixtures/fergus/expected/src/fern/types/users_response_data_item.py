

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address_contact import AddressContact
from .links import Links
from .users_response_data_item_status import UsersResponseDataItemStatus
from .users_response_data_item_user_type import UsersResponseDataItemUserType


class UsersResponseDataItem(UniversalBaseModel):
    id: float
    company_id: typing_extensions.Annotated[float, FieldMetadata(alias="companyId"), pydantic.Field(alias="companyId")]
    first_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="firstName"), pydantic.Field(alias="firstName")
    ] = None
    last_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lastName"), pydantic.Field(alias="lastName")
    ] = None
    email: str
    user_type: typing_extensions.Annotated[
        UsersResponseDataItemUserType, FieldMetadata(alias="userType"), pydantic.Field(alias="userType")
    ]
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    modified_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="modifiedAt"), pydantic.Field(alias="modifiedAt")
    ]
    address: AddressContact
    pay_rate: typing_extensions.Annotated[float, FieldMetadata(alias="payRate"), pydantic.Field(alias="payRate")]
    charge_out_rate: typing_extensions.Annotated[
        float, FieldMetadata(alias="chargeOutRate"), pydantic.Field(alias="chargeOutRate")
    ]
    status: UsersResponseDataItemStatus
    links: typing.List[Links]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
