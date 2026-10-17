

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v1project_advisors_response_output_lints_item_metadata_type import (
    V1ProjectAdvisorsResponseOutputLintsItemMetadataType,
)


class V1ProjectAdvisorsResponseOutputLintsItemMetadata(UniversalBaseModel):
    schema_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="schema"), pydantic.Field(alias="schema")
    ] = None
    name: typing.Optional[str] = None
    entity: typing.Optional[str] = None
    type: typing.Optional[V1ProjectAdvisorsResponseOutputLintsItemMetadataType] = None
    fkey_name: typing.Optional[str] = None
    fkey_columns: typing.Optional[typing.List[float]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
