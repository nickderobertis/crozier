

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .skg_if_next_page import SkgIfNextPage
from .skg_if_part_of import SkgIfPartOf
from .skg_if_prev_page import SkgIfPrevPage


class SkgIfResponseMeta(UniversalBaseModel):
    local_identifier: typing.Optional[str] = None
    entity_type: typing.Optional[str] = None
    prev_page: typing.Optional[SkgIfPrevPage] = None
    next_page: typing.Optional[SkgIfNextPage] = None
    part_of: typing.Optional[SkgIfPartOf] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
