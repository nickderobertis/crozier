

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .global_jwt_verifier_algo_settings import GlobalJwtVerifierAlgoSettings
from .global_jwt_verifier_source import GlobalJwtVerifierSource
from .global_jwt_verifier_strategy import GlobalJwtVerifierStrategy


class GlobalJwtVerifier(UniversalBaseModel):
    """
    A JWT verifier used by multiple service descriptor
    """

    algo_settings: typing_extensions.Annotated[
        GlobalJwtVerifierAlgoSettings, FieldMetadata(alias="algoSettings"), pydantic.Field(alias="algoSettings")
    ]
    desc: str = pydantic.Field()
    """
    Verifier description
    """

    enabled: bool = pydantic.Field()
    """
    Is it enabled
    """

    id: str = pydantic.Field()
    """
    Verifier id
    """

    name: str = pydantic.Field()
    """
    Verifier name
    """

    source: GlobalJwtVerifierSource
    strategy: GlobalJwtVerifierStrategy
    strict: bool = pydantic.Field()
    """
    Does it fail if JWT not found
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
