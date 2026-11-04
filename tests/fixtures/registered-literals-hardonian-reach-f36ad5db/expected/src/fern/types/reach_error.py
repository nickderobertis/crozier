

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ReachError(UniversalBaseModel):
    error: str = pydantic.Field()
    """
    Human-readable error message
    """

    code: str = pydantic.Field()
    """
    Machine-readable error code
    """

    details: typing.Optional[typing.Dict[str, typing.Any]] = None
    remediation: typing.Optional[str] = pydantic.Field(default=None)
    """
    Suggested action to resolve the error
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
