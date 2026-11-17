

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Institution(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The institution's unique identifier
    """

    name: str
    description: str
    location: str
    website: str
    email: typing.Optional[str] = None
    phone: typing.Optional[str] = None
    web_contact: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="webContact"), pydantic.Field(alias="webContact")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
