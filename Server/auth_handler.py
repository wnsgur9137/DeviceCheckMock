from datetime import timedelta, datetime
from typing import Any, Optional, Union
from dotenv import load_dotenv
from jose import JWTError, jwt
from fastapi import HTTPException, status
import time

import configs

load_dotenv()

settings = configs.Settings()

class AuthHandler:
    is_product: bool = settings.IS_PRODUCT # 앱 배포 여부
    server_uuid: str = settings.SERVER_UUID # 서버 uuid str(uuid.uuid4())를 통해 생성
    algorithm: str = settings.ALGORITHM # ES256
    apple_privacy_key = settings.APPLE_PRIVACY_KEY
    apple_team_id = settings.APPLE_TEAM_ID
    apple_key_id = settings.APPLE_KEY_ID
    
    def get_device_check_host(self) -> str:
    return 'api.devicecheck.apple.com' if self.is_product else 'api.development.devicecheck.apple.com'

    def get_transaction_id(self) -> str:
        return self.server_uuid

    def create_apple_devicecheck_jwt(self) -> str:
        header = {
            'alg': self.algorithm,
            'kid': self.apple_key_id,
            'typ': "JWT"
        }
        current_time = int(time.time())
        payload = {
            'iss': self.apple_team_id,
            'iat': current_time,
            'exp': current_time + 60 * 60,
            'aud': get_device_check_host(),
            'sub': self.apple_key_id
        }

        privacy_key = "-----BEGIN PRIVATE KEY-----\n" + self.apple_privacy_key + "\n-----END PRIVATE KEY-----"
        token = jwt.encode(payload, privacy_key, algorithm=self.algorithm, headers=header)
        return token


auth = AuthHandler()
