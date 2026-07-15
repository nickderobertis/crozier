

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.input_company import InputCompany
from ...types.similar_company import SimilarCompany


class GetSimilarResponse(UniversalBaseModel):
    calls_per_month: typing.Optional[str] = None
    companies: typing.Optional[typing.List[SimilarCompany]] = None
    count_remaining: typing.Optional[str] = None
    input_company: typing.Optional[InputCompany] = None
    renewal_date: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
