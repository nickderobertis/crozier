

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .employment_source_type import EmploymentSourceType
from .link_token_create_request_employment_bank_income import LinkTokenCreateRequestEmploymentBankIncome


class LinkTokenCreateRequestEmployment(UniversalBaseModel):
    """
    Specifies options for initializing Link for use with the Employment product. This field is required if `employment` is included in the `products` array.
    """

    bank_employment: typing.Optional[LinkTokenCreateRequestEmploymentBankIncome] = None
    employment_source_types: typing.Optional[typing.List[EmploymentSourceType]] = pydantic.Field(default=None)
    """
    The types of source employment data that users will be permitted to share. Options include `bank` and `payroll`. Currently you can only specify one of these options.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
