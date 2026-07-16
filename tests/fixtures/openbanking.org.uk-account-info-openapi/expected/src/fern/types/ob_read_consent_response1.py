

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .links import Links
from .meta import Meta
from .ob_read_consent_response1data import ObReadConsentResponse1Data
from .ob_risk2 import ObRisk2


class ObReadConsentResponse1(UniversalBaseModel):
    data: typing_extensions.Annotated[
        ObReadConsentResponse1Data, FieldMetadata(alias="Data"), pydantic.Field(alias="Data")
    ]
    links: typing_extensions.Annotated[
        typing.Optional[Links], FieldMetadata(alias="Links"), pydantic.Field(alias="Links")
    ] = None
    meta: typing_extensions.Annotated[
        typing.Optional[Meta], FieldMetadata(alias="Meta"), pydantic.Field(alias="Meta")
    ] = None
    risk: typing_extensions.Annotated[ObRisk2, FieldMetadata(alias="Risk"), pydantic.Field(alias="Risk")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
