

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .lineage_confidence_assertion import LineageConfidenceAssertion
from .lineage_derivation_input import LineageDerivationInput
from .lineage_transformation import LineageTransformation


class LineageDerivation(UniversalBaseModel):
    """
    One explicit hyperedge: an activity generated exactly one output entity from zero or more typed input entities.
    """

    id: typing.Optional[str] = None
    output: str
    activity: str
    inputs: typing.List[LineageDerivationInput]
    transformation: typing.Optional[LineageTransformation] = None
    confidence: typing.Optional[LineageConfidenceAssertion] = None
    attributes: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
