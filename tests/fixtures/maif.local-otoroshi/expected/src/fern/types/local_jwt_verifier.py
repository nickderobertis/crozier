

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .local_jwt_verifier_algo_settings import LocalJwtVerifierAlgoSettings
from .local_jwt_verifier_source import LocalJwtVerifierSource
from .local_jwt_verifier_strategy import LocalJwtVerifierStrategy


class LocalJwtVerifier(UniversalBaseModel):
    """
    A JWT verifier used only for the current service descriptor
    """

    algo_settings: typing_extensions.Annotated[LocalJwtVerifierAlgoSettings, FieldMetadata(alias="algoSettings")]
    enabled: bool = pydantic.Field()
    """
    Is it enabled
    """

    source: LocalJwtVerifierSource
    strategy: LocalJwtVerifierStrategy
    strict: bool = pydantic.Field()
    """
    Does it fail if JWT not found
    """

    type: str = pydantic.Field()
    """
    A string with value 'local'
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
