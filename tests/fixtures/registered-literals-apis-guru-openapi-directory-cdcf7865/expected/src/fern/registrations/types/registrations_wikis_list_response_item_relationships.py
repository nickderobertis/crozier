

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegistrationsWikisListResponseItemRelationships(UniversalBaseModel):
    """
    URLs to other entities or entity collections that have a relationship to the wiki.
    """

    comments: str = pydantic.Field()
    """
    A relationship to the comments related to this wiki.
    """

    node: str = pydantic.Field()
    """
    A relationship to the associated node.
    """

    user: str = pydantic.Field()
    """
    A relationship to the user associated with this wiki.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
