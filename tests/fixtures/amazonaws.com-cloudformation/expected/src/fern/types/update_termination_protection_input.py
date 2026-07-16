

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UpdateTerminationProtectionInput(UniversalBaseModel):
    enable_termination_protection: typing_extensions.Annotated[
        bool, FieldMetadata(alias="EnableTerminationProtection")
    ] = pydantic.Field()
    """
    Whether to enable termination protection on the specified stack.
    """

    stack_name: typing_extensions.Annotated[str, FieldMetadata(alias="StackName")] = pydantic.Field()
    """
    The name or unique ID of the stack for which you want to set termination protection.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
