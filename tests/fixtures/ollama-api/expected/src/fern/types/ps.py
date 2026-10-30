

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Ps(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the running model
    """

    model: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the running model
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Size of the model in bytes
    """

    digest: typing.Optional[str] = pydantic.Field(default=None)
    """
    SHA256 digest of the model
    """

    details: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Model details such as format and family
    """

    expires_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    Time when the model will be unloaded
    """

    size_vram: typing.Optional[int] = pydantic.Field(default=None)
    """
    VRAM usage in bytes
    """

    context_length: typing.Optional[int] = pydantic.Field(default=None)
    """
    Context length for the running model
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
