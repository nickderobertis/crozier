

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .patch_document_op import PatchDocumentOp


class PatchDocument(UniversalBaseModel):
    """
    A JSONPatch document as defined by RFC 6902
    """

    op: PatchDocumentOp = pydantic.Field()
    """
    The operation to be performed
    """

    path: str = pydantic.Field()
    """
    A JSON-Pointer
    """

    value: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The value to be used within the operations.
    """

    from_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="from"),
        pydantic.Field(alias="from", description="A string containing a JSON Pointer value."),
    ] = None
    """
    A string containing a JSON Pointer value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
