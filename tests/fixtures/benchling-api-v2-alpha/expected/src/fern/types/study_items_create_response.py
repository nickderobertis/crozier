

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .study_item import StudyItem


class StudyItemsCreateResponse(UniversalBaseModel):
    items: typing.Optional[typing.List[StudyItem]] = pydantic.Field(default=None)
    """
    The created study items
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
