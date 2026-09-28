

from __future__ import annotations

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ...types.expectation import Expectation


class PutMockserverGenerateExpectationResponse(UniversalBaseModel):
    suggestions: typing.Optional[typing.List[Expectation]] = None
    confidence: typing.Optional[float] = None
    preview: typing.Optional[bool] = None
    explanation: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(PutMockserverGenerateExpectationResponse)
