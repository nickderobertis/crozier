

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ApiModelsRole(UniversalBaseModel):
    """
    Defines an API Role
    """

    description: typing_extensions.Annotated[
        str, FieldMetadata(alias="Description"), pydantic.Field(alias="Description", description="Role description")
    ]
    """
    Role description
    """

    id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="Id"),
        pydantic.Field(alias="Id", description="The role's identifier."),
    ] = None
    """
    The role's identifier.
    """

    name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Name"),
        pydantic.Field(
            alias="Name", description="The name of the role. Must be alpha-numeric strings separated by a period (.)."
        ),
    ]
    """
    The name of the role. Must be alpha-numeric strings separated by a period (.).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
