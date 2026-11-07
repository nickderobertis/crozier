

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .assertion import Assertion
from .enricher_mock import EnricherMock


class NodeTestCase(UniversalBaseModel):
    enricher_mock: typing_extensions.Annotated[
        typing.Optional[EnricherMock], FieldMetadata(alias="enricherMock"), pydantic.Field(alias="enricherMock")
    ] = None
    assertions: typing.Optional[typing.List[Assertion]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
