

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .pipelines_list_pipelines_response_pipelines_item import PipelinesListPipelinesResponsePipelinesItem


class PipelinesListPipelinesResponse(UniversalBaseModel):
    pipelines: typing.List[PipelinesListPipelinesResponsePipelinesItem]
    has_next_page: typing_extensions.Annotated[
        bool, FieldMetadata(alias="hasNextPage"), pydantic.Field(alias="hasNextPage")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
