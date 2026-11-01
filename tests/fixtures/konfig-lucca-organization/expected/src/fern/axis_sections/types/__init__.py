



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .axis import Axis
    from .axis_section import AxisSection
    from .get_api_v3axes_response import GetApiV3AxesResponse
    from .get_api_v3axes_response_data import GetApiV3AxesResponseData
    from .get_api_v3axis_sections_axis_section_id_response import GetApiV3AxisSectionsAxisSectionIdResponse
    from .get_api_v3axissections_response import GetApiV3AxissectionsResponse
    from .get_api_v3axissections_response_data import GetApiV3AxissectionsResponseData
    from .post_api_v3axis_sections_response import PostApiV3AxisSectionsResponse
    from .put_api_v3axis_sections_axis_section_id_response import PutApiV3AxisSectionsAxisSectionIdResponse
_dynamic_imports: typing.Dict[str, str] = {
    "Axis": ".axis",
    "AxisSection": ".axis_section",
    "GetApiV3AxesResponse": ".get_api_v3axes_response",
    "GetApiV3AxesResponseData": ".get_api_v3axes_response_data",
    "GetApiV3AxisSectionsAxisSectionIdResponse": ".get_api_v3axis_sections_axis_section_id_response",
    "GetApiV3AxissectionsResponse": ".get_api_v3axissections_response",
    "GetApiV3AxissectionsResponseData": ".get_api_v3axissections_response_data",
    "PostApiV3AxisSectionsResponse": ".post_api_v3axis_sections_response",
    "PutApiV3AxisSectionsAxisSectionIdResponse": ".put_api_v3axis_sections_axis_section_id_response",
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
    "Axis",
    "AxisSection",
    "GetApiV3AxesResponse",
    "GetApiV3AxesResponseData",
    "GetApiV3AxisSectionsAxisSectionIdResponse",
    "GetApiV3AxissectionsResponse",
    "GetApiV3AxissectionsResponseData",
    "PostApiV3AxisSectionsResponse",
    "PutApiV3AxisSectionsAxisSectionIdResponse",
]
