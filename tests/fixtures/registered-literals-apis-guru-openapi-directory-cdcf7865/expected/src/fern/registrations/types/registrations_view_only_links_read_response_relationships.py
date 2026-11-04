

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegistrationsViewOnlyLinksReadResponseRelationships(UniversalBaseModel):
    """
    URLs to other entities or entity collections that have a relationship to the view only link entity.
    """

    creator: typing.Optional[str] = pydantic.Field(default=None)
    """
    A relationship to the user who created this view only link.
    """

    nodes: str = pydantic.Field()
    """
    A relationship to the nodes which this view only link gives read-only access to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
