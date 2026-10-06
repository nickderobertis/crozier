

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetUnhealthyAssetsGetResponse(UniversalBaseModel):
    display_result: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayResult"),
        pydantic.Field(
            alias="displayResult",
            description="The list of unhealthy assets with description and asset number in html format",
        ),
    ] = None
    """
    The list of unhealthy assets with description and asset number in html format
    """

    json_result: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="jsonResult"),
        pydantic.Field(alias="jsonResult", description="The list of unhealthy assets in json format"),
    ] = None
    """
    The list of unhealthy assets in json format
    """

    json_result_asset_string: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="jsonResultAssetString"),
        pydantic.Field(alias="jsonResultAssetString", description="Asset number space delimited in a String"),
    ] = None
    """
    Asset number space delimited in a String
    """

    json_result_asset_uid_string: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="jsonResultAssetUIDString"),
        pydantic.Field(alias="jsonResultAssetUIDString", description="Asset UID space delimited in a String"),
    ] = None
    """
    Asset UID space delimited in a String
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
