# Copyright (c) 2022-2025, Foxconn. All rights reserved.
#
# Foxconn and its aiRobots division retain all intellectual property
# and proprietary rights in and to this software, related documentation,
# and any modifications thereto. Any use, reproduction, disclosure, or
# distribution of this software and related documentation without an express
# license agreement from Foxconn is strictly prohibited.
#

# --------------------------------------------------
# system
# --------------------------------------------------
from datetime import datetime


class Console:
    enable = True  # 控制開關

    # ANSI 顏色碼
    LIGHT_GREEN = "\033[92m"  # 亮綠色
    RESET = "\033[0m"  # 重置顏色

    @staticmethod
    def DBG_PRINT(message: str, tag: str = "") -> None:
        if Console.enable:
            current_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]  # 格式化時間
            tag_part = f"[{tag}] " if tag else ""  # 如果有 tag，拼接到輸出中
            print(
                f"{Console.LIGHT_GREEN}[{current_time}]{Console.RESET} {tag_part}{message}"
            )


# 提供簡化名稱，讓使用者可以直接 import
DBG_PRINT = Console.DBG_PRINT
