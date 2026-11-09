

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DiskUsageNotes(UniversalBaseModel):
    """
    Additional notes
    """

    database: typing.Optional[str] = pydantic.Field(default=None)
    """
    Database location
    """

    repository: typing.Optional[str] = pydantic.Field(default=None)
    """
    Repository location
    """

    fossology_config: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fossologyConfig"),
        pydantic.Field(alias="fossologyConfig", description="Fossology configuration location"),
    ] = None
    """
    Fossology configuration location
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
