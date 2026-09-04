

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .identifier_type import IdentifierType


class Identifier(UniversalBaseModel):
    """
    An identifier with a specified type
    """

    id_type: typing_extensions.Annotated[
        typing.Optional[IdentifierType],
        FieldMetadata(alias="idType"),
        pydantic.Field(alias="idType", description="Type of identifier, e.g. `TEI`, `PURL`, `CPE`"),
    ] = None
    """
    Type of identifier, e.g. `TEI`, `PURL`, `CPE`
    """

    id_value: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="idValue"),
        pydantic.Field(alias="idValue", description="Identifier value"),
    ] = None
    """
    Identifier value
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
