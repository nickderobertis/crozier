

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .patch_op import PatchOp
from .patch_value import PatchValue


class Patch(UniversalBaseModel):
    """
    The JSON patch object to apply partial updates to resources.
    """

    op: PatchOp = pydantic.Field()
    """
    The operation.
    """

    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    The <a href="https://tools.ietf.org/html/rfc6901">JSON Pointer</a> to the target document location at which to complete the operation.
    """

    value: typing.Optional[PatchValue] = pydantic.Field(default=None)
    """
    The value to apply. The <code>remove</code> operation does not require a value.
    """

    from_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="from"),
        pydantic.Field(
            alias="from",
            description='The <a href="https://tools.ietf.org/html/rfc6901">JSON Pointer</a> to the target document location from which to move the value. Required for the <code>move</code> operation.',
        ),
    ] = None
    """
    The <a href="https://tools.ietf.org/html/rfc6901">JSON Pointer</a> to the target document location from which to move the value. Required for the <code>move</code> operation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
