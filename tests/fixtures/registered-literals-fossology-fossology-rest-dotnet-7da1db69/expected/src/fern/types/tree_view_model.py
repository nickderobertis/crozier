

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tree_view_model_clearing_progress import TreeViewModelClearingProgress
from .tree_view_model_clearing_status import TreeViewModelClearingStatus
from .tree_view_model_edited_license_list_item import TreeViewModelEditedLicenseListItem
from .tree_view_model_file_details import TreeViewModelFileDetails
from .tree_view_model_license_list_item import TreeViewModelLicenseListItem


class TreeViewModel(UniversalBaseModel):
    file_details: typing_extensions.Annotated[
        typing.Optional[TreeViewModelFileDetails],
        FieldMetadata(alias="fileDetails"),
        pydantic.Field(alias="fileDetails", description="Details about the file."),
    ] = None
    """
    Details about the file.
    """

    license_list: typing_extensions.Annotated[
        typing.Optional[typing.List[TreeViewModelLicenseListItem]],
        FieldMetadata(alias="licenseList"),
        pydantic.Field(alias="licenseList", description="List of licenses."),
    ] = None
    """
    List of licenses.
    """

    edited_license_list: typing_extensions.Annotated[
        typing.Optional[typing.List[TreeViewModelEditedLicenseListItem]],
        FieldMetadata(alias="editedLicenseList"),
        pydantic.Field(alias="editedLicenseList", description="List of edited licenses."),
    ] = None
    """
    List of edited licenses.
    """

    clearing_status: typing_extensions.Annotated[
        typing.Optional[TreeViewModelClearingStatus],
        FieldMetadata(alias="clearingStatus"),
        pydantic.Field(alias="clearingStatus", description="The clearing status."),
    ] = None
    """
    The clearing status.
    """

    clearing_progress: typing_extensions.Annotated[
        typing.Optional[TreeViewModelClearingProgress],
        FieldMetadata(alias="clearingProgress"),
        pydantic.Field(alias="clearingProgress", description="The progress of clearing."),
    ] = None
    """
    The progress of clearing.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
