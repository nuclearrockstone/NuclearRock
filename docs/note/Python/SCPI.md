---
title: SCPI
---

# SCPI

**SCPI是Standard Command for Programmable Instruments（可编程仪器标准指令）的简称，**是在IEEE-488（通用接口总线）上定义的一种通信规范，可以用于自动测试设备和电子测试设备

> 本次实践基于胜利仪器VC4091C进行，主要使用Python操作串口进行了命令的手法，实现了对数据的读取和实时显示，未尽之处，尚待补充

SCPI可以运行在多种物理层之上，VC4091C支持USB，RS232等多种串口，安装驱动后，可以使用串口调试助手验证相关SCPI命令

[串口调试助手下载链接](https://apps.microsoft.com/detail/9nblggh43hdm?launch=true&hl=zh-cn&gl=cn)

选择相应的串口，并设置波特率为9600，在发送窗口发送SCPI命令，查询仪器型号和制造商的等信息

```shell
>>> *IDN?/n
>>> VIC,VICTOR 4091C   ,V6.00.2405.039,V1.12.2103.008,101340702
```

:::note 

需要注意的是，每一条SCPI都以换行符结尾（即为胜利仪器给出的手册中给出的每帧结尾的0a），可以手动敲回车模拟换行符

::: 

若成功返回相关信息，则说明驱动和串口已经配置成功，可以使用Python开始自动化操作了

<details>
<summary>**胜利仪器SCPI指令表**</summary>

    | 指令 | 意义 |
    | --- | --- |
    | *IDN? | 基本信息查询 |
    | FETCH? | 获取仪器测量数据 |

</details>

1. 安装`Pyserial`模块

2. 定义串口并尝试收发指令：注意到使用`with`关键字管理上下文，避免未释放串口资源导致的BUG
    ```python
    port = "COM3"
    baudrate = 9600  # 波特率，根据你的设备设定
    CHECK_COMMAND = "*IDN?\n"
    
    import serial
    
    with serial.Serial(port, baudrate, timeout=1) as ser:
    	print(f"Connected to {port} at {baudrate} baud.")
      ser.write(CHECK_COMMAND.encode())
      response = ser.readline().decode().strip()
      print(f"Response: {response}")
     
    ```


1. 运行成功后，可以得到和在串口调试工具中一致的结果

2. 随后，定义收发指令的函数
    ```python
    def SCPI_CMD(command: str,port:str=port,baudrate:int=baudrate) -> str:
        """
        发送SCPI命令并返回响应
        :param command: SCPI命令
        :return: 响应字符串
        """
        with serial.Serial(port, baudrate, timeout=1) as ser:
            ser.write((command + "\n").encode())
            response = ser.readline().decode().strip()
            return response
    ```


在使用时调用改函数即可获取实时测量数据

