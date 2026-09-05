

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompt_parser_nullish_type import PromptParserNullishType


class PromptParserNullish(UniversalBaseModel):
    type: PromptParserNullishType
    use_cot: bool
    choice_scores: typing.Optional[typing.Dict[str, float]] = pydantic.Field(default=None)
    """
    Map of choices to scores (0-1). Used by scorers.
    """

    choice: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of valid choices without score mapping. Used by classifiers that deposit output to tags.
    """

    allow_no_match: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, adds a 'No match' option. When selected, no tag is deposited.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
