

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entity_result_dto import EntityResultDto
from .page_metadata_dto import PageMetadataDto


class PagedEntityResultsDto(UniversalBaseModel):
    content: typing.Optional[typing.List[EntityResultDto]] = pydantic.Field(default=None)
    """
    List of entity results for the current page
    """

    page: typing.Optional[PageMetadataDto] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
