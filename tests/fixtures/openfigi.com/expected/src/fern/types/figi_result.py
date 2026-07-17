

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FigiResult(UniversalBaseModel):
    composite_figi: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="compositeFIGI"), pydantic.Field(alias="compositeFIGI")
    ] = None
    exch_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="exchCode"), pydantic.Field(alias="exchCode")
    ] = None
    figi: typing.Optional[str] = None
    market_sector: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="marketSector"), pydantic.Field(alias="marketSector")
    ] = None
    metadata: typing.Optional[str] = pydantic.Field(default=None)
    """
    Exists when API is unable to show non-FIGI fields.
    """

    name: typing.Optional[str] = None
    security_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="securityDescription"), pydantic.Field(alias="securityDescription")
    ] = None
    security_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="securityType"), pydantic.Field(alias="securityType")
    ] = None
    security_type2: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="securityType2"), pydantic.Field(alias="securityType2")
    ] = None
    share_class_figi: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="shareClassFIGI"), pydantic.Field(alias="shareClassFIGI")
    ] = None
    ticker: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
