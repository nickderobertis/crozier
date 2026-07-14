

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .stream_transform import StreamTransform


class CatalogDiff(UniversalBaseModel):
    """
    Describes the difference between two Airbyte catalogs.
    """

    transforms: typing.List[StreamTransform] = pydantic.Field()
    """
    list of stream transformations. order does not matter.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
