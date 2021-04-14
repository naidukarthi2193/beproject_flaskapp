import json


def DataAlreadyExsist(message="Data Already Exists", **kwargs):
    """
    Method which initializes response object for delete success

    Args -

        message: message to return. (default value = Deleted successfully)
    """
    data = kwargs.get('data', dict())
    return (
        json.dumps({"message": message, "data": data}),
        409,
        {"Content-Type": "application/json"},
    )


def DeleteSucessful(message="Data Deleted Successfully", **kwargs):
    """
    Method which initializes response object for delete success

    Args -

        message: message to return. (default value = Deleted successfully)
    """
    data = kwargs.get('data', dict())
    return (
        json.dumps({"message": message, "data": data}),
        202,
        {"Content-Type": "application/json"},
    )


def OperationCorrect(message="Operation successful", **kwargs):
    """
    Method which initializes response object for Operation success

    Args -

        message: message to return. (default value = Operation successful)
    """
    data = kwargs.get('data', dict())
    return (
        json.dumps({"message": message, "data": data}),
        200,
        {"Content-Type": "application/json"}
    )


def OperationFailed(message="Operation Failed", **kwargs):
    """
    Method which initializes response object for operation failed

    Args -

        message: message to return
    """
    data = kwargs.get('data', dict())
    return (
        json.dumps({"message": message, "data": data}),
        400,
        {"Content-Type": "application/json"},
    )


def AuthenticationFailed(message="Credentials Dont Match", **kwargs):
    """
    Method which initializes response object for Authentication failed

    Args -

        message: message to return
    """
    data = kwargs.get('data', dict())
    return (
        json.dumps({"message": message, "data": data}),
        403,
        {"Content-Type": "application/json"},
    )


def NotFound(message="Not Found", **kwargs):
    """
    Method which initializes response object for not found

    Args -

        message: message to return
    """
    data = kwargs.get('data', dict())
    return (
        json.dumps({"message": message, "data": data}),
        404,
        {"Content-Type": "application/json"},
    )


def InternalServerError(message="Internal Server error", **kwargs):
    """
    Method which initializes response object for internal server error

    Args -

        message: message to return
    """
    data = kwargs.get('data', dict())
    return (
        json.dumps({"message": message, "data": data}),
        500,
        {"Content-Type": "application/json"},
    )


def DBServerError(message="Databse Server error", **kwargs):
    """
    Method which initializes response object for Database server error

    Args -

        message: message to return
    """
    data = kwargs.get('data', dict())
    return (
        json.dumps({"message": message, "data": data}),
        501,
        {"Content-Type": "application/json"},
    )


def ServiceUnavailable(message="Service unavailable", **kwargs):
    """
    Method which initializes response object for service unavailable

    Args -

        message: message to return
    """
    data = kwargs.get('data', dict())
    return (
        json.dumps({"message": message, "data": data}),
        503,
        {"Content-Type": "application/json"},
    )


def MethodNotAvailable(message="Method Not Available", **kwargs):
    """
    Method which initializes response object for operation failed

    Args -

        message: message to return
    """
    data = kwargs.get('data', dict())
    return (
        json.dumps({"message": message, "data": data}),
        405,
        {"Content-Type": "application/json"},
    )
