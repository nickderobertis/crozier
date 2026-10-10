

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pagination_meta import PaginationMeta
from .show_summary import ShowSummary


class ShowListResponse(UniversalBaseModel):
    """
    Show list response used by Kodi source as `json["shows"]`.
    """

    shows: typing.List[ShowSummary]
    meta: typing.Optional[PaginationMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
