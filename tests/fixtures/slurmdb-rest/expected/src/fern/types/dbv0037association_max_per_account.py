

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Dbv0037AssociationMaxPerAccount(UniversalBaseModel):
    """
    Max per accounting settings
    """

    wall_clock: typing.Optional[int] = pydantic.Field(default=None)
    """
    Max wallclock per account
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
