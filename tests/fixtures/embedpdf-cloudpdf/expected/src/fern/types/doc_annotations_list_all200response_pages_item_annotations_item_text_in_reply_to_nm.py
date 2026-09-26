

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_text_in_reply_to_nm_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextInReplyToNmPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextInReplyToNm(UniversalBaseModel):
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextInReplyToNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
