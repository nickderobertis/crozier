

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class IncomeVerificationPrecheckMilitaryInfo(UniversalBaseModel):
    """
    Data about military info in the income verification precheck.
    """

    branch: typing.Optional[str] = pydantic.Field(default=None)
    """
    If the user is currently serving in the US military, the branch of the military in which they are serving
    Valid values: 'AIR FORCE', 'ARMY', 'COAST GUARD', 'MARINES', 'NAVY', 'UNKNOWN'
    """

    is_active_duty: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Is the user currently active duty in the US military
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
