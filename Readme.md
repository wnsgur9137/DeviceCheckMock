# Apple Device Check API

서버는 FastAPI 이용

## 생성

1. iOS에서 DeviceToken을 조회하여 서버로 전송
2. 서버에서는 DeviceToken을 이용해 jwt 토큰을 생성하고, bit0, bit1의 초기값을 Apple 서버로 전송



## 조회

1. iOS에서 DeviceToken을 이용한 조회 API 사용
2. 서버에서 DeviceToken을 이용해 jwt 토큰을 생성하고 이를 Apple 서버에 요청하여 조회
3. 조회한 값을 iOS로 response 반환
4. iOS에서 response를 이용해 적절한 대응

## 업데이트

1. 서버 혹은 API를 이용해 관리자가 업데이트
2. 서버에서 DeviceToken을 이용하여 Apple 서버로 bit0, bit1의 값을 업데이트 
