

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OperationDisplay(UniversalBaseModel):
    """
    Operation display
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Localized description of the operation for display purpose.
    """

    operation: typing.Optional[str] = pydantic.Field(default=None)
    """
    Localized name of the operation for display purpose.
    """

    provider: typing.Optional[str] = pydantic.Field(default=None)
    """
    Provider name.
    """

    resource: typing.Optional[str] = pydantic.Field(default=None)
    """
    Resource name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
