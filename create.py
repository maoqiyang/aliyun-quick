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


class create:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Ecs20140526Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 必填，您的 AccessKey ID,
            access_key_id=access_key_id,
            # 必填，您的 AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # Endpoint 请参考 https://api.aliyun.com/product/Ecs
        config.endpoint = f'ecs.cn-shanghai.aliyuncs.com'
        return Ecs20140526Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例使用环境变量获取 AccessKey 的方式进行调用，仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html
        client = create.create_client(os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'], os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'])
        system_disk = ecs_20140526_models.RunInstancesRequestSystemDisk(
            category='cloud_essd_entry',
            size='40'
        )
        run_instances_request = ecs_20140526_models.RunInstancesRequest(
            region_id='cn-shanghai',
            instance_type='ecs.e-c1m2.large',
            security_group_id='sg-uf68ogvsofz1u0vdu4tf',
            v_switch_id='vsw-uf6qdbgxrcv1ee0kihxsv',
            image_id='centos_7_6_x64_20G_alibase_20211130.vhd',
            internet_max_bandwidth_in=200,
            internet_max_bandwidth_out=5,
            password='123456',
            internet_charge_type='PayByTraffic',
            key_pair_name='123',
            spot_strategy='SpotAsPriceGo',
            system_disk=system_disk,
            #amount = 2
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值

            info=client.run_instances_with_options(run_instances_request, runtime)
            return info
        except Exception as error:
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例使用环境变量获取 AccessKey 的方式进行调用，仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html
        client = create.create_client(os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'], os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'])
        system_disk = ecs_20140526_models.RunInstancesRequestSystemDisk(
            category='cloud_essd_entry',
            size='40'
        )
        run_instances_request = ecs_20140526_models.RunInstancesRequest(
            region_id='cn-shanghai',
            instance_type='ecs.e-c1m2.large',
            security_group_id='sg-uf68ogvsofz1u0vdu4tf',
            v_switch_id='vsw-uf6qdbgxrcv1ee0kihxsv',
            image_id='centos_7_6_x64_20G_alibase_20211130.vhd',
            internet_max_bandwidth_in=200,
            internet_max_bandwidth_out=5,
            password='123456',
            internet_charge_type='PayByTraffic',
            key_pair_name='123',
            spot_strategy='SpotAsPriceGo',
            system_disk=system_disk,
            #amount = 2   增加数量
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            await client.run_instances_with_options_async(run_instances_request, runtime)
        except Exception as error:
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


if __name__ == '__main__':
    create.main(sys.argv[1:])
