

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class License(UniversalBaseModel):
    """
    License from the database
    """

    short_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="shortName"),
        pydantic.Field(alias="shortName", description="Short name"),
    ] = None
    """
    Short name
    """

    full_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="fullName"), pydantic.Field(alias="fullName", description="Full name")
    ] = None
    """
    Full name
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    License text
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the license text
    """

    risk: typing.Optional[int] = pydantic.Field(default=None)
    """
    Risk level
    """

    is_candidate: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isCandidate"),
        pydantic.Field(alias="isCandidate", description="Is the license a candidate?"),
    ] = None
    """
    Is the license a candidate?
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
