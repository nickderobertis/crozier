

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Dbv0037AssociationUsage(UniversalBaseModel):
    """
    Association usage
    """

    accrue_job_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Jobs accuring priority
    """

    group_used_wallclock: typing.Optional[float] = pydantic.Field(default=None)
    """
    Group used wallclock time (s)
    """

    fairshare_factor: typing.Optional[float] = pydantic.Field(default=None)
    """
    Fairshare factor
    """

    fairshare_shares: typing.Optional[int] = pydantic.Field(default=None)
    """
    Fairshare shares
    """

    normalized_priority: typing.Optional[int] = pydantic.Field(default=None)
    """
    Currently active jobs
    """

    normalized_shares: typing.Optional[float] = pydantic.Field(default=None)
    """
    Normalized shares
    """

    effective_normalized_usage: typing.Optional[float] = pydantic.Field(default=None)
    """
    Effective normalized usage
    """

    raw_usage: typing.Optional[int] = pydantic.Field(default=None)
    """
    Raw usage
    """

    job_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total jobs submitted
    """

    fairshare_level: typing.Optional[float] = pydantic.Field(default=None)
    """
    Fairshare level
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
