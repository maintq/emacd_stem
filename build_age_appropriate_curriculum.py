#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Curriculum Builder: Age-Appropriate STEM Quiz and Practice Generator
Generates pedagogically calibrated questions and activities for all 4 educational levels:
1. Mầm non (Kindergarten, 3-5/6 years old)
2. Tiểu học (Primary School, Grades 1-5, 6-11 years old)
3. THCS (Middle School, Grades 6-9, 11-15 years old)
4. THPT (High School, Grades 10-12, 15-18 years old)
Supports both VIE and ENG across 12 authentic STEM technical domains.
"""

import json
import os
import sys

def detect_domain(title, topic):
    text = (title + " " + topic).lower()
    if any(k in text for k in ['bay', 'flight', 'rocket', 'tên lửa', 'drone', 'không lưu', 'air traffic', 'blast off', 'dù lượn', 'hang glider', 'paraglider', 'aerospace']):
        return 'aerospace'
    if any(k in text for k in ['thuyền', 'boat', 'chìm', 'nổi', 'buoyancy', 'float', 'sink', 'tàu', 'oil spill', 'tràn dầu', 'marine', 'submarine']):
        return 'marine'
    if any(k in text for k in ['cầu', 'bridge', 'mái vòm', 'dome', 'tháp', 'tower', 'lighthouse', 'mái nhà', 'roof', 'kiến trúc', 'architectural', 'critical load', 'túp lều', 'shelter', 'island survival', 'sinh tồn']):
        return 'bridge'
    if any(k in text for k in ['mặt trời', 'solar', 'gió', 'wind', 'cối xay', 'watermill', 'windmill', 'đập', 'dam', 'thủy điện', 'năng lượng', 'green energy', 'irrigation', 'tưới tiêu']):
        return 'energy_renewable'
    if any(k in text for k in ['mạch', 'circuit', 'điện', 'electric', 'pin', 'battery', 'đèn pin', 'flashlight', 'biến áp', 'transformer', 'ohm', 'conductor', 'insulator', 'bán dẫn']):
        return 'circuit'
    if any(k in text for k in ['lọc', 'filter', 'nước', 'water', 'tái chế', 'recycling', 'nhựa', 'plastic', 'môi trường', 'pollution', 'bảo vệ môi trường']):
        return 'filtration'
    if any(k in text for k in ['robot', 'cánh tay robot', 'robotic', 'servo', 'cảm biến', 'sensor', 'arduino', 'blink', 'voorhis']):
        return 'robotics'
    if any(k in text for k in ['đòn bẩy', 'lever', 'ròng rọc', 'pulley', 'bánh răng', 'gear', 'con quay', 'spinner', 'băng tải', 'conveyor', 'cáp treo', 'chair lift', 'dây chuyền', 'assembly line', 'balance', 'bấm móng tay', 'clipper']):
        return 'mechanism'
    if any(k in text for k in ['nano', 'kính hiển vi', 'microscope', 'mạ đồng', 'copperplate', 'tinh thể', 'crystal', 'vật liệu', 'materials', 'khoai tây', 'potato', 'kẹo', 'candy', 'bột', 'dough']):
        return 'materials_science'
    if any(k in text for k in ['mã vạch', 'barcode', 'thuật toán', 'algorithm', 'complexity', 'độ phức tạp', 'mê cung', 'maze', 'html', 'lập trình', 'programming', 'binary', 'mouse', 'search engine', 'code', 'sorting']):
        return 'computing'
    if any(k in text for k in ['xe', 'car', 'racer', 'rubber band', 'dây cao su', 'dốc', 'skier', 'seismograph', 'động đất', 'vận tải', 'transportation', 'road', 'bearings', 'bounce', 'super ball', 'force', 'lực']):
        return 'vehicle'
    if any(k in text for k in ['rover', 'kỳ nhông', 'salamander', 'chim', 'bird', 'động vật', 'animal', 'sinh học', 'biology', 'wildlife', 'cây', 'plant', 'nature', 'weather', 'bóng râm', 'shadow', 'biomimicry']):
        return 'biology'
    return 'bridge'

def get_age_tier(level_str):
    l = level_str.lower()
    if 'mầm' in l or 'kindergarten' in l:
        return 'kindergarten'
    if 'tiểu' in l or 'primary' in l:
        return 'primary'
    if 'thcs' in l or 'middle' in l:
        return 'middle'
    return 'high'

print("Master curriculum builder loaded.")
