



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .channel import Channel
    from .channel_one import ChannelOne
    from .channels import Channels
    from .channels_one import ChannelsOne
    from .gap import Gap
    from .lull import Lull
    from .pitch import Pitch
    from .reading import Reading
    from .reading_alarm import ReadingAlarm
    from .reading_mode import ReadingMode
    from .silence import Silence
    from .stillness import Stillness
    from .tone import Tone
_dynamic_imports: typing.Dict[str, str] = {
    "Channel": ".channel",
    "ChannelOne": ".channel_one",
    "Channels": ".channels",
    "ChannelsOne": ".channels_one",
    "Gap": ".gap",
    "Lull": ".lull",
    "Pitch": ".pitch",
    "Reading": ".reading",
    "ReadingAlarm": ".reading_alarm",
    "ReadingMode": ".reading_mode",
    "Silence": ".silence",
    "Stillness": ".stillness",
    "Tone": ".tone",
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
    "Channel",
    "ChannelOne",
    "Channels",
    "ChannelsOne",
    "Gap",
    "Lull",
    "Pitch",
    "Reading",
    "ReadingAlarm",
    "ReadingMode",
    "Silence",
    "Stillness",
    "Tone",
]
