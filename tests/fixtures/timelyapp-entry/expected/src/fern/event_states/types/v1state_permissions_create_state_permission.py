

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1StatePermissionsCreateStatePermission(UniversalBaseModel):
    role_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Role IDs to grant state permissions to
    """

    team_lead: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether team leads have this permission
    """

    project_lead: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether project leads have this permission
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
