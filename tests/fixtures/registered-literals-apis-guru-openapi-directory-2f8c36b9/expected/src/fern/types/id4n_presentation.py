

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .id4n_presentation_type import Id4NPresentationType


class Id4NPresentation(UniversalBaseModel):
    created_timestamp: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="createdTimestamp"),
        pydantic.Field(alias="createdTimestamp", description="The UTC unix timestamp of when this ID has been created"),
    ] = None
    """
    The UTC unix timestamp of when this ID has been created
    """

    holder_organization_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="holderOrganizationId"),
        pydantic.Field(alias="holderOrganizationId", description="Organization namespace of the holder of the ID"),
    ] = None
    """
    Organization namespace of the holder of the ID
    """

    id4n: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID
    """

    label: typing.Optional[str] = None
    owner_organization_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ownerOrganizationId"),
        pydantic.Field(alias="ownerOrganizationId", description="Organization namespace of the ID owner"),
    ] = None
    """
    Organization namespace of the ID owner
    """

    properties: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    The properties of the organization
    """

    type: typing.Optional[Id4NPresentationType] = pydantic.Field(default=None)
    """
    The type of ID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
