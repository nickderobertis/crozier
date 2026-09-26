

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_ref_nm_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRefNmPage,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRefNm(UniversalBaseModel):
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
