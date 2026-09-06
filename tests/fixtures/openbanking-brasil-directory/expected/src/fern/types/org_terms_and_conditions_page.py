

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .org_terms_and_conditions_detail import OrgTermsAndConditionsDetail
from .pagination_properties import PaginationProperties


class OrgTermsAndConditionsPage(PaginationProperties):
    content: typing.Optional[typing.List[OrgTermsAndConditionsDetail]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
