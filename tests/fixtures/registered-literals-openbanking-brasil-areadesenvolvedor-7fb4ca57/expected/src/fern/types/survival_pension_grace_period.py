

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SurvivalPensionGracePeriod(UniversalBaseModel):
    """
    Prazo de carência
    """

    redemption: float = pydantic.Field()
    """
    Prazo em dias de carência para resgate Para Coletivos: Valor máximo da carência.
    """

    between_redemption_requests: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="betweenRedemptionRequests"),
        pydantic.Field(
            alias="betweenRedemptionRequests",
            description="Prazo em dias de carência entre pedidos de resgate Para Coletivos: Valor máximo da carência",
        ),
    ]
    """
    Prazo em dias de carência entre pedidos de resgate Para Coletivos: Valor máximo da carência
    """

    portability: float = pydantic.Field()
    """
    Prazo em dias de carência para portabilidade (entre empresas diferentes).
    """

    between_portability_requests: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="betweenPortabilityRequests"),
        pydantic.Field(
            alias="betweenPortabilityRequests",
            description="Prazo em dias de carência entre pedidos de portabilidade (entre empresas diferentes).",
        ),
    ]
    """
    Prazo em dias de carência entre pedidos de portabilidade (entre empresas diferentes).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
