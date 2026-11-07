

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Organization(UniversalBaseModel):
    """
    An organization
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the organization ( Deprecated: Use namespace instead. )
    """

    logo_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="logoURL"),
        pydantic.Field(alias="logoURL", description="URL to a logo of the organization"),
    ] = None
    """
    URL to a logo of the organization
    """

    name: str = pydantic.Field()
    """
    The name of the organization
    """

    namespace: str = pydantic.Field()
    """
    The namespace of the organization
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
