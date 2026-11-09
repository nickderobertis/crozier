

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .upload_perm_groups_perm_groups_item import UploadPermGroupsPermGroupsItem


class UploadPermGroups(UniversalBaseModel):
    """
    Groups with their respective permissions for a upload
    """

    public_perm: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="publicPerm"),
        pydantic.Field(alias="publicPerm", description="Public permission for the upload"),
    ] = None
    """
    Public permission for the upload
    """

    perm_groups: typing_extensions.Annotated[
        typing.Optional[typing.List[UploadPermGroupsPermGroupsItem]],
        FieldMetadata(alias="permGroups"),
        pydantic.Field(
            alias="permGroups", description="Indexed Object of GroupIds with their respective permissions for a upload"
        ),
    ] = None
    """
    Indexed Object of GroupIds with their respective permissions for a upload
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
