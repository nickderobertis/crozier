

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .action import Action
from .collection_info import CollectionInfo


class ActionCollection(CollectionInfo):
    """
    A collection of actions.

    *New in version 2.1.0*
    """

    actions: typing.Optional[typing.List[Action]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
