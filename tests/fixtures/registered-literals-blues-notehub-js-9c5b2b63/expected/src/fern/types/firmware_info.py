

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FirmwareInfo(UniversalBaseModel):
    built: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date the firmware was built.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date the firmware was created.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of the firmware.
    """

    filename: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the firmware file.
    """

    info: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    User-defined metadata
    """

    md5: typing.Optional[str] = pydantic.Field(default=None)
    """
    The MD5 hash of the firmware file.
    """

    notes: typing.Optional[str] = pydantic.Field(default=None)
    """
    User-defined notes
    """

    organization: typing.Optional[str] = pydantic.Field(default=None)
    """
    The organization that owns the firmware.
    """

    product: typing.Optional[str] = pydantic.Field(default=None)
    """
    The product that the firmware is for.
    """

    published: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True if the firmware is published.
    """

    tags: typing.Optional[str] = pydantic.Field(default=None)
    """
    A list of tags associated with the firmware.
    """

    target: typing.Optional[str] = pydantic.Field(default=None)
    """
    The target device for the firmware.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of firmware.
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version of the firmware.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
