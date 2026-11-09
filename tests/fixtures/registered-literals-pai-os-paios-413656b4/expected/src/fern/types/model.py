

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model_object import ModelObject


class Model(UniversalBaseModel):
    """
    Describes an OpenAI model offering that can be used with the API.
    """

    id: str = pydantic.Field()
    """
    The model identifier, which can be referenced in the API endpoints.
    """

    created: int = pydantic.Field()
    """
    The Unix timestamp (in seconds) when the model was created.
    """

    object: ModelObject = pydantic.Field()
    """
    The object type, which is always "model".
    """

    owned_by: str = pydantic.Field()
    """
    The organization that owns the model.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
