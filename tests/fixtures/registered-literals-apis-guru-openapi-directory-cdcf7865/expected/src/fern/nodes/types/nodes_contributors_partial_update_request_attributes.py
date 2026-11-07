

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nodes_contributors_partial_update_request_attributes_permission import (
    NodesContributorsPartialUpdateRequestAttributesPermission,
)


class NodesContributorsPartialUpdateRequestAttributes(UniversalBaseModel):
    """
    The properties of the contributor entity.
    """

    bibliographic: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the contributor will be included in citations for the node. The default value is true.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The position of this contributor in the list of project contributors and in project citations.
    """

    permission: typing.Optional[NodesContributorsPartialUpdateRequestAttributesPermission] = pydantic.Field(
        default=None
    )
    """
    The permission level of the contributor. The default value is 'write'.
    """

    unregistered_contributor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The assigned name of the contributor if the contributor has not yet claimed their account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
