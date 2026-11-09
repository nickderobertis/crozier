

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class JobDefinitionSelect(UniversalBaseModel):
    """
    Device selection criteria
    """

    all_devices: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Select all devices in the project
    """

    comment: typing.Optional[str] = None
    devices: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Specific device UIDs to include
    """

    devices_by_sn: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Serial number patterns to match (supports glob wildcards *, ?, [...])
    """

    devices_in_fleets: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Fleet UIDs whose devices should be included
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
