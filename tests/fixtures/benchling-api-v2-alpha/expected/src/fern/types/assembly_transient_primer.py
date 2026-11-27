

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AssemblyTransientPrimer(UniversalBaseModel):
    bases: typing.Optional[str] = pydantic.Field(default=None)
    """
    Bases of the primer.
    """

    binding_position: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="bindingPosition"),
        pydantic.Field(alias="bindingPosition", description="Binding position of the primer on the construct."),
    ] = None
    """
    Binding position of the primer on the construct.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
