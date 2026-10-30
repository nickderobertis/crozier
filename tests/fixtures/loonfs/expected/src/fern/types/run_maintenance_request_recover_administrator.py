

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .principal_id import PrincipalId


class RunMaintenanceRequestRecoverAdministrator(UniversalBaseModel):
    """
    A job that restores a root administrator.
    """

    principal_id: PrincipalId = pydantic.Field()
    """
    The principal that receives administrator rights.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
