

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ereader_device_object import EreaderDeviceObject


class EmailSettings(UniversalBaseModel):
    """
    The email settings configuration for the server. This includes the credentials to send e-books and an array of e-reader devices.
    """

    id: str = pydantic.Field()
    """
    The unique identifier for the email settings. Currently this is always `email-settings`
    """

    host: typing.Optional[str] = pydantic.Field(default=None)
    """
    The SMTP host address.
    """

    port: int = pydantic.Field()
    """
    The port number for the SMTP server.
    """

    secure: bool = pydantic.Field()
    """
    Indicates if the connection should use SSL/TLS.
    """

    reject_unauthorized: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="rejectUnauthorized"),
        pydantic.Field(
            alias="rejectUnauthorized", description="Indicates if unauthorized SSL/TLS certificates should be rejected."
        ),
    ] = None
    """
    Indicates if unauthorized SSL/TLS certificates should be rejected.
    """

    user: typing.Optional[str] = pydantic.Field(default=None)
    """
    The username for SMTP authentication.
    """

    pass_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pass"),
        pydantic.Field(alias="pass", description="The password for SMTP authentication."),
    ] = None
    """
    The password for SMTP authentication.
    """

    test_address: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="testAddress"),
        pydantic.Field(alias="testAddress", description="The test email address used for sending test emails."),
    ] = None
    """
    The test email address used for sending test emails.
    """

    from_address: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fromAddress"),
        pydantic.Field(alias="fromAddress", description='The default "from" email address for outgoing emails.'),
    ] = None
    """
    The default "from" email address for outgoing emails.
    """

    ereader_devices: typing_extensions.Annotated[
        typing.List[EreaderDeviceObject],
        FieldMetadata(alias="ereaderDevices"),
        pydantic.Field(alias="ereaderDevices", description="List of configured e-reader devices."),
    ]
    """
    List of configured e-reader devices.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
