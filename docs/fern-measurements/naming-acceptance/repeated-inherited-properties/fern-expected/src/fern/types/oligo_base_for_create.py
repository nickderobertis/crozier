

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OligoBaseForCreate(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Name of the oligo.
    """

    folder_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="folderId"),
        pydantic.Field(alias="folderId", description="ID of the folder containing the oligo."),
    ] = None
    """
    ID of the folder containing the oligo.
    """

    bases: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
