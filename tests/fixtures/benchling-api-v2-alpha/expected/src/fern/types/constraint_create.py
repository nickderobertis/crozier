

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .constraint_create_fields_item import ConstraintCreateFieldsItem


class ConstraintCreate(UniversalBaseModel):
    are_unique_residues_case_sensitive: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="areUniqueResiduesCaseSensitive"),
        pydantic.Field(alias="areUniqueResiduesCaseSensitive"),
    ] = None
    fields: typing.Optional[typing.List[ConstraintCreateFieldsItem]] = None
    has_unique_canonical_smiles: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasUniqueCanonicalSmiles"),
        pydantic.Field(alias="hasUniqueCanonicalSmiles"),
    ] = None
    has_unique_residues: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hasUniqueResidues"), pydantic.Field(alias="hasUniqueResidues")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
