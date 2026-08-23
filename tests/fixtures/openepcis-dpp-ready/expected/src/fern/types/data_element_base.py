

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DataElementBase(UniversalBaseModel):
    element_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="elementId"),
        pydantic.Field(
            alias="elementId", description="Relative identifier; unique within its scope (EN 18223 clause 4.1.2.3)."
        ),
    ]
    """
    Relative identifier; unique within its scope (EN 18223 clause 4.1.2.3).
    """

    dictionary_reference: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="dictionaryReference"),
        pydantic.Field(
            alias="dictionaryReference", description="Resolvable IRI into the EN 18223 clause 4.3 data dictionary."
        ),
    ] = None
    """
    Resolvable IRI into the EN 18223 clause 4.3 data dictionary.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
