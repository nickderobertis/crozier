

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .obligation_classification import ObligationClassification


class Obligation(UniversalBaseModel):
    """
    Obligation information
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Id key
    """

    topic: typing.Optional[str] = pydantic.Field(default=None)
    """
    Obligation topic
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of obligation
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    Obligation text
    """

    classification: typing.Optional[ObligationClassification] = pydantic.Field(default=None)
    """
    Level of attention this obligation should raise in the clearing process
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    Comments for the obligation
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
