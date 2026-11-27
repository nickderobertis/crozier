

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .assembly_spec_finalized_output_location import AssemblySpecFinalizedOutputLocation


class AssemblySpecFinalized(UniversalBaseModel):
    """
    Additional information required when creating and finalizing a bulk assembly.
    """

    folder_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="folderId"),
        pydantic.Field(
            alias="folderId", description="API identifier of the folder in which the assembly should be created."
        ),
    ]
    """
    API identifier of the folder in which the assembly should be created.
    """

    name: str = pydantic.Field()
    """
    Name of the bulk assembly.
    """

    output_location: typing_extensions.Annotated[
        AssemblySpecFinalizedOutputLocation,
        FieldMetadata(alias="outputLocation"),
        pydantic.Field(alias="outputLocation"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
