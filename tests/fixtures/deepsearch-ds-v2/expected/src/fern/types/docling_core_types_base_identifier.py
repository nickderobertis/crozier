

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DoclingCoreTypesBaseIdentifier(UniversalBaseModel):
    """
    Unique identifier of a Docling data object.
    """

    type: str = pydantic.Field()
    """
    A string representing a collection or database that contains this data object.
    """

    value: str = pydantic.Field()
    """
    The identifier value of the data object within a collection or database.
    """

    name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="_name"),
        pydantic.Field(
            alias="_name",
            description="A unique identifier of the data object across Docling, consisting of the concatenation of type and value in lower case, separated by hash (#).",
        ),
    ]
    """
    A unique identifier of the data object across Docling, consisting of the concatenation of type and value in lower case, separated by hash (#).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
