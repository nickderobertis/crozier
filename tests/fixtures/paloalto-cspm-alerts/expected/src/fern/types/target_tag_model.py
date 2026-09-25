

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TargetTagModel(UniversalBaseModel):
    """
    Model for Target Tag
    """

    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    Resource tag target
    """

    values: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of value(s) for resource tag key
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
