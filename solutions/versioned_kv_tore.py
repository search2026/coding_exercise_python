# -*- coding: utf-8 -*-

################################################
#
# openai coding question
#
# designed a versioned key-value store, with two functions:
# getCell(String key, Integer version)
# setCellValue(String key, Integer value, Integer version)
#
################################################

import bisect
from collections import defaultdict
import time
import threading

class VersionedKVStore:
    def __init__(self):
        self.store = defaultdict(list)  # 键值对存储
        self.lock = threading.Lock()

    def put(self, key, value):
        timestamp = time.time()  # 获取当前时间戳
        with self.lock:
            self.store[key].append((timestamp, value))  # 添加到键的值列表
            self.store[key].sort(key=lambda x: x[0])  # 根据时间戳排序

    def get(self, key, timestamp=None):
        with self.lock:
            if key not in self.store:
                return None

            if timestamp is None:
                return self.store[key][-1][1]  # 返回最新值

            index = bisect.bisect_right(self.store[key], (timestamp, float('inf'))) - 1  # 二分查找最大时间戳
            if index < 0:
                return None
            return self.store[key][index][1]  # 返回对应值

    def get_history(self, key):
        return self.store.get(key, [])  # 返回键的所有历史记录


# 示例用法
kv_store = VersionedKVStore()
kv_store.put('key1', 'value1')
time.sleep(1)  # 等待一秒，模拟时间间隔
kv_store.put('key1', 'value2')

# 查询最新值
print("Latest value for key1:", kv_store.get('key1'))

# 查询特定时间戳的值
timestamp = time.time() - 0.5  # 当前时间戳减去0.5秒
print("Value for key1 at timestamp {}: {}".format(timestamp, kv_store.get('key1', timestamp)))

# 查询键的历史记录
print("History for key1:", kv_store.get_history('key1'))
