#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import unicodedata

LESSON_PLAN_TEMPLATES = {
    "khoa-hoc-vat-ly": {
        "discipline": "Khoa học Vật lý & Động lực học (Physics & Dynamics)",
        "duration": "90 - 120 phút",
        "scenario": "Một nhà máy sản xuất phương tiện tự động đang nghiên cứu nguyên mẫu xe tiết kiệm năng lượng, vận hành hoàn toàn nhờ thế năng chuyển hóa thành động năng mà không gây ô nhiễm.",
        "criteria": [
            "Mô hình phải tự chuyển động liên tục quãng đường tối thiểu 3 mét (10 feet) trên sàn phẳng.",
            "Cơ chế truyền động phải ổn định, không bị kẹt trục khi giải phóng năng lượng."
        ],
        "constraints": [
            "Chỉ sử dụng tối đa 4 dây cao su hoặc lò xo cơ học nhỏ.",
            "Không dùng pin điện hoặc bất kỳ chất đốt nào."
        ],
        "calc": {
            "type": "velocity",
            "title": "Bảng Tính Vận Tốc Thực Nghiệm (Velocity Calculator)",
            "label1": "Quãng đường đo được (mét)",
            "label2": "Thời gian chuyển động (giây)",
            "unit": "m/s",
            "formula": "v = s / t"
        }
    },
    "thiet-ke-cong-trinh": {
        "discipline": "Kỹ thuật Xây dựng & Kết cấu Kiến trúc (Civil & Structural Engineering)",
        "duration": "90 - 120 phút",
        "scenario": "Một trận lũ lớn đã cuốn trôi cây cầu độc đạo nối liền hai ngôi làng. Nhóm kỹ sư của bạn được giao nhiệm vụ thiết kế một cây cầu tạm có nhịp vượt 30cm, sử dụng vật liệu nhẹ nhưng chịu được tải trọng lớn.",
        "criteria": [
            "Cây cầu phải bắc qua khoảng trống tối thiểu 30cm mà không có trụ chống ở giữa.",
            "Phải chịu được tải trọng thử nghiệm tối thiểu 500g đặt tại chính giữa thân cầu mà không bị sập."
        ],
        "constraints": [
            "Chỉ được dùng tối đa 60 que kem gỗ và keo dán thủ công.",
            "Không được dán cố định mố cầu vào mép bàn kiểm tra."
        ],
        "calc": {
            "type": "bridge_ratio",
            "title": "Bảng Tính Tỷ Số Chịu Tải Kỹ Thuật (Strength-to-Weight Ratio)",
            "label1": "Tải trọng chịu được trước khi gãy (gam)",
            "label2": "Khối lượng bản thân cây cầu (gam)",
            "unit": "lần (Tỷ số)",
            "formula": "Tỷ số = Tải trọng chịu được / Khối lượng cầu"
        }
    },
    "nang-luong-xanh": {
        "discipline": "Năng lượng Tái tạo & Kỹ thuật Môi trường (Renewable Energy)",
        "duration": "60 - 90 phút",
        "scenario": "Một trạm nghiên cứu thời tiết trên đảo xa cần nguồn điện liên tục từ ánh sáng mặt trời và sức gió để vận hành các cảm biến khí tượng mà không cần thay pin hóa học.",
        "criteria": [
            "Mô hình phải thu nhận được năng lượng ánh sáng hoặc động năng gió để tạo ra dòng điện hoặc công cơ học.",
            "Thiết kế góc hứng ánh sáng hoặc cánh đón gió đạt hiệu suất cao nhất."
        ],
        "constraints": [
            "Sử dụng pin năng lượng mặt trời mini (1.5V - 3V) hoặc mô tơ quay DC tái chế.",
            "Toàn bộ vật liệu phải chịu được ánh nắng trực tiếp ngoài trời."
        ],
        "calc": {
            "type": "power",
            "title": "Bảng Tính Công Suất Điện Năng (Electrical Power)",
            "label1": "Hiệu điện thế đo được (Vôn - V)",
            "label2": "Cường độ dòng điện đo được (Ampe - A)",
            "unit": "Watt (W)",
            "formula": "P = U * I"
        }
    },
    "lap-trinh": {
        "discipline": "Khoa học Máy tính & Tư duy Thuật toán (Computer Science)",
        "duration": "60 - 90 phút",
        "scenario": "Một nhóm thám hiểm cần lập trình cho một robot tự hành điều hướng trong mê cung ngầm để tìm kiếm lối ra an toàn mà không bị va chạm vào tường đá.",
        "criteria": [
            "Xây dựng thuật toán logic tuần tự giúp robot giải quyết bài toán mê cung.",
            "Viết mã lệnh HTML chuẩn ngữ nghĩa để hiển thị thông tin báo cáo thám hiểm."
        ],
        "constraints": [
            "Thuật toán phải đảm bảo tính dừng (không rơi vào vòng lặp vô tận).",
            "Mã nguồn phải rõ ràng, có chú thích giải thích các khối lệnh."
        ],
        "calc": {
            "type": "complexity",
            "title": "Bảng Ước Tính Độ Phức Tạp Thuật Toán (Steps Counter)",
            "label1": "Số lượng ngã rẽ trong mê cung (N)",
            "label2": "Thời gian xử lý trung bình mỗi bước (giây)",
            "unit": "giây",
            "formula": "Thời gian tổng = N * Thời gian mỗi bước"
        }
    },
    "generic": {
        "discipline": "Khoa học Ứng dụng & Kỹ thuật STEM (Applied STEM Engineering)",
        "duration": "60 - 90 phút",
        "scenario": "Nhóm của bạn được giao một thử thách kỹ thuật thực tế: nghiên cứu nguyên lý hoạt động của đối tượng, phác thảo thiết kế và kiểm tra thử nghiệm để giải quyết vấn đề đặt ra.",
        "criteria": [
            "Sản phẩm hoàn thiện phải đáp ứng đầy đủ công năng theo yêu cầu đề bài.",
            "Quy trình thử nghiệm phải thu thập được số liệu định lượng rõ ràng."
        ],
        "constraints": [
            "Sử dụng vật liệu an toàn, dễ tìm và thân thiện với môi trường.",
            "Hoàn thành mô hình và báo cáo trong thời lượng tiết học."
        ],
        "calc": {
            "type": "general",
            "title": "Bảng Tính Hiệu Suất Mô Hình (Efficiency Calculator)",
            "label1": "Kết quả thực tế đạt được",
            "label2": "Mục tiêu lý thuyết đề ra",
            "unit": "%",
            "formula": "Hiệu suất = (Thực tế / Lý thuyết) * 100"
        }
    }
}

