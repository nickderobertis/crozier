

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class JobDefinitionReportOptions(UniversalBaseModel):
    """
    Controls what data is included in the job report
    """

    app_fleets: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include project fleets in the report
    """

    app_info: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include project info in the report
    """

    app_vars: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include project environment variables in the report
    """

    comment: typing.Optional[str] = None
    device_activity: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include device activity data in the report
    """

    device_health: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include device health data in the report
    """

    device_info: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include device info in the report
    """

    device_vars: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include device environment variables in the report
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
