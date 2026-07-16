

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CreateStackSetOutput(UniversalBaseModel):
    stack_set_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StackSetId"),
        pydantic.Field(alias="StackSetId", description="The ID of the stack set that you're creating."),
    ] = None
    """
    The ID of the stack set that you're creating.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
