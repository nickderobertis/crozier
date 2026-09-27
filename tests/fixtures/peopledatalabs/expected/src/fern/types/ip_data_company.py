

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .company_location import CompanyLocation
from .ip_data_company_confidence import IpDataCompanyConfidence
from .ip_data_company_size import IpDataCompanySize


class IpDataCompany(UniversalBaseModel):
    """
    Information related to the company associated with the IP address.
    """

    confidence: typing.Optional[IpDataCompanyConfidence] = pydantic.Field(default=None)
    """
    How confident we are that the returned company is associated with requested IP.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The PDL ID of the company associated with the IP address.
    """

    website: typing.Optional[str] = pydantic.Field(default=None)
    """
    The primary website of the company associated with the IP address.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the company associated with the IP address.
    """

    location: typing.Optional[CompanyLocation] = pydantic.Field(default=None)
    """
    The location of the company's primary HQ associated with the IP address.
    """

    size: typing.Optional[IpDataCompanySize] = pydantic.Field(default=None)
    """
    The self-reported size range of the company associated with the IP address.
    """

    industry: typing.Optional[str] = pydantic.Field(default=None)
    """
    The self-reported industry of the company associated with the IP address.
    """

    inferred_revenue: typing.Optional[str] = pydantic.Field(default=None)
    """
    The estimated annual revenue (in USD) of the company associated with the IP address.
    """

    employee_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The current number of employees working at the company associated with the IP address.
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Tags associated with the company associated with the IP address.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
