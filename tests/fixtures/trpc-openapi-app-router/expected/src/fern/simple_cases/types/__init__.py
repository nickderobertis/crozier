



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .simple_cases_nullable_response import SimpleCasesNullableResponse
    from .simple_cases_nullable_response_result import SimpleCasesNullableResponseResult
    from .simple_cases_nullable_response_result_data import SimpleCasesNullableResponseResultData
    from .simple_cases_nullish_response import SimpleCasesNullishResponse
    from .simple_cases_nullish_response_result import SimpleCasesNullishResponseResult
    from .simple_cases_nullish_response_result_data import SimpleCasesNullishResponseResultData
    from .simple_cases_optional_response import SimpleCasesOptionalResponse
    from .simple_cases_optional_response_result import SimpleCasesOptionalResponseResult
    from .simple_cases_optional_response_result_data import SimpleCasesOptionalResponseResultData
_dynamic_imports: typing.Dict[str, str] = {
    "SimpleCasesNullableResponse": ".simple_cases_nullable_response",
    "SimpleCasesNullableResponseResult": ".simple_cases_nullable_response_result",
    "SimpleCasesNullableResponseResultData": ".simple_cases_nullable_response_result_data",
    "SimpleCasesNullishResponse": ".simple_cases_nullish_response",
    "SimpleCasesNullishResponseResult": ".simple_cases_nullish_response_result",
    "SimpleCasesNullishResponseResultData": ".simple_cases_nullish_response_result_data",
    "SimpleCasesOptionalResponse": ".simple_cases_optional_response",
    "SimpleCasesOptionalResponseResult": ".simple_cases_optional_response_result",
    "SimpleCasesOptionalResponseResultData": ".simple_cases_optional_response_result_data",
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
    "SimpleCasesNullableResponse",
    "SimpleCasesNullableResponseResult",
    "SimpleCasesNullableResponseResultData",
    "SimpleCasesNullishResponse",
    "SimpleCasesNullishResponseResult",
    "SimpleCasesNullishResponseResultData",
    "SimpleCasesOptionalResponse",
    "SimpleCasesOptionalResponseResult",
    "SimpleCasesOptionalResponseResultData",
]
