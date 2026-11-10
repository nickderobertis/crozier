

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_moderation_response_results_item_categories import CreateModerationResponseResultsItemCategories
from .create_moderation_response_results_item_category_scores import CreateModerationResponseResultsItemCategoryScores


class CreateModerationResponseResultsItem(UniversalBaseModel):
    flagged: bool = pydantic.Field()
    """
    Whether any of the below categories are flagged.
    """

    categories: CreateModerationResponseResultsItemCategories = pydantic.Field()
    """
    A list of the categories, and whether they are flagged or not.
    """

    category_scores: CreateModerationResponseResultsItemCategoryScores = pydantic.Field()
    """
    A list of the categories along with their scores as predicted by model.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
