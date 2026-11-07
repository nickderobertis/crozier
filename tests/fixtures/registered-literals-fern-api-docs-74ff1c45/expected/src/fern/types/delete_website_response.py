

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeleteWebsiteResponse(UniversalBaseModel):
    success: bool = pydantic.Field()
    """
    Whether the website was successfully deleted
    """

    pages_deleted: int = pydantic.Field()
    """
    Number of pages deleted
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
