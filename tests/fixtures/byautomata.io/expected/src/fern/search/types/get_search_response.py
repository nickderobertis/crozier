

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.similar_company_search import SimilarCompanySearch


class GetSearchResponse(UniversalBaseModel):
    calls_per_month: typing.Optional[str] = None
    companies: typing.Optional[typing.List[SimilarCompanySearch]] = None
    count_remaining: typing.Optional[str] = None
    renewal_date: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
