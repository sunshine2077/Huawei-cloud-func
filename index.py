# -*- coding:utf-8 -*-
import json
import requests
import base64

# Root
def handler(event, context):
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": json.dumps(chatgpt_api(event))
    }
# MESSAGE STATUS:
MSG_SUCCESS=0
MSG_FAILED=1
MSG_UNVALID_PARAM=2


# implement:
def chatgpt_api(request_dict: dict):
    try:
        # step1. get request headers and body
        if "headers" not in request_dict:
            return {
                "code": MSG_UNVALID_PARAM,
                "msg": "The request header not found",
                "data": None
            }
        if "body" not in request_dict:
            return {
                "code": MSG_UNVALID_PARAM,
                "msg": "The request body not found",
                "data": None
            }
        request_header=request_dict["headers"]
        request_body=json.loads(base64.b64decode(request_dict["body"]))
        # step2. build OPENAI request params 
        openai_method=request_header["x-openai-method"]
        openai_url=request_header["x-openai-url"]
        openai_headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {request_header['x-openai-key']}"
        }
        openai_body=request_body
        # step3. send request to OPENAI
        if openai_method=="get":
            response = requests.get(openai_url, headers=openai_headers)
        else:
            response = requests.post(openai_url, headers=openai_headers, data=openai_body)
        # step4. get result of the request
        if response.ok:
            return {
                "code": MSG_SUCCESS,
                "msg": "ok",
                "data": response.text
            }
        else:
            response.raise_for_status()
    except Exception as e:
        return {
            "code": MSG_FAILED,
            "msg": str(e),
            "data": None
        }
