

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PostV1VectorSearchResponseDataDataItem(UniversalBaseModel):
    """
    Search results. By default, each entity object carries the `id` and `distance` fields. If `outputFields` is specified, the entity object also carries the specified fields.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the entity.
    """

    distance: typing.Optional[float] = pydantic.Field(default=None)
    """
    The similarity score of the entity to the query vector.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
