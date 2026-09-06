

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .agco_power_services_models_ecu_state import AgcoPowerServicesModelsEcuState


class AgcoPowerServicesModelsEcu(UniversalBaseModel):
    """
    An AGCO Power ECU
    """

    activation_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ActivationCode"),
        pydantic.Field(
            alias="ActivationCode",
            description="The code used to activate the ECU. May not be modified. Returned only on activation.",
        ),
    ] = None
    """
    The code used to activate the ECU. May not be modified. Returned only on activation.
    """

    damaged_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="DamagedDescription"),
        pydantic.Field(alias="DamagedDescription", description="A description why the ECU cannot be deactivated."),
    ] = None
    """
    A description why the ECU cannot be deactivated.
    """

    engine_serial_number: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="EngineSerialNumber"),
        pydantic.Field(alias="EngineSerialNumber", description="The serial number of the ECU’s engine"),
    ]
    """
    The serial number of the ECU’s engine
    """

    replaces_ecu_serial_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ReplacesECUSerialNumber"),
        pydantic.Field(
            alias="ReplacesECUSerialNumber",
            description="The serial number of the ECU that this ECU replaces. Required if activating an ECU..",
        ),
    ] = None
    """
    The serial number of the ECU that this ECU replaces. Required if activating an ECU..
    """

    serial_number: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="SerialNumber"),
        pydantic.Field(alias="SerialNumber", description="The serial number of the ECU"),
    ]
    """
    The serial number of the ECU
    """

    state: typing_extensions.Annotated[
        AgcoPowerServicesModelsEcuState,
        FieldMetadata(alias="State"),
        pydantic.Field(alias="State", description="The state of the ECU"),
    ]
    """
    The state of the ECU
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
