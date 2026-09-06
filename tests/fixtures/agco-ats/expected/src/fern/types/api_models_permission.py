

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_models_permission_data_required import ApiModelsPermissionDataRequired


class ApiModelsPermission(UniversalBaseModel):
    data_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="DataDescription"),
        pydantic.Field(
            alias="DataDescription", description="Description of data to be provided with Role Authorization"
        ),
    ] = None
    """
    Description of data to be provided with Role Authorization
    """

    data_required: typing_extensions.Annotated[
        ApiModelsPermissionDataRequired,
        FieldMetadata(alias="DataRequired"),
        pydantic.Field(alias="DataRequired", description="Indicates if data is required or optional"),
    ]
    """
    Indicates if data is required or optional
    """

    description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Description"), pydantic.Field(alias="Description")
    ] = None
    id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="Id"),
        pydantic.Field(alias="Id", description="The identifier of the permission."),
    ] = None
    """
    The identifier of the permission.
    """

    name: typing_extensions.Annotated[
        str, FieldMetadata(alias="Name"), pydantic.Field(alias="Name", description="The name of the permission.")
    ]
    """
    The name of the permission.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
