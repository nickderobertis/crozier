

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .thinking import Thinking


class ShowResponse(UniversalBaseModel):
    thinking: typing.Optional[Thinking] = None
    parameters: typing.Optional[str] = pydantic.Field(default=None)
    """
    Model parameter settings serialized as text
    """

    license: typing.Optional[str] = pydantic.Field(default=None)
    """
    The license of the model
    """

    modified_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    Last modified timestamp in ISO 8601 format
    """

    details: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    High-level model details
    """

    template: typing.Optional[str] = pydantic.Field(default=None)
    """
    The template used by the model to render prompts
    """

    capabilities: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of supported features
    """

    model_info: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Additional model metadata
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
