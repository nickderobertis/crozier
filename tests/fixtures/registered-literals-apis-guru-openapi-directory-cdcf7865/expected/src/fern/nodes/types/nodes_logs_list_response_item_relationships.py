

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NodesLogsListResponseItemRelationships(UniversalBaseModel):
    """
    URLs to other entities or entity collections that have a relationship to the log.
    """

    linked_node: typing.Optional[str] = pydantic.Field(default=None)
    """
    A relationship to the node linked to this log.
    """

    node: typing.Optional[str] = pydantic.Field(default=None)
    """
    A relationship to the node associated with this log.
    """

    original_node: typing.Optional[str] = pydantic.Field(default=None)
    """
    A relationship to the original node that was associated with this log, in case this log was copied from a node to a fork or registration.
    """

    template_node: typing.Optional[str] = pydantic.Field(default=None)
    """
    A relationship to the node used as a template for this log.
    """

    user: typing.Optional[str] = pydantic.Field(default=None)
    """
    A relationship to the user who performed the log action.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
