

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .dna_oligo_helm import DnaOligoHelm
from .pagination import Pagination


class DnaOligosPaginatedListHelm(Pagination):
    dna_oligos: typing_extensions.Annotated[
        typing.Optional[typing.List[DnaOligoHelm]], FieldMetadata(alias="dnaOligos"), pydantic.Field(alias="dnaOligos")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
