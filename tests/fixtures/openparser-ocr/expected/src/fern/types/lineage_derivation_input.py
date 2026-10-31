

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .lineage_confidence_assertion import LineageConfidenceAssertion
from .lineage_derivation_input_effect import LineageDerivationInputEffect


class LineageDerivationInput(UniversalBaseModel):
    entity: str
    role: typing.Optional[str] = None
    effect: LineageDerivationInputEffect
    confidence: typing.Optional[LineageConfidenceAssertion] = None
    attributes: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
