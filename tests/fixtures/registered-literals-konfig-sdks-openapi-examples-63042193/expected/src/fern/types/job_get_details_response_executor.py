

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class JobGetDetailsResponseExecutor(UniversalBaseModel):
    """
    Information about executor used for a job.
    """

    resource_class: str = pydantic.Field()
    """
    Resource class name.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Executor type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