def get_template_key(topic_name):
    t = unicodedata.normalize('NFC', topic_name).lower()
    if any(k in t for k in ["vật lý", "lực", "chuyển động", "physics", "force", "motion", "vận tải", "transportation", "hàng không", "aerospace"]):
        return "khoa-hoc-vat-ly"
    if any(k in t for k in ["công trình", "kiến trúc", "cầu", "tháp", "architectural", "construction", "bridge"]):
        return "thiet-ke-cong-trinh"
    if any(k in t for k in ["năng lượng", "mặt trời", "gió", "green energy", "solar", "môi trường", "environmental"]):
        return "nang-luong-xanh"
    if any(k in t for k in ["lập trình", "máy tính", "programming", "computer", "robotics"]):
        return "lap-trinh"
    return "generic"

def enrich_lecture_with_lesson_plan(lec, topic_name, lang, level_name):
    tpl_key = get_template_key(topic_name)
    tpl = LESSON_PLAN_TEMPLATES[tpl_key]
    title = lec.get("title", "Bài học STEM")
    is_vie = (lang == "VIE")

    if is_vie:
        overview = {
            "ageGroup": f"Phù hợp: {level_name}",
            "duration": tpl["duration"],
            "discipline": tpl["discipline"],
            "summary": f"Bài học STEM '{title}' được thiết kế dựa trên giáo án kỹ thuật thực hành. Học sinh sẽ tìm hiểu nguyên lý khoa học đằng sau đối tượng nghiên cứu, thực hành phác thảo thiết kế, tự tay chế tạo mô hình và thu thập số liệu thử nghiệm."
        }
        objectives = [
            f"Hiểu rõ nguyên lý khoa học nền tảng của {title} và cơ chế vận hành trong đời sống.",
            "Làm việc nhóm theo Quy trình Thiết kế Kỹ thuật 5 bước (EDP): Hỏi ➔ Tưởng tượng ➔ Lập kế hoạch ➔ Chế tạo ➔ Cải tiến.",
            "Thu thập số liệu đo lường thực nghiệm và áp dụng công thức toán học để đánh giá hiệu suất mô hình.",
            "Phát hiện lỗi kỹ thuật, phân tích nguyên nhân và thực hiện cải tiến tối ưu hóa sản phẩm."
        ]
        materials = {
            "required": [
                "Bìa cứng carton hoặc que gỗ kem thủ công",
                "Dây cao su đàn hồi hoặc băng keo kết dính",
                "Kéo cắt an toàn hoặc dao trổ giấy"
            ],
            "optional": [
                "Nắp chai nhựa tái chế hoặc lõi giấy vệ sinh",
                "Que xiên tre hoặc kẹp giấy kim loại",
                "Màu vẽ trang trí mô hình"
            ],
            "tools": [
                "Thước đo milimet hoặc thước dây cuộn",
                "Đồng hồ bấm giờ (điện thoại hoặc stopwatch)",
                "Bút chì và giấy kẻ ô phác thảo ý tưởng"
            ]
        }
        challenge = {
            "scenario": f"Đặt trong bối cảnh thực tế: {tpl['scenario']}",
            "criteria": tpl["criteria"],
            "constraints": tpl["constraints"]
        }
        scientific_principles = [
            {
                "title": f"Bản chất Khoa học Cốt lõi của {title}",
                "explanation": f"Mọi cơ chế hoạt động của {title} đều tuân theo các định luật vật lý cơ bản: định luật bảo toàn năng lượng, sự cân bằng lực và phản lực, cùng các thuộc tính cơ học của vật liệu chế tạo.",
                "formula": tpl["calc"]["formula"],
                "realWorldApp": f"Nguyên lý này được ứng dụng rộng rãi trong các dây chuyền công nghiệp hiện đại và các công trình kỹ thuật quy mô lớn."
            },
            {
                "title": "Ma sát & Tổn hao Năng lượng",
                "explanation": "Trong quá trình vận hành, một phần năng lượng hữu ích sẽ bị biến đổi thành nhiệt năng do ma sát giữa các bề mặt tiếp xúc và sức cản của môi trường không khí.",
                "formula": "F_ms = μ * N",
                "realWorldApp": "Kỹ sư cơ khí luôn tìm cách tối ưu hóa khí động học và sử dụng vòng bi bôi trơn để giảm thiểu ma sát hao phí."
            }
        ]
        engineering_steps = [
            {
                "stepNumber": 1,
                "stepName": "Bước 1: Hỏi & Khảo sát (Ask)",
                "instruction": f"Xác định rõ vấn đề cần giải quyết với {title}: Yêu cầu kỹ thuật là gì? Những ràng buộc nào cần tuân thủ? Những vật liệu nào hiện có sẵn trong lớp?",
                "proTip": "Ghi chép lại các tiêu chí đánh giá vào sổ tay kỹ thuật trước khi bắt đầu."
            },
            {
                "stepNumber": 2,
                "stepName": "Bước 2: Tưởng tượng Giải pháp (Imagine)",
                "instruction": "Từng thành viên trong nhóm đưa ra ít nhất 2 ý tưởng thiết kế khác nhau. Trao đổi và chọn ra giải pháp khả thi nhất về độ bền và thời gian thực hiện.",
                "proTip": "Không chỉ trích ý tưởng của bạn bè; khuyến khích những sáng kiến độc đáo."
            },
            {
                "stepNumber": 3,
                "stepName": "Bước 3: Lập kế hoạch & Vẽ bản vẽ (Plan)",
                "instruction": "Vẽ phác thảo mô hình chi tiết với kích thước cụ thể trên giấy kẻ ô. Lập danh sách phân công nhiệm vụ cho từng thành viên trong nhóm.",
                "proTip": "Bản vẽ càng chi tiết thì khi lắp ráp càng ít xảy ra sai sót lệch kích thước."
            },
            {
                "stepNumber": 4,
                "stepName": "Bước 4: Chế tạo & Lắp ráp (Create)",
                "instruction": "Tiến hành cắt ghép vật liệu và lắp ráp từng cụm chi tiết theo đúng bản vẽ thiết kế đã duyệt. Chú ý an toàn khi dùng kéo và keo dán.",
                "proTip": "Kiểm tra độ chắc chắn của từng mối nối trước khi dán cố định toàn bộ mô hình."
            },
            {
                "stepNumber": 5,
                "stepName": "Bước 5: Thử nghiệm & Hoàn thiện (Test & Improve)",
                "instruction": "Đưa sản phẩm vào bài kiểm tra thực nghiệm. Ghi nhận số liệu đo lường. Nếu sản phẩm chưa đạt mục tiêu, hãy tìm nguyên nhân và gia cố lại.",
                "proTip": "Thất bại trong lần thử nghiệm đầu tiên là cơ hội quý giá nhất để học hỏi và cải tiến!"
            }
        ]
        lab_calculator = tpl["calc"]
        discussion_questions = [
            f"Điểm khó khăn lớn nhất mà nhóm bạn gặp phải khi chế tạo {title} là gì và các bạn đã khắc phục như thế nào?",
            "Nếu có thêm thời gian và ngân sách vật liệu tốt hơn, bạn sẽ nâng cấp chi tiết nào của mô hình?",
            "Làm thế nào để áp dụng bài học này vào việc giải quyết một vấn đề thực tế trong trường học hoặc gia đình của em?",
            "Theo em, sự khác biệt giữa một người thợ thủ công và một kỹ sư thiết kế STEM nằm ở điểm nào?"
        ]
    else:
        overview = {
            "ageGroup": f"Recommended for: {level_name}",
            "duration": tpl["duration"],
            "discipline": tpl["discipline"],
            "summary": f"This STEM hands-on lesson '{title}' guides students through the complete engineering design process. Learners explore underlying scientific principles, sketch design schematics, construct functional prototypes, and analyze empirical test data."
        }
        objectives = [
            f"Understand the fundamental scientific and physical principles governing {title}.",
            "Apply the 5-step Engineering Design Process (EDP): Ask, Imagine, Plan, Create, Test & Improve.",
            "Gather empirical quantitative measurements and compute performance metrics using standard formulas.",
            "Analyze points of failure and iterate to optimize the prototype design."
        ]
        materials = {
            "required": [
                "Corrugated cardboard or wooden craft sticks",
                "Elastic rubber bands or adhesive masking tape",
                "Safety scissors or craft cutters"
            ],
            "optional": [
                "Recycled plastic bottle caps or paper towel tubes",
                "Wooden skewers, straws, or metal paperclips",
                "Markers and labels for prototype decoration"
            ],
            "tools": [
                "Metric ruler or measuring tape",
                "Stopwatch or digital smartphone timer",
                "Graph paper and pencil for drafting"
            ]
        }
        challenge = {
            "scenario": f"Real-world Context: {tpl['scenario']}",
            "criteria": tpl["criteria"],
            "constraints": tpl["constraints"]
        }
        scientific_principles = [
            {
                "title": f"Core Scientific Principle of {title}",
                "explanation": f"The performance of {title} relies directly on fundamental physical laws: conservation of energy, force and reaction, and material mechanical properties.",
                "formula": tpl["calc"]["formula"],
                "realWorldApp": "These engineering principles underpin modern industrial automation and structural design."
            }
        ]
        engineering_steps = [
            {
                "stepNumber": 1,
                "stepName": "Step 1: Ask & Define (Ask)",
                "instruction": f"Define the engineering problem clearly: What are the criteria and constraints for {title}? What materials are available?",
                "proTip": "Document key design constraints in your engineering notebook."
            },
            {
                "stepNumber": 2,
                "stepName": "Step 2: Imagine & Brainstorm (Imagine)",
                "instruction": "Brainstorm multiple possible design configurations with your teammates. Select the most promising concept.",
                "proTip": "Encourage wild ideas and combine concepts to find innovative solutions."
            },
            {
                "stepNumber": 3,
                "stepName": "Step 3: Plan & Schematic (Plan)",
                "instruction": "Draw a dimensioned diagram on graph paper. List materials required and assign assembly roles.",
                "proTip": "Accurate planning minimizes measurement errors during assembly."
            },
            {
                "stepNumber": 4,
                "stepName": "Step 4: Create Prototype (Create)",
                "instruction": "Assemble the model following the approved plan. Follow proper workshop safety rules.",
                "proTip": "Verify the freedom of moving parts before gluing them securely."
            },
            {
                "stepNumber": 5,
                "stepName": "Step 5: Test & Iterate (Test & Improve)",
                "instruction": "Test the prototype under designated test conditions. Measure and record quantitative performance metrics.",
                "proTip": "Failure during testing is normal; use data to diagnose and strengthen weak points."
            }
        ]
        lab_calculator = {
            "type": tpl["calc"]["type"],
            "title": tpl["calc"]["title"],
            "label1": "Measured Test Parameter 1",
            "label2": "Measured Test Parameter 2",
            "unit": tpl["calc"]["unit"],
            "formula": tpl["calc"]["formula"]
        }
        discussion_questions = [
            f"What was the most challenging technical hurdle your team faced while building {title}?",
            "If you had access to stronger materials or more time, what specific improvements would you implement?",
            "How does this engineering activity connect to real-world technology in your daily life?"
        ]

    lec["lessonPlan"] = {
        "overview": overview,
        "objectives": objectives,
        "materials": materials,
        "challenge": challenge,
        "scientificPrinciples": scientific_principles,
        "engineeringSteps": engineering_steps,
        "labCalculator": lab_calculator,
        "discussionQuestions": discussion_questions
    }

def process_all_data():
    with open("data.json", "r", encoding="utf-8") as f:
        dataset = json.load(f)

    total_lectures = 0
    for lvl in dataset:
        lvl_name = lvl.get("levelFullName", lvl.get("level", "STEM"))
        for lg in lvl["languages"]:
            lang = lg["lang"]
            for t in lg["topics"]:
                topic_name = t["topicName"]
                for lec in t["lectures"]:
                    enrich_lecture_with_lesson_plan(lec, topic_name, lang, lvl_name)
                    total_lectures += 1

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)

    js_content = "/**\n * E-Learning Resource Tree Mock Data with Rich Digital Lesson Plans\n * Based directly on IEEE TryEngineering & ScienceBuddies lesson plan guides.\n */\nwindow.APP_DATA = " + json.dumps(dataset, ensure_ascii=False, indent=2) + ";\n"
    with open("data.js", "w", encoding="utf-8") as f:
        f.write(js_content)

    print(f"Normalized and enriched {total_lectures} lectures.")

if __name__ == "__main__":
    process_all_data()
