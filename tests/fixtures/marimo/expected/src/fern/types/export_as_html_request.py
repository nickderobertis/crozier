

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ExportAsHtmlRequest(UniversalBaseModel):
    asset_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="assetUrl"), pydantic.Field(alias="assetUrl")
    ] = None
    download: bool
    files: typing.List[str]
    include_code: typing_extensions.Annotated[
        bool, FieldMetadata(alias="includeCode"), pydantic.Field(alias="includeCode")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
