

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpdateItemsItemsResponseItemsPagination(UniversalBaseModel):
    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    The limit specified in the request
    """

    offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    The offset specified for pagination
    """

    total: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of items in the collection
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
