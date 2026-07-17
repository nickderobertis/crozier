

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DetectStackResourceDriftInput(UniversalBaseModel):
    stack_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="StackName"),
        pydantic.Field(alias="StackName", description="The name of the stack to which the resource belongs."),
    ]
    """
    The name of the stack to which the resource belongs.
    """

    logical_resource_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="LogicalResourceId"),
        pydantic.Field(
            alias="LogicalResourceId",
            description="The logical name of the resource for which to return drift information.",
        ),
    ]
    """
    The logical name of the resource for which to return drift information.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
