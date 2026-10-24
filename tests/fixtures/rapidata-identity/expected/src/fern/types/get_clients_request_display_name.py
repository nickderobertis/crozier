

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetClientsRequestDisplayName(UniversalBaseModel):
    eq: typing.Optional[str] = None
    neq: typing.Optional[str] = None
    gt: typing.Optional[str] = None
    gte: typing.Optional[str] = None
    lt: typing.Optional[str] = None
    lte: typing.Optional[str] = None
    contains: typing.Optional[str] = None
    starts_with: typing.Optional[str] = None
    ends_with: typing.Optional[str] = None
    in_: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="in"), pydantic.Field(alias="in")
    ] = None
    not_contains: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
