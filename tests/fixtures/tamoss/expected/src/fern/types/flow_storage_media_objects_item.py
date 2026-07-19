

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .http_request import HttpRequest


class FlowStorageMediaObjectsItem(UniversalBaseModel):
    """
    Information for a Media Object
    """

    object_id: str = pydantic.Field()
    """
    The object store identifier for the Media Object.
    """

    put_url: HttpRequest

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
