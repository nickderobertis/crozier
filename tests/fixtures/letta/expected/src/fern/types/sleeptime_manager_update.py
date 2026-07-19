

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SleeptimeManagerUpdate(UniversalBaseModel):
    manager_agent_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    
    """

    sleeptime_agent_frequency: typing.Optional[int] = pydantic.Field(default=None)
    """
    
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
