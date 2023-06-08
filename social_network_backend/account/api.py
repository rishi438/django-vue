from django.http import JsonResponse
from loguru import logger
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import SigupForm


@api_view(["GET"])
def me(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    return JsonResponse(
        {
            "id": request.user.id,
            "name": request.user.name,
            "email": request.user.email,
        }
    )


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def signup(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    data = request.data
    message = "success"
    logger.debug(data)
    form = SigupForm(
        {
            "email": data.get("email"),
            "name": data.get("name"),
            "password1": data.get("password1"),
            "password2": data.get("password2"),
        }
    )
    logger.debug(form.errors)
    if form.is_valid():
        form.save()
        # send verfication email later!
    else:
        message = "Error: Invalid Form please contact Tech Team"
    return JsonResponse({"status": message})
