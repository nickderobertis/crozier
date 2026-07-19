

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Dbv0037JobComment(UniversalBaseModel):
    """
    Job comments by type
    """

    administrator: typing.Optional[str] = pydantic.Field(default=None)
    """
    Administrator set comment
    """

    job: typing.Optional[str] = pydantic.Field(default=None)
    """
    Job comment
    """

    system: typing.Optional[str] = pydantic.Field(default=None)
    """
    System set comment
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
