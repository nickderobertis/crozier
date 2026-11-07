

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ProblemDetailDto(UniversalBaseModel):
    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    A URI reference that identifies the problem type
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    A short, human-readable summary of the problem type
    """

    status: typing.Optional[int] = pydantic.Field(default=None)
    """
    The HTTP status code
    """

    detail: typing.Optional[str] = pydantic.Field(default=None)
    """
    A human-readable explanation specific to this occurrence of the problem
    """

    instance: typing.Optional[str] = pydantic.Field(default=None)
    """
    A URI reference that identifies the specific occurrence of the problem
    """

    properties: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]] = pydantic.Field(default=None)
    """
    Additional properties specific to the problem type
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
