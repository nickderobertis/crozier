

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_pages_viewports200response_item_bbox import DocPagesViewports200ResponseItemBbox
from .doc_pages_viewports200response_item_measure import DocPagesViewports200ResponseItemMeasure


class DocPagesViewports200ResponseItem(UniversalBaseModel):
    bbox: DocPagesViewports200ResponseItemBbox
    name: typing.Optional[str] = None
    measure: typing.Optional[DocPagesViewports200ResponseItemMeasure] = None
    owned: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
