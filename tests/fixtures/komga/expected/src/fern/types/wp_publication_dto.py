

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .wp_link_dto import WpLinkDto
from .wp_metadata_dto import WpMetadataDto


class WpPublicationDto(UniversalBaseModel):
    context: typing.Optional[str] = None
    images: typing.List[WpLinkDto]
    landmarks: typing.List[WpLinkDto]
    links: typing.List[WpLinkDto]
    metadata: WpMetadataDto
    page_list: typing_extensions.Annotated[
        typing.List[WpLinkDto], FieldMetadata(alias="pageList"), pydantic.Field(alias="pageList")
    ]
    reading_order: typing_extensions.Annotated[
        typing.List[WpLinkDto], FieldMetadata(alias="readingOrder"), pydantic.Field(alias="readingOrder")
    ]
    resources: typing.List[WpLinkDto]
    toc: typing.List[WpLinkDto]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
