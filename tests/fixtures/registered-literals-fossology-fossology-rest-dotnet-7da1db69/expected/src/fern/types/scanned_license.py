

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ScannedLicense(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Id of the license
    """

    shortname: typing.Optional[str] = pydantic.Field(default=None)
    """
    Short name of the license
    """

    occurrence: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of occurrences of the license
    """

    unique: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of unique occurrences of the license
    """

    spdx_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="spdxName"),
        pydantic.Field(alias="spdxName", description="SPDX name associated with the license"),
    ] = None
    """
    SPDX name associated with the license
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
