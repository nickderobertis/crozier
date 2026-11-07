

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class RegistrationsChildrenListResponseItemLinks(UniversalBaseModel):
    """
    URLs to alternative representations of the registrations entity.
    """

    html: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the registration's page on the OSF.
    """

    self_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="self"),
        pydantic.Field(alias="self", description="A link to the canonical API endpoint of this registration."),
    ] = None
    """
    A link to the canonical API endpoint of this registration.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
