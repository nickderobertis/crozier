

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .patch_page_request_cover_external import PatchPageRequestCoverExternal
from .patch_page_request_cover_type import PatchPageRequestCoverType


class PatchPageRequestCover(UniversalBaseModel):
    """
    A cover image for the page. Only [external file objects](https://developers.notion.com/reference/file-object) are supported.
    """

    external: PatchPageRequestCoverExternal
    type: typing.Optional[PatchPageRequestCoverType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
