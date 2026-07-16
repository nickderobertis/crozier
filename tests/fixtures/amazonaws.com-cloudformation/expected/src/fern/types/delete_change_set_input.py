

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DeleteChangeSetInput(UniversalBaseModel):
    """
    The input for the <a>DeleteChangeSet</a> action.
    """

    change_set_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ChangeSetName"),
        pydantic.Field(
            alias="ChangeSetName",
            description="The name or Amazon Resource Name (ARN) of the change set that you want to delete.",
        ),
    ]
    """
    The name or Amazon Resource Name (ARN) of the change set that you want to delete.
    """

    stack_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StackName"),
        pydantic.Field(
            alias="StackName",
            description="If you specified the name of a change set to delete, specify the stack name or Amazon Resource Name (ARN) that's associated with it.",
        ),
    ] = None
    """
    If you specified the name of a change set to delete, specify the stack name or Amazon Resource Name (ARN) that's associated with it.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
