

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_moderation_response_results_item import CreateModerationResponseResultsItem


class CreateModerationResponse(UniversalBaseModel):
    """
    Represents if a given text input is potentially harmful.
    """

    id: str = pydantic.Field()
    """
    The unique identifier for the moderation request.
    """

    model: str = pydantic.Field()
    """
    The model used to generate the moderation results.
    """

    results: typing.List[CreateModerationResponseResultsItem] = pydantic.Field()
    """
    A list of moderation objects.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
