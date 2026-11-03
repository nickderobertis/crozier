

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .glossary import Glossary


class Packet(UniversalBaseModel):
    species: str
    viability: float = pydantic.Field()
    """
    Germination rate as a fraction.
    """

    viability_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="viability (%)"),
        pydantic.Field(alias="viability (%)", description="Germination rate as a percentage label."),
    ] = None
    """
    Germination rate as a percentage label.
    """

    dict_: typing_extensions.Annotated[Glossary, FieldMetadata(alias="dict"), pydantic.Field(alias="dict")]
    moisture_: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="moisture (%)"),
        pydantic.Field(alias="moisture (%)", description="Moisture content, with no sibling sharing its stem."),
    ] = None
    """
    Moisture content, with no sibling sharing its stem.
    """

    seed__weight: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="seed % weight"),
        pydantic.Field(alias="seed % weight", description="A punctuation-only word between two words."),
    ] = None
    """
    A punctuation-only word between two words.
    """

    lot_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lotCode"), pydantic.Field(alias="lotCode")
    ] = None
    lot_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lotCode_"),
        pydantic.Field(
            alias="lotCode_", description="A second spelling of the lot code, differing by a trailing underscore."
        ),
    ] = None
    """
    A second spelling of the lot code, differing by a trailing underscore.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
