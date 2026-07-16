



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .abstract_exchange import AbstractExchange
    from .abstract_exchange_type import AbstractExchangeType
    from .binding import Binding
    from .binding_type import BindingType
    from .counter import Counter
    from .counter_map import CounterMap
    from .daily_invocation_statistic import DailyInvocationStatistic
    from .event_message import EventMessage
    from .exchange import Exchange, Exchange_ReqRespPair, Exchange_UnidirEvent
    from .features_config import FeaturesConfig
    from .features_config_async_api import FeaturesConfigAsyncApi
    from .features_config_microcks_hub import FeaturesConfigMicrocksHub
    from .features_config_repository_filter import FeaturesConfigRepositoryFilter
    from .features_config_repository_tenancy import FeaturesConfigRepositoryTenancy
    from .header import Header
    from .header_dto import HeaderDto
    from .import_job import ImportJob
    from .keycloak_config import KeycloakConfig
    from .keycloak_config_ssl_required import KeycloakConfigSslRequired
    from .labels_map import LabelsMap
    from .message_array import MessageArray
    from .metadata import Metadata
    from .oauth_scope import OauthScope
    from .operation import Operation
    from .operation_headers import OperationHeaders
    from .parameter_constraint import ParameterConstraint
    from .parameter_constraint_in import ParameterConstraintIn
    from .request import Request
    from .request_response_pair import RequestResponsePair
    from .resource import Resource
    from .resource_type import ResourceType
    from .response import Response
    from .secret import Secret
    from .secret_ref import SecretRef
    from .service import Service
    from .service_ref import ServiceRef
    from .service_type import ServiceType
    from .service_view import ServiceView
    from .string_array import StringArray
    from .test_case_result import TestCaseResult
    from .test_conformance_metric import TestConformanceMetric
    from .test_result import TestResult
    from .test_result_summary import TestResultSummary
    from .test_return import TestReturn
    from .test_runner_type import TestRunnerType
    from .test_step_result import TestStepResult
    from .trend import Trend
    from .unidirectional_event import UnidirectionalEvent
    from .weighted_metric_value import WeightedMetricValue
_dynamic_imports: typing.Dict[str, str] = {
    "AbstractExchange": ".abstract_exchange",
    "AbstractExchangeType": ".abstract_exchange_type",
    "Binding": ".binding",
    "BindingType": ".binding_type",
    "Counter": ".counter",
    "CounterMap": ".counter_map",
    "DailyInvocationStatistic": ".daily_invocation_statistic",
    "EventMessage": ".event_message",
    "Exchange": ".exchange",
    "Exchange_ReqRespPair": ".exchange",
    "Exchange_UnidirEvent": ".exchange",
    "FeaturesConfig": ".features_config",
    "FeaturesConfigAsyncApi": ".features_config_async_api",
    "FeaturesConfigMicrocksHub": ".features_config_microcks_hub",
    "FeaturesConfigRepositoryFilter": ".features_config_repository_filter",
    "FeaturesConfigRepositoryTenancy": ".features_config_repository_tenancy",
    "Header": ".header",
    "HeaderDto": ".header_dto",
    "ImportJob": ".import_job",
    "KeycloakConfig": ".keycloak_config",
    "KeycloakConfigSslRequired": ".keycloak_config_ssl_required",
    "LabelsMap": ".labels_map",
    "MessageArray": ".message_array",
    "Metadata": ".metadata",
    "OauthScope": ".oauth_scope",
    "Operation": ".operation",
    "OperationHeaders": ".operation_headers",
    "ParameterConstraint": ".parameter_constraint",
    "ParameterConstraintIn": ".parameter_constraint_in",
    "Request": ".request",
    "RequestResponsePair": ".request_response_pair",
    "Resource": ".resource",
    "ResourceType": ".resource_type",
    "Response": ".response",
    "Secret": ".secret",
    "SecretRef": ".secret_ref",
    "Service": ".service",
    "ServiceRef": ".service_ref",
    "ServiceType": ".service_type",
    "ServiceView": ".service_view",
    "StringArray": ".string_array",
    "TestCaseResult": ".test_case_result",
    "TestConformanceMetric": ".test_conformance_metric",
    "TestResult": ".test_result",
    "TestResultSummary": ".test_result_summary",
    "TestReturn": ".test_return",
    "TestRunnerType": ".test_runner_type",
    "TestStepResult": ".test_step_result",
    "Trend": ".trend",
    "UnidirectionalEvent": ".unidirectional_event",
    "WeightedMetricValue": ".weighted_metric_value",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "AbstractExchange",
    "AbstractExchangeType",
    "Binding",
    "BindingType",
    "Counter",
    "CounterMap",
    "DailyInvocationStatistic",
    "EventMessage",
    "Exchange",
    "Exchange_ReqRespPair",
    "Exchange_UnidirEvent",
    "FeaturesConfig",
    "FeaturesConfigAsyncApi",
    "FeaturesConfigMicrocksHub",
    "FeaturesConfigRepositoryFilter",
    "FeaturesConfigRepositoryTenancy",
    "Header",
    "HeaderDto",
    "ImportJob",
    "KeycloakConfig",
    "KeycloakConfigSslRequired",
    "LabelsMap",
    "MessageArray",
    "Metadata",
    "OauthScope",
    "Operation",
    "OperationHeaders",
    "ParameterConstraint",
    "ParameterConstraintIn",
    "Request",
    "RequestResponsePair",
    "Resource",
    "ResourceType",
    "Response",
    "Secret",
    "SecretRef",
    "Service",
    "ServiceRef",
    "ServiceType",
    "ServiceView",
    "StringArray",
    "TestCaseResult",
    "TestConformanceMetric",
    "TestResult",
    "TestResultSummary",
    "TestReturn",
    "TestRunnerType",
    "TestStepResult",
    "Trend",
    "UnidirectionalEvent",
    "WeightedMetricValue",
]
