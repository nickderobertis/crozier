

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .insurance_pension_enum_pmbac_remuneration_update_indexes_item import (
    InsurancePensionEnumPmbacRemunerationUpdateIndexesItem,
)


class InsurancePensionEnumPmbacRemuneration(UniversalBaseModel):
    interest_rate: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="interestRate"),
        pydantic.Field(alias="interestRate", description="Taxa de juros para capitalização da PMBaC"),
    ] = None
    """
    Taxa de juros para capitalização da PMBaC
    """

    update_indexes: typing_extensions.Annotated[
        typing.Optional[typing.List[InsurancePensionEnumPmbacRemunerationUpdateIndexesItem]],
        FieldMetadata(alias="updateIndexes"),
        pydantic.Field(alias="updateIndexes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
