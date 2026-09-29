

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .big_query_computed_field_definition import BigQueryComputedFieldDefinition


class BigqueryComputedFieldMetadata(UniversalBaseModel):
    comment: typing.Optional[str] = None
    definition: BigQueryComputedFieldDefinition
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
