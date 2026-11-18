#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Curriculum Master Orchestrator: Applies age-appropriate content across all 450 lessons.
"""

import json
import os
import copy
from packs.kindergarten_pack import KINDERGARTEN_PACK
from packs.primary_pack import PRIMARY_PACK
from packs.middle_pack import MIDDLE_PACK
from packs.high_pack import HIGH_PACK

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

def get_pack_for_level(level_name):
    l = level_name.lower()
    if 'mầm' in l or 'kindergarten' in l:
        return KINDERGARTEN_PACK
    if 'tiểu' in l or 'primary' in l:
        return PRIMARY_PACK
    if 'thcs' in l or 'middle' in l:
        return MIDDLE_PACK
    return HIGH_PACK

def main():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    total_lectures = 0
    level_counts = {}

    for lvl in data:
        level_name = lvl.get('level', '')
        level_pack = get_pack_for_level(level_name)
        level_counts[level_name] = 0

        for lg in lvl.get('languages', []):
            lang_code = lg.get('lang', 'VIE')
            lang_dict = level_pack.get(lang_code, level_pack.get('VIE', {}))

            for topic in lg.get('topics', []):
                topic_name = topic.get('topicName', '')
                for lecture in topic.get('lectures', []):
                    title = lecture.get('title', '')
                    dom_key = detect_domain(title, topic_name)

                    dom_data = lang_dict.get(dom_key)
                    if not dom_data:
                        dom_data = lang_dict.get('bridge', list(lang_dict.values())[0])

                    # Build personalized 6 quiz questions
                    quiz_source = copy.deepcopy(dom_data['quiz'])
                    for q in quiz_source:
                        q['question'] = q['question'].replace('{title}', title)
                        if '{title}' in q.get('explanation', ''):
                            q['explanation'] = q['explanation'].replace('{title}', title)

                    # Build practice data
                    practice_source = {
                        'flashcards': copy.deepcopy(dom_data['flashcards']),
                        'matchingPairs': copy.deepcopy(dom_data['matching']),
                        'sequencing': copy.deepcopy(dom_data['sequencing']),
                        'cloze': copy.deepcopy(dom_data['cloze'])
                    }

                    # Attach to lecture
                    lecture['quizData'] = quiz_source
                    lecture['practiceData'] = practice_source

                    total_lectures += 1
                    level_counts[level_name] += 1

    print(f"Successfully processed {total_lectures} lectures across levels:")
    for k, v in level_counts.items():
        print(f"  - {k}: {v} lectures")

    # Save to data.json
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Saved updated data.json")

    # Export to data.js
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write("// STEM LMS Global Curriculum Dataset (Age-Appropriate Calibrated)\n")
        f.write("window.APP_DATA = ")
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print("Saved updated data.js")

if __name__ == '__main__':
    main()
