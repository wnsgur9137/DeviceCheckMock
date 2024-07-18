from fastapi import FastAPI
import uvicorn

import auth_handler

# Device의 bit값들을 조회하는 API
@app.post("/user/checkDevice", tags=["User"])
async def post_user_check_device(deviceToken: str):
    jwt_token = auth_handler.create_apple_devicecheck_jwt() # JWT Token 생성
    transaction_id = auth_handler.get_transaction_id() # Server UUID
    device_check_host = auth_handler.get_device_check_host() # Apple device check host

    headers = {
        'Authorization': f'Bearer {jwt_token}',
        'Content-Type': 'application/json'
    }
    post_data = {
        'device_token': deviceToken, # iOS Device Token
        'transaction_id': transaction_id, # Server UUID
        'timestamp': int(time.time()) * 1000 # milliseconds
    }

    url = f"https://{device_check_host}/v1/query_two_bits"
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=post_data, headers=headers)

    try:
        json_response = response.json()
        return JSONResponse(status_code=response.status_code, content={
            "status": response.status_code,
            "bit0": json_response.get('bit0'), # bit0
            "bit1": json_response.get('bit1'), # bit1
            "lastUpdated": json_response.get('last_update_time')
        })
    except json.JSONDecodeError:
        print("ERROR Check Device Decode")
        return JSONResponse(status_code=response.status_code)

# Device의 bit값들을 저장하는 API (App에서는 사용하지 않음)
@app.post("/user/updateDevice/", tags=["User"])
async def post_user_update_device(deviceToken: str, bit0: bool, bit1: bool):
    jwt_token = auth_handler.create_apple_devicecheck_jwt()
    transaction_id = auth_handler.get_transaction_id()
    device_check_host = auth_handler.get_device_check_host()
    headers = {
        'Authorization': f'Bearer {jwt_token}',
        'Content-Type': 'application/json'
    }
    post_data = {
        'device_token': deviceToken, # iOS Device Token
        'transaction_id': transaction_id, # Server UUID
        'timestamp': int(time.time()) * 1000, # milliseconds
        'bit0': bit0, # bit0
        'bit1': bit1 # bit1
    }

    url = f"https://{device_check_host}/v1/update_two_bits"
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=post_data, headers=headers)

    return JSONResponse(status_code=response.status_code, content={"status": response.status_code})

if __name__ == "__main__":
    uvicorn.run("main:app")
