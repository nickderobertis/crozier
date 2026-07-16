

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Document(UniversalBaseModel):
    """
    Document
    """

    collection: typing_extensions.Annotated[
        str, FieldMetadata(alias="$collection"), pydantic.Field(alias="$collection", description="Collection ID.")
    ]
    """
    Collection ID.
    """

    id: typing_extensions.Annotated[
        str, FieldMetadata(alias="$id"), pydantic.Field(alias="$id", description="Document ID.")
    ]
    """
    Document ID.
    """

    permissions: typing_extensions.Annotated[
        typing.Dict[str, typing.Any],
        FieldMetadata(alias="$permissions"),
        pydantic.Field(alias="$permissions", description="Document permissions."),
    ]
    """
    Document permissions.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
