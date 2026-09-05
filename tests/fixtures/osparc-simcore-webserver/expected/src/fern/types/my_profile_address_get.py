

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MyProfileAddressGet(UniversalBaseModel):
    """
    Details provided upon registration and used e.g. for invoicing
    """

    institution: typing.Optional[str] = None
    address: typing.Optional[str] = None
    city: typing.Optional[str] = None
    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    State, province, canton, ...
    """

    postal_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="postalCode"), pydantic.Field(alias="postalCode")
    ] = None
    country: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
