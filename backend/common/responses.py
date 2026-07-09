from rest_framework.response import Response


def success_response(
    data=None,
    message="Success",
    status_code=200,
):
    return Response(
        {
            "success": True,
            "message": message,
            "data": data,
        },
        status=status_code,
    )


def list_response(
    data,
    status_code=200,
):
    return Response(
        {
            "success": True,
            "count": len(data),
            "data": data,
        },
        status=status_code,
    )


def error_response(
    message="Something went wrong.",
    errors=None,
    status_code=400,
):
    return Response(
        {
            "success": False,
            "message": message,
            "errors": errors,
        },
        status=status_code,
    )