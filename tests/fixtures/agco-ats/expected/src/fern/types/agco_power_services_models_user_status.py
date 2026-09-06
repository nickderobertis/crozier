

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .agco_power_services_models_user_status_state import AgcoPowerServicesModelsUserStatusState


class AgcoPowerServicesModelsUserStatus(UniversalBaseModel):
    """
    Status of a voucher in the AGCO Power system
    """

    dealer_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="DealerCode"),
        pydantic.Field(alias="DealerCode", description="The dealer code of the voucher"),
    ]
    """
    The dealer code of the voucher
    """

    state: typing_extensions.Annotated[
        typing.Optional[AgcoPowerServicesModelsUserStatusState],
        FieldMetadata(alias="State"),
        pydantic.Field(alias="State", description="The state of the voucher"),
    ] = None
    """
    The state of the voucher
    """

    voucher_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="VoucherCode"), pydantic.Field(alias="VoucherCode", description="The voucher code")
    ]
    """
    The voucher code
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
