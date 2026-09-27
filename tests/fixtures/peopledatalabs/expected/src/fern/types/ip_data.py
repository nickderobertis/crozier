

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ip_data_company import IpDataCompany
from .ip_data_ip import IpDataIp
from .ip_data_person import IpDataPerson


class IpData(UniversalBaseModel):
    """
    The information about the IP address from the ip input parameter.
    """

    ip: typing.Optional[IpDataIp] = pydantic.Field(default=None)
    """
    Information related to the IP address.
    """

    company: typing.Optional[IpDataCompany] = pydantic.Field(default=None)
    """
    Information related to the company associated with the IP address.
    """

    person: typing.Optional[IpDataPerson] = pydantic.Field(default=None)
    """
    Information related to the person associated with the IP address.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
