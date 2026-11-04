

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.file_revision_metadata_v2 import FileRevisionMetadataV2
from ...types.pagination_links import PaginationLinks


class ValFilesGet2Response(UniversalBaseModel):
    """
    A paginated result set
    """

    data: typing.List[FileRevisionMetadataV2]
    links: PaginationLinks

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
