

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class JobGetDetailsResponseLatestWorkflow(UniversalBaseModel):
    """
    Info about the latest workflow the job was a part of.
    """

    id: str = pydantic.Field()
    """
    The unique ID of the workflow.
    """

    name: str = pydantic.Field()
    """
    The name of the workflow.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
