

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PipRequirement(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Name of the pip package.
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional version of the package, following semantic versioning.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
