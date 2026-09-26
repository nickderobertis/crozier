

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .column_list_uuid import ColumnListUuid
from .column_ratio import ColumnRatio
from .column_uuid import ColumnUuid
from .is_hidden import IsHidden
from .is_required import IsRequired
from .name import Name


class WalletConnectPayload(UniversalBaseModel):
    """
    Payload for WALLET_CONNECT block type. Used for Web3 wallet connection.
    """

    is_hidden: typing_extensions.Annotated[
        typing.Optional[IsHidden], FieldMetadata(alias="isHidden"), pydantic.Field(alias="isHidden")
    ] = None
    is_required: typing_extensions.Annotated[
        typing.Optional[IsRequired], FieldMetadata(alias="isRequired"), pydantic.Field(alias="isRequired")
    ] = None
    column_list_uuid: typing_extensions.Annotated[
        typing.Optional[ColumnListUuid], FieldMetadata(alias="columnListUuid"), pydantic.Field(alias="columnListUuid")
    ] = None
    column_uuid: typing_extensions.Annotated[
        typing.Optional[ColumnUuid], FieldMetadata(alias="columnUuid"), pydantic.Field(alias="columnUuid")
    ] = None
    column_ratio: typing_extensions.Annotated[
        typing.Optional[ColumnRatio], FieldMetadata(alias="columnRatio"), pydantic.Field(alias="columnRatio")
    ] = None
    name: typing.Optional[Name] = None
    has_email_login: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasEmailLogin"),
        pydantic.Field(
            alias="hasEmailLogin",
            description="When true, allows respondents to connect using email-based wallet login.",
        ),
    ] = None
    """
    When true, allows respondents to connect using email-based wallet login.
    """

    has_social_login: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasSocialLogin"),
        pydantic.Field(
            alias="hasSocialLogin", description="When true, allows respondents to connect using social login providers."
        ),
    ] = None
    """
    When true, allows respondents to connect using social login providers.
    """

    use_caip_format: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="useCaipFormat"),
        pydantic.Field(
            alias="useCaipFormat",
            description="When true, returns the wallet address in CAIP-10 format (e.g., 'eip155:1:0x...'). When false, returns the simple address format.",
        ),
    ] = None
    """
    When true, returns the wallet address in CAIP-10 format (e.g., 'eip155:1:0x...'). When false, returns the simple address format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
