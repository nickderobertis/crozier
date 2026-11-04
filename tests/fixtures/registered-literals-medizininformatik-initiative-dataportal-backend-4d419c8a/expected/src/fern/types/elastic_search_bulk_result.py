

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .elastic_search_result_entry_extended import ElasticSearchResultEntryExtended


class ElasticSearchBulkResult(UniversalBaseModel):
    ui_profile_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uiProfileId"), pydantic.Field(alias="uiProfileId")
    ] = None
    found: typing.Optional[typing.List[ElasticSearchResultEntryExtended]] = None
    not_found: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="notFound"), pydantic.Field(alias="notFound")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
