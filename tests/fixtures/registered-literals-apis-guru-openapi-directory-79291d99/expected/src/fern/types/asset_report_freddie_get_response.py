

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .asset_report_freddie import AssetReportFreddie
from .request_id import RequestId


class AssetReportFreddieGetResponse(UniversalBaseModel):
    """
    AssetReportFreddieGetResponse defines the response schema for `/asset_report/get`
    """

    deal: typing_extensions.Annotated[AssetReportFreddie, FieldMetadata(alias="DEAL"), pydantic.Field(alias="DEAL")]
    schema_version: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="SchemaVersion"),
        pydantic.Field(
            alias="SchemaVersion",
            description="The Verification Of Assets (aka VOA or Freddie Mac Schema) schema version.",
        ),
    ]
    """
    The Verification Of Assets (aka VOA or Freddie Mac Schema) schema version.
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
