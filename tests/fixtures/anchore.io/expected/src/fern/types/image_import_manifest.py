

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .import_content_digests import ImportContentDigests


class ImageImportManifest(UniversalBaseModel):
    contents: ImportContentDigests
    digest: str
    local_image_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    An "imageId" as used by Docker if available
    """

    operation_uuid: str
    parent_digest: typing.Optional[str] = pydantic.Field(default=None)
    """
    The digest of the images's manifest-list parent if it was accessed from a multi-arch tag where the tag pointed to a manifest-list. This allows preservation of that relationship in the data
    """

    tags: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
