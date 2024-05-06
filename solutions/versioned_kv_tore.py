# -*- coding: utf-8 -*-

################################################
#
# openai coding question
#
# designed a versioned key-value store, with two functions:
# 1. getCell(String key, Integer version)
# 2. setCellValue(String key, Integer value, Integer version)
#
# Following-up questions:
# 1. How to make these two methods thread-safe?
# 2. How to handle OOM cases?
################################################

import bisect
from collections import defaultdict
import time
import threading


class VersionedKVStore:
    def __init__(self):
        self.store = defaultdict(list)
        self.lock = threading.Lock()

    def put(self, key: str, value: str):
        time_stamp = time.time()
        with self.lock:
            self.store[key].append((time_stamp, value))
            self.store[key].sort(key=lambda x: x[0])

    def get(self, key, time_stamp=None):
        with self.lock:
            if key not in self.store:
                return None

            if time_stamp is None:
                return self.store[key][-1][1]

            index = bisect.bisect_right(self.store[key], (time_stamp, float('inf'))) - 1  # 二分查找最大时间戳
            if index < 0:
                return None
            return self.store[key][index][1]

    def get_history(self, key):
        return self.store.get(key, [])


kv_store = VersionedKVStore()
kv_store.put('key1', 'value1')
time.sleep(1)
kv_store.put('key1', 'value2')

print("Latest value for key1:", kv_store.get('key1'))

timestamp = time.time() - 0.5
print("Value for key1 at timestamp {}: {}".format(timestamp, kv_store.get('key1', timestamp)))

print("History for key1:", kv_store.get_history('key1'))
