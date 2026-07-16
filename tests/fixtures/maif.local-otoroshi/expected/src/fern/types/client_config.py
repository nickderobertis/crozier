

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ClientConfig(UniversalBaseModel):
    """
    The configuration of the circuit breaker for a service descriptor
    """

    backoff_factor: typing_extensions.Annotated[int, FieldMetadata(alias="backoffFactor")] = pydantic.Field()
    """
    Specify the factor to multiply the delay for each retry
    """

    call_timeout: typing_extensions.Annotated[int, FieldMetadata(alias="callTimeout")] = pydantic.Field()
    """
    Specify how long each call should last at most in milliseconds
    """

    global_timeout: typing_extensions.Annotated[int, FieldMetadata(alias="globalTimeout")] = pydantic.Field()
    """
    Specify how long the global call (with retries) should last at most in milliseconds
    """

    max_errors: typing_extensions.Annotated[int, FieldMetadata(alias="maxErrors")] = pydantic.Field()
    """
    Specify how many errors can pass before opening the circuit breaker
    """

    retries: int = pydantic.Field()
    """
    Specify how many times the client will try to fetch the result of the request after an error before giving up.
    """

    retry_initial_delay: typing_extensions.Annotated[int, FieldMetadata(alias="retryInitialDelay")] = pydantic.Field()
    """
    Specify the delay between two retries. Each retry, the delay is multiplied by the backoff factor
    """

    sample_interval: typing_extensions.Annotated[int, FieldMetadata(alias="sampleInterval")] = pydantic.Field()
    """
    Specify the sliding window time for the circuit breaker in milliseconds, after this time, error count will be reseted
    """

    use_circuit_breaker: typing_extensions.Annotated[bool, FieldMetadata(alias="useCircuitBreaker")] = pydantic.Field()
    """
    Use a circuit breaker to avoid cascading failure when calling chains of services. Highly recommended !
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
