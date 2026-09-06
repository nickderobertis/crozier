

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ereader_device_object_availability_option import EreaderDeviceObjectAvailabilityOption
from .ereader_name import EreaderName


class EreaderDeviceObject(UniversalBaseModel):
    """
    An e-reader device configured to receive EPUB through e-mail.
    """

    name: EreaderName
    email: str = pydantic.Field()
    """
    The email address associated with the e-reader device.
    """

    availability_option: typing_extensions.Annotated[
        EreaderDeviceObjectAvailabilityOption,
        FieldMetadata(alias="availabilityOption"),
        pydantic.Field(alias="availabilityOption", description="The availability option for the device."),
    ]
    """
    The availability option for the device.
    """

    users: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of specific users allowed to access the device.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
