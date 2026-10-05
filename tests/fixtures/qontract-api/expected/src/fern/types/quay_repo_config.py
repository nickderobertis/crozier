

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class QuayRepoConfig(UniversalBaseModel):
    """
    Desired state for a single Quay repository.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Repository description
    """

    name: str = pydantic.Field()
    """
    Repository name
    """

    public: bool = pydantic.Field()
    """
    Whether the repository should be public
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
