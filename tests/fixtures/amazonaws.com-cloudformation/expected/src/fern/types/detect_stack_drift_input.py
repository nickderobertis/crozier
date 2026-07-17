

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .logical_resource_id import LogicalResourceId


class DetectStackDriftInput(UniversalBaseModel):
    stack_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="StackName"),
        pydantic.Field(alias="StackName", description="The name of the stack for which you want to detect drift."),
    ]
    """
    The name of the stack for which you want to detect drift.
    """

    logical_resource_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[LogicalResourceId]],
        FieldMetadata(alias="LogicalResourceIds"),
        pydantic.Field(
            alias="LogicalResourceIds", description="The logical names of any resources you want to use as filters."
        ),
    ] = None
    """
    The logical names of any resources you want to use as filters.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
