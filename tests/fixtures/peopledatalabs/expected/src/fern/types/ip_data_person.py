

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ip_data_person_confidence import IpDataPersonConfidence
from .ip_data_person_job_title_levels import IpDataPersonJobTitleLevels
from .ip_data_person_job_title_role import IpDataPersonJobTitleRole
from .ip_data_person_job_title_sub_role import IpDataPersonJobTitleSubRole


class IpDataPerson(UniversalBaseModel):
    """
    Information related to the person associated with the IP address.
    """

    confidence: typing.Optional[IpDataPersonConfidence] = pydantic.Field(default=None)
    """
    How confident we are that the returned person is associated with requested IP.
    """

    job_title_role: typing.Optional[IpDataPersonJobTitleRole] = pydantic.Field(default=None)
    """
    A person's current job title derived role
    """

    job_title_sub_role: typing.Optional[IpDataPersonJobTitleSubRole] = pydantic.Field(default=None)
    """
    A person's job title derived subrole. Each subrole maps to a role
    """

    job_title_levels: typing.Optional[IpDataPersonJobTitleLevels] = pydantic.Field(default=None)
    """
    A person's current job title derived levels
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
