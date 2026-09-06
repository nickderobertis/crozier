

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .pagination_properties import PaginationProperties
from .terms_and_conditions_item import TermsAndConditionsItem


class TermsAndConditionsPage(PaginationProperties):
    content: typing.Optional[typing.List[TermsAndConditionsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
