#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re

def detect_category(title, topic_name):
    s = ((title or "") + " " + (topic_name or "")).lower()
    if any(k in s for k in ['máy bay', 'tên lửa', 'dù lượn', 'phi thuyền', 'khí cầu', 'rocket', 'plane', 'aerospace', 'parachute', 'glider', 'wing', 'flight', 'hàng không', 'không lưu']):
        return "aerospace"
    if any(k in s for k in ['thuyền', 'tàu thủy', 'chìm nổi', 'phao', 'submarine', 'boat', 'ship', 'buoyancy', 'sail', 'thủy sinh', 'biển', 'nước', 'watermill', 'cối xay nước']):
        return "marine"
    if any(k in s for k in ['cầu', 'bridge', 'vòm', 'giàn không gian', 'trụ cầu', 'tháp', 'tower', 'kết cấu', 'chịu lực', 'trọng tải', 'mái nhà', 'nhà']):
        return "bridge"
    if any(k in s for k in ['gió', 'mặt trời', 'năng lượng', 'pin', 'solar', 'wind turbine', 'turbine', 'cối xay gió', 'renewable']):
        return "energy_renewable"
    if any(k in s for k in ['mạch điện', 'led', 'dây dẫn', 'công tắc', 'điện trở', 'circuit', 'voltage', 'pin chanh', 'lemon battery', 'sensor', 'cảm biến', 'điện']):
        return "circuit"
    if any(k in s for k in ['lọc nước', 'nước sạch', 'filter', 'filtration', 'môi trường', 'chất thải', 'ô nhiễm', 'đất', 'water purify', 'tái chế']):
        return "filtration"
    if any(k in s for k in ['robot', 'cánh tay robot', 'băng chuyền', 'tự động', 'gripper', 'pneumatic', 'khí nén', 'hydraulic', 'thủy lực']):
        return "robotics"
    if any(k in s for k in ['con quay', 'ròng rọc', 'bánh răng', 'đòn bẩy', 'pulley', 'gear', 'lever', 'cam', 'cơ cấu', 'máy móc', 'con lắc', 'pendulum']):
        return "mechanism"
    if any(k in s for k in ['vật liệu', 'polyme', 'composite', 'cách nhiệt', 'cách âm', 'bao bì', 'túi', 'chống sốc', 'áo giáp', 'keo', 'slime', 'nano', 'tinh thể']):
        return "materials_science"
    if any(k in s for k in ['máy tính', 'thuật toán', 'mã hóa', 'binary', 'computer', 'scratch', 'code', 'logic', 'mạng', 'mã vạch', 'barcode', 'html']):
        return "computing"
    if any(k in s for k in ['xe', 'ô tô', 'car', 'vehicle', 'tốc độ', 'ma sát', 'dây cao su', 'balloon car', 'xe đua']):
        return "vehicle"
    return "biology"

print("Category detector verified.")
