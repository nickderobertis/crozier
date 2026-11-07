

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AllServerJobsDataItem(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the agent
    """

    running: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of running instances
    """

    pending: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of pending instances
    """

    eta: typing.Optional[str] = pydantic.Field(default=None)
    """
    Estimated time of arrival
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
