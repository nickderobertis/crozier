

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_post_response_data_item_results import QueryPostResponseDataItemResults


class QueryPostResponseDataItem(UniversalBaseModel):
    notebook_uuid: typing_extensions.Annotated[
        str, FieldMetadata(alias="notebookUuid"), pydantic.Field(alias="notebookUuid")
    ]
    results: typing.Optional[QueryPostResponseDataItemResults] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
