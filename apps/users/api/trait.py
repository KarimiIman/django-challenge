
from rest_framework_jwt.settings import api_settings

class jWTMixin:
    def getToken(self, user):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        return jwt_encode_handler(payload)