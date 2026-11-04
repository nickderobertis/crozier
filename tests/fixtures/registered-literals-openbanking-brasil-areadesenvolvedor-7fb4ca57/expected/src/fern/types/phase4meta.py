

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Phase4Meta(UniversalBaseModel):
    """
    Meta informações referente à API requisitada.
    """

    total_records: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalRecords"),
        pydantic.Field(alias="totalRecords", description="Número total de registros no resultado"),
    ]
    """
    Número total de registros no resultado
    """

    total_pages: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalPages"),
        pydantic.Field(alias="totalPages", description="Número total de páginas no resultado"),
    ]
    """
    Número total de páginas no resultado
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
