import time
import func

def main():
    sto = "none"
    while True:
        print("请选择操作：1.创建虚拟机 2.删除虚拟机 3.显示所有云主机属性 4.删除所有虚拟机 5.停止所有虚拟机 6.开启所有虚拟机  "
              "7.开启美国服务器 8.停止美国服务器 9.显示美国ip地址 10.退出")

        choice = input("输入选项：").strip()
        if choice == "1":
            info=func.create_vm().to_map()
            instance_id = info['body']['InstanceIdSets']['InstanceIdSet'][0]
            print(f"实例 ID: {instance_id}")
            sto=instance_id

        elif choice == "2":
            user_input = input(f"请输入实例 ID(直接回车使用默认值 {sto}): ").strip()
            # 检查用户是否有输入
            if user_input == "":
                # 用户直接回车，使用默认值
                instance_id = sto
            else:
                # 用户有输入，使用用户的输入
                instance_id = user_input
            # 调用 func.main，并传入 instance_id
                print(f"正在删除{instance_id}")
            time.sleep(5)
            func.delete_vm(instance_id)
            if sto != "none":
                print("well done!")

        elif choice == "3":
            func.shallfuc()

        elif choice == "4":
            func.delete_all()

        elif choice == "5":
            func.stop_vm()
        elif choice == "6":
            func.start_vm()
        elif choice == "7":
            func.us_start()
        elif choice == "8":
            func.us_stop()
        elif choice == "9":
            func.us_show()
        elif choice == "10":
            print("退出程序。")
            break
        else:
            print("无效的选项，请重新输入。")
if __name__ == "__main__":
    main()
