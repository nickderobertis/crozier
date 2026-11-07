

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetReuseReportSummary(UniversalBaseModel):
    """
    Information required by Reuse Report Summary for an upload
    """

    decleared_license: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="declearedLicense"),
        pydantic.Field(alias="declearedLicense", description="Decleared license"),
    ] = None
    """
    Decleared license
    """

    cleared_license: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="clearedLicense"),
        pydantic.Field(alias="clearedLicense", description="Cleared license"),
    ] = None
    """
    Cleared license
    """

    unused_license: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="unusedLicense"),
        pydantic.Field(alias="unusedLicense", description="Unused license"),
    ] = None
    """
    Unused license
    """

    missing_license: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="missingLicense"),
        pydantic.Field(alias="missingLicense", description="Missing license"),
    ] = None
    """
    Missing license
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
