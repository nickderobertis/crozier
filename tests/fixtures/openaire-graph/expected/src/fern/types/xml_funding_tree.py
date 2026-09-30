

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .xml_funder import XmlFunder
from .xml_funding_level import XmlFundingLevel


class XmlFundingTree(UniversalBaseModel):
    funder: typing.Optional[XmlFunder] = None
    funding_level0: typing_extensions.Annotated[
        typing.Optional[XmlFundingLevel], FieldMetadata(alias="fundingLevel0"), pydantic.Field(alias="fundingLevel0")
    ] = None
    funding_level1: typing_extensions.Annotated[
        typing.Optional[XmlFundingLevel], FieldMetadata(alias="fundingLevel1"), pydantic.Field(alias="fundingLevel1")
    ] = None
    funding_level2: typing_extensions.Annotated[
        typing.Optional[XmlFundingLevel], FieldMetadata(alias="fundingLevel2"), pydantic.Field(alias="fundingLevel2")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
