# -*- coding: utf-8 -*-
import os
import sys

from typing import List

from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


class st:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> Ecs20140526Client:
        """
        使用AK&SK初始化账号Client
        """
        config = open_api_models.Config(
            access_key_id=os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_ID'),
            access_key_secret=os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_SECRET')
        )
        config.endpoint = 'ecs.cn-shanghai.aliyuncs.com'
        return Ecs20140526Client(config)

    @staticmethod
    def start_instance(instance_id: str) -> None:
        client = st.create_client()
        start_instance_request = ecs_20140526_models.StartInstanceRequest(
            instance_id=instance_id
        )
        runtime = util_models.RuntimeOptions()
        try:
            response = client.start_instance_with_options(start_instance_request, runtime)
            print(response)
        except Exception as error:
            print(f"Error message: {error.message}")
            if error.data:
                print(f"Recommend: {error.data.get('Recommend')}")

    @staticmethod
    async def start_instance_async(instance_id: str) -> None:
        client = st.create_client()
        start_instance_request = ecs_20140526_models.StartInstanceRequest(
            instance_id=instance_id
        )
        runtime = util_models.RuntimeOptions()
        try:
            response = await client.start_instance_with_options_async(start_instance_request, runtime)
            print(response)
        except Exception as error:
            print(f"Error message: {error.message}")
            if error.data:
                print(f"Recommend: {error.data.get('Recommend')}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        st.start_instance(sys.argv[1])
    else:
        print("Please provide an instance ID.")
