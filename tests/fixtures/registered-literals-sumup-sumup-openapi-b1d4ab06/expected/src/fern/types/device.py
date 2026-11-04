

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Device(UniversalBaseModel):
    """
    Details of the device used to create the transaction.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device name.
    """

    system_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device OS.
    """

    model: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device model.
    """

    system_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device OS version.
    """

    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid", description="Device UUID.")
    ] = None
    """
    Device UUID.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
