

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AnalysisUpdateEval(UniversalBaseModel):
    """
    Evaluation Results for an entity (current or last)
    """

    analysis_status: typing.Optional[str] = None
    annotations: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    image_digest: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
