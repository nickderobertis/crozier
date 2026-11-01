

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InferredReturnsMixedObjectResponseResultData(UniversalBaseModel):
    id: float
    name: str
    tags: typing.List[str]
    metadata: typing.Dict[str, str]
    active: bool
    score: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
