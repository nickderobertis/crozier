

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OtoroshiModelsTeamAccess(UniversalBaseModel):
    """
    Access rights for teams
    """

    can_read: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="canRead"),
        pydantic.Field(alias="canRead", description="Can this access right read data"),
    ] = None
    """
    Can this access right read data
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    Access pattern
    """

    can_write: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="canWrite"),
        pydantic.Field(alias="canWrite", description="Can this access right write data"),
    ] = None
    """
    Can this access right write data
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
