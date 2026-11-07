

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .player_family import PlayerFamily
from .post_api_v1player_releases_upload_response_data_channel import PostApiV1PlayerReleasesUploadResponseDataChannel
from .post_api_v1player_releases_upload_response_data_platform import PostApiV1PlayerReleasesUploadResponseDataPlatform
from .post_api_v1player_releases_upload_response_data_source import PostApiV1PlayerReleasesUploadResponseDataSource


class PostApiV1PlayerReleasesUploadResponseData(UniversalBaseModel):
    id: typing.Optional[str] = None
    platform: typing.Optional[PostApiV1PlayerReleasesUploadResponseDataPlatform] = None
    player_family: typing_extensions.Annotated[
        typing.Optional[PlayerFamily], FieldMetadata(alias="playerFamily"), pydantic.Field(alias="playerFamily")
    ] = None
    architecture: typing.Optional[str] = pydantic.Field(default=None)
    """
    `x86_64` or `aarch64` for Tilecast Edge; empty for the other families.
    """

    source: typing.Optional[PostApiV1PlayerReleasesUploadResponseDataSource] = None
    version_code: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="versionCode"), pydantic.Field(alias="versionCode")
    ] = None
    version_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="versionName"), pydantic.Field(alias="versionName")
    ] = None
    channel: typing.Optional[PostApiV1PlayerReleasesUploadResponseDataChannel] = None
    apk_size_bytes: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="apkSizeBytes"),
        pydantic.Field(alias="apkSizeBytes", description="The artifact size"),
    ] = None
    """
    The artifact size
    """

    duplicate: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
