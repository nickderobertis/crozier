

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PipelineGetAllPipelinesResponseItemsItemTriggerActor(UniversalBaseModel):
    """
    The user who triggered the Pipeline.
    """

    login: str = pydantic.Field()
    """
    The login information for the user on the VCS.
    """

    avatar_url: str = pydantic.Field()
    """
    URL to the user's avatar on the VCS
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
