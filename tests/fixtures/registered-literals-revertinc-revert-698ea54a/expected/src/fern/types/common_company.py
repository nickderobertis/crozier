

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .common_common_unified_fields import CommonCommonUnifiedFields
from .common_company_address import CommonCompanyAddress


class CommonCompany(CommonCommonUnifiedFields):
    name: str = pydantic.Field()
    """
    Name of the company in a CRM.
    """

    industry: str = pydantic.Field()
    """
    Industry associated with this company. (not supported by pipedrive)
    """

    description: str = pydantic.Field()
    """
    Description of the company. (not supported by pipedrive)
    """

    annual_revenue: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="annualRevenue"),
        pydantic.Field(
            alias="annualRevenue", description="Annual revenue of the company. (not supported by pipedrive)"
        ),
    ]
    """
    Annual revenue of the company. (not supported by pipedrive)
    """

    size: int = pydantic.Field()
    """
    Number of employees or size of the company.
    """

    phone: str = pydantic.Field()
    """
    Phone number of the company. (not supported by pipedrive)
    """

    address: CommonCompanyAddress = pydantic.Field()
    """
    Company address.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
