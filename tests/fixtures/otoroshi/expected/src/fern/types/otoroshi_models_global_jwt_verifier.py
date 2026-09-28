

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_models_algo_settings import OtoroshiModelsAlgoSettings
from .otoroshi_models_global_jwt_verifier_type import OtoroshiModelsGlobalJwtVerifierType


class OtoroshiModelsGlobalJwtVerifier(UniversalBaseModel):
    """
    Otoroshi model for JWT token verifier
    """

    type: typing.Optional[OtoroshiModelsGlobalJwtVerifierType] = pydantic.Field(default=None)
    """
    the kind of verifier
    """

    desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    Verifier description
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Verifier name
    """

    strict: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Does it fail if JWT not found
    """

    source: typing.Optional[typing.Any] = None
    algo_settings: typing_extensions.Annotated[
        typing.Optional[OtoroshiModelsAlgoSettings],
        FieldMetadata(alias="algoSettings"),
        pydantic.Field(alias="algoSettings", description="Algo settings of the verifier"),
    ] = None
    """
    Algo settings of the verifier
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Entity tags
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Verifier id
    """

    loc: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="_loc"), pydantic.Field(alias="_loc")
    ] = None
    strategy: typing.Optional[typing.Any] = None
    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Entity metadata
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
