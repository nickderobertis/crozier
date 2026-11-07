

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .possible_norm_law_firm_source_details_source import PossibleNormLawFirmSourceDetailsSource


class PossibleNormLawFirmSourceDetails(UniversalBaseModel):
    linked_norm_attorney_id_array: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="linkedNormAttorneyIdArray"),
        pydantic.Field(alias="linkedNormAttorneyIdArray"),
    ]
    source: typing.Optional[PossibleNormLawFirmSourceDetailsSource] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
