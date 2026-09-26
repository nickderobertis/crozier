

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DocSignaturesList200ResponseSignaturesItemSeedValue(UniversalBaseModel):
    required_flags: typing_extensions.Annotated[
        int, FieldMetadata(alias="requiredFlags"), pydantic.Field(alias="requiredFlags")
    ]
    present_flags: typing_extensions.Annotated[
        int, FieldMetadata(alias="presentFlags"), pydantic.Field(alias="presentFlags")
    ]
    version: typing.Optional[int] = None
    mdp: typing.Optional[float] = None
    filter: typing.Optional[str] = None
    sub_filters: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="subFilters"), pydantic.Field(alias="subFilters")
    ]
    digest_methods: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="digestMethods"), pydantic.Field(alias="digestMethods")
    ]
    reasons: typing.List[str]
    unsupported_required: typing_extensions.Annotated[
        bool, FieldMetadata(alias="unsupportedRequired"), pydantic.Field(alias="unsupportedRequired")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
