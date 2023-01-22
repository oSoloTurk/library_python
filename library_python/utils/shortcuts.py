from typing import Any, Type, Optional


def cast_or_default(data: Any, cast_type: Type, default: Optional[Any]) -> Any:
    try:
        return cast_type(data)
    except Exception:
        return default
