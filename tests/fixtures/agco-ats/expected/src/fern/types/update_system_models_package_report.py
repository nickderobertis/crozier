

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .update_system_models_category import UpdateSystemModelsCategory


class UpdateSystemModelsPackageReport(UniversalBaseModel):
    categories: typing_extensions.Annotated[
        typing.Optional[typing.List[UpdateSystemModelsCategory]],
        FieldMetadata(alias="Categories"),
        pydantic.Field(alias="Categories", description="The package report's categories."),
    ] = None
    """
    The package report's categories.
    """

    package_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PackageDescription"),
        pydantic.Field(alias="PackageDescription", description="Read Only. The package description"),
    ] = None
    """
    Read Only. The package description
    """

    package_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PackageID"),
        pydantic.Field(alias="PackageID", description="The PackageID."),
    ] = None
    """
    The PackageID.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
