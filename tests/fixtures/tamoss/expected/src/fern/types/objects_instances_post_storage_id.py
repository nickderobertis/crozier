

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .uuid_ import Uuid


class ObjectsInstancesPostStorageId(UniversalBaseModel):
    """
    Request the duplication of a Media Object instance to a new Storage Backend, via it's `storage_id`.
    """

    storage_id: Uuid = pydantic.Field()
    """
    Storage backend identifier
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
