

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.eval_status_page import EvalStatusPage


class GetEvalStatusPageResponse(UniversalBaseModel):
    objects: typing.List[EvalStatusPage] = pydantic.Field()
    """
    A list of eval_status_page objects
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
