

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ExtractionReviewRetraction(UniversalBaseModel):
    """
    Take back the caller own current tip on this path. Only a path is accepted: the tip is unambiguous once eligibility has been checked.
    """

    path: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
