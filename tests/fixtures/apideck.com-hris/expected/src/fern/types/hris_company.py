

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .created_at import CreatedAt
from .created_by import CreatedBy
from .email import Email
from .hris_company_status import HrisCompanyStatus
from .id import Id
from .phone_number import PhoneNumber
from .updated_at import UpdatedAt
from .updated_by import UpdatedBy
from .website import Website


class HrisCompany(UniversalBaseModel):
    addresses: typing.Optional[typing.List[Address]] = None
    company_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    An Company Number, Company ID or Company Code, is a unique number that has been assigned to each company.
    """

    created_at: typing.Optional[CreatedAt] = None
    created_by: typing.Optional[CreatedBy] = None
    debtor_id: typing.Optional[str] = None
    deleted: typing.Optional[bool] = None
    display_name: typing.Optional[str] = None
    emails: typing.Optional[typing.List[Email]] = None
    id: typing.Optional[Id] = None
    legal_name: str
    phone_numbers: typing.Optional[typing.List[PhoneNumber]] = None
    status: typing.Optional[HrisCompanyStatus] = None
    subdomain: typing.Optional[str] = None
    updated_at: typing.Optional[UpdatedAt] = None
    updated_by: typing.Optional[UpdatedBy] = None
    websites: typing.Optional[typing.List[Website]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
