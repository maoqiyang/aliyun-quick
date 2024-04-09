# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys

from typing import List

from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class sp:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> Ecs20140526Client:
        """
        使用AK&SK初始化账号Client
        """
        config = open_api_models.Config(
            access_key_id=os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
            access_key_secret=os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET']
        )
        config.endpoint = 'ecs.cn-shanghai.aliyuncs.com'
        return Ecs20140526Client(config)

    @staticmethod
    def stop_instance(instance_id: str) -> None:
        client = sp.create_client()
        stop_instance_request = ecs_20140526_models.StopInstanceRequest(
            instance_id=instance_id,
            stopped_mode='StopCharging'
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 尝试停止实例并打印返回的 API 响应
            response = client.stop_instance_with_options(stop_instance_request, runtime)
            print(response)
        except Exception as error:
            print(error.message)
            print(error.data.get("Recommend"))

    @staticmethod
    async def stop_instance_async(instance_id: str) -> None:
        client = sp.create_client()
        stop_instance_request = ecs_20140526_models.StopInstanceRequest(
            instance_id=instance_id,
            stopped_mode = 'StopCharging'
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 异步停止实例并打印返回的 API 响应
            response = await client.stop_instance_with_options_async(stop_instance_request, runtime)
            print(response)
        except Exception as error:
            print(error.message)
            print(error.data.get("Recommend"))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        sp.stop_instance(sys.argv[1])
    else:
        print("Please provide an instance ID.")
