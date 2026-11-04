

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .collection import Collection
from .link import Link


class Collections(UniversalBaseModel):
    links: typing.List[Link]
    collections: typing.List[Collection]
    crs: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    a list of CRS identifiers that are supported for more that one feature collection offered by the service
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
