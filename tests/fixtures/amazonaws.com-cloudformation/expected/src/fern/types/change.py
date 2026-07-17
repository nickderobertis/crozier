

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .change_resource_change import ChangeResourceChange
from .change_type import ChangeType


class Change(UniversalBaseModel):
    """
    The <code>Change</code> structure describes the changes CloudFormation will perform if you execute the change set.
    """

    type: typing_extensions.Annotated[
        typing.Optional[ChangeType],
        FieldMetadata(alias="Type"),
        pydantic.Field(
            alias="Type",
            description="The type of entity that CloudFormation changes. Currently, the only entity type is <code>Resource</code>.",
        ),
    ] = None
    """
    The type of entity that CloudFormation changes. Currently, the only entity type is <code>Resource</code>.
    """

    hook_invocation_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="HookInvocationCount"),
        pydantic.Field(
            alias="HookInvocationCount",
            description="Is either <code>null</code>, if no hooks invoke for the resource, or contains the number of hooks that will invoke for the resource.",
        ),
    ] = None
    """
    Is either <code>null</code>, if no hooks invoke for the resource, or contains the number of hooks that will invoke for the resource.
    """

    resource_change: typing_extensions.Annotated[
        typing.Optional[ChangeResourceChange],
        FieldMetadata(alias="ResourceChange"),
        pydantic.Field(
            alias="ResourceChange",
            description="A <code>ResourceChange</code> structure that describes the resource and action that CloudFormation will perform.",
        ),
    ] = None
    """
    A <code>ResourceChange</code> structure that describes the resource and action that CloudFormation will perform.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
