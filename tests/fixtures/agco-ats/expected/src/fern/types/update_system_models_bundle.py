

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UpdateSystemModelsBundle(UniversalBaseModel):
    active: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Active"),
        pydantic.Field(
            alias="Active",
            description="Default Value: false. During the creation of the Bundle, this field must be false.",
        ),
    ] = None
    """
    Default Value: false. During the creation of the Bundle, this field must be false.
    """

    bundle_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="BundleID"),
        pydantic.Field(alias="BundleID", description="Read-Only."),
    ] = None
    """
    Read-Only.
    """

    bundle_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="BundleNumber"), pydantic.Field(alias="BundleNumber", description="The bundle number")
    ]
    """
    The bundle number
    """

    description: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Description"),
        pydantic.Field(alias="Description", description="The Bundle description."),
    ]
    """
    The Bundle description.
    """

    update_group_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="UpdateGroupID"),
        pydantic.Field(alias="UpdateGroupID", description="The update group this bundle belongs to."),
    ]
    """
    The update group this bundle belongs to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
