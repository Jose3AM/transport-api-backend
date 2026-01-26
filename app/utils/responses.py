from typing import Any, Optional

def success_response(
    data: Any,
    *,
    total: Optional[int] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None
):
    response = {
        "status": "success",
        "data": data
    }

    if total is not None:
        response["total"] = total
    if limit is not None:
        response["limit"] = limit
    if offset is not None:
        response["offset"] = offset

    return response