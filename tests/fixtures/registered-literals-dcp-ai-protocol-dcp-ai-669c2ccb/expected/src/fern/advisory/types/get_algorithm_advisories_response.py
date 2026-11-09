

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.algorithm_advisory import AlgorithmAdvisory


class GetAlgorithmAdvisoriesResponse(UniversalBaseModel):
    advisories: typing.Optional[typing.List[AlgorithmAdvisory]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
