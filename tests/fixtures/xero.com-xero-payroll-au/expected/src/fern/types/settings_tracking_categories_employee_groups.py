

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SettingsTrackingCategoriesEmployeeGroups(UniversalBaseModel):
    """
    The tracking category used for employees
    """

    tracking_category_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TrackingCategoryID"),
        pydantic.Field(alias="TrackingCategoryID", description="The identifier for the tracking category"),
    ] = None
    """
    The identifier for the tracking category
    """

    tracking_category_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TrackingCategoryName"),
        pydantic.Field(alias="TrackingCategoryName", description="Name of the tracking category"),
    ] = None
    """
    Name of the tracking category
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
