#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import unicodedata

def get_topic_category(topic_name):
    t = unicodedata.normalize('NFC', topic_name).lower()
    if any(k in t for k in ["vật lý", "lực", "chuyển động", "physics", "force", "motion", "vận tải", "transportation"]):
        return "mechanics"
    if any(k in t for k in ["công trình", "kiến trúc", "cầu", "tháp", "architectural", "construction", "bridge"]):
        return "structural"
    if any(k in t for k in ["năng lượng", "mặt trời", "gió", "green energy", "solar"]):
        return "energy"
    if any(k in t for k in ["lập trình", "máy tính", "programming", "computer", "robotics"]):
        return "computing"
    if any(k in t for k in ["môi trường", "hoang dã", "wildlife", "environmental", "conservation"]):
        return "environment"
    return "general_stem"

def create_diversified_practice(topic_name, title, lang):
    cat = get_topic_category(topic_name)
    is_vie = (lang == "VIE")

    if is_vie:
        if cat == "mechanics":
            flashcards = [
                {"term": "Thế năng đàn hồi", "phonetic": "/ɪˈlæstɪk pəˈtɛnʃəl/", "definition": "Năng lượng tích trữ khi vật bị biến dạng đàn hồi như lò xo hoặc dây cao su.", "example": "Dây cao su bị xoắn tích trữ năng lượng phóng xe đua."},
                {"term": "Động năng", "phonetic": "/kɪˈnɛtɪk ˈɛnərdʒi/", "definition": "Năng lượng mà vật có được do đang chuyển động.", "example": "Xe chạy càng nhanh thì động năng càng lớn."},
                {"term": "Lực ma sát", "phonetic": "/ˈfrɪkʃən fɔːrs/", "definition": "Lực cản trở chuyển động tại bề mặt tiếp xúc giữa hai vật thể.", "example": "Lốp xe cao su có gai giúp tăng ma sát bám đường."},
                {"term": "Vận tốc trung bình", "phonetic": "/ˈævərɪdʒ vəˈlɒsɪti/", "definition": "Tỷ số giữa quãng đường dịch chuyển và khoảng thời gian thực hiện chuyển động.", "example": "v = s / t đo độ nhanh chậm của xe đua."}
            ]
            matching = [
                {"term": "Dây cao su bị xoắn", "definition": "Tích trữ thế năng đàn hồi"},
                {"term": "Trục quay bánh xe", "definition": "Chuyển cơ năng làm bánh xe lăn"},
                {"term": "Bề mặt lốp xe có khía", "definition": "Tăng ma sát bám đường chống trượt"},
                {"term": "Dầu bôi trơn trục", "definition": "Giảm ma sát hao phí giữa các chi tiết"}
            ]
            sequencing = [
                {"stepNumber": 1, "text": "Khảo sát yêu cầu đề bài và chuẩn bị que xiên, nắp chai, dây cao su"},
                {"stepNumber": 2, "text": "Phác thảo kích thước khung gầm và vị trí lắp 2 trục bánh xe"},
                {"stepNumber": 3, "text": "Lắp ống hút cố định dưới khung và luồn trục quay qua ống"},
                {"stepNumber": 4, "text": "Gắn mấu giữ dây cao su trên trục bánh sau và nối với khung trước"},
                {"stepNumber": 5, "text": "Quấn dây cao su, thả xe trên đường đua và đo đạc thời gian, quãng đường"}
            ]
            cloze = [
                {
                    "sentence": "Khi bạn xoắn dây cao su quanh trục bánh xe, công cơ học được chuyển thành [...] tích trữ.",
                    "options": ["thế năng đàn hồi", "nhiệt năng hao phí", "từ trường vĩnh cửu"],
                    "answer": "thế năng đàn hồi",
                    "explanation": "Dây cao su bị kéo giãn hoặc xoắn sẽ tích lũy thế năng đàn hồi."
                },
                {
                    "sentence": "Để giảm ma sát giữa trục xe và khung gầm, kỹ sư luồn trục qua một đoạn [...] để trục quay tự do.",
                    "options": ["ống hút trơn", "băng dính nhám", "dây buộc chặt"],
                    "answer": "ống hút trơn",
                    "explanation": "Ống hút đóng vai trò ổ đỡ trục lỏng giúp giảm ma sát tiếp xúc."
                },
                {
                    "sentence": "Vận tốc trung bình của mô hình chuyển động được tính bằng công thức [...].",
                    "options": ["v = s / t", "v = s * t", "v = m * a"],
                    "answer": "v = s / t",
                    "explanation": "Vận tốc bằng quãng đường (s) chia cho thời gian (t)."
                }
            ]
        elif cat == "structural":
            flashcards = [
                {"term": "Kết cấu giàn tam giác (Truss)", "phonetic": "/trʌs ˈstrʌktʃər/", "definition": "Hệ khung gồm các thanh nối thành hình tam giác giúp phân tán lực đều khắp công trình.", "example": "Mái nhà và cầu thép luôn ứng dụng giàn tam giác."},
                {"term": "Lực nén (Compression)", "phonetic": "/kəmˈprɛʃən/", "definition": "Lực tác dụng ép các phân tử vật liệu lại gần nhau hơn.", "example": "Các trụ cầu chịu lực nén cực lớn từ trọng lượng xe cộ."},
                {"term": "Lực kéo (Tension)", "phonetic": "/ˈtɛnʃən/", "definition": "Lực tác dụng kéo giãn vật liệu ra xa nhau.", "example": "Dây cáp của cầu treo chịu lực kéo căng liên tục."},
                {"term": "Tải trọng tới hạn", "phonetic": "/ˈkrɪtɪkəl loʊd/", "definition": "Khối lượng tối đa mà kết cấu chịu được trước khi bị gãy hoặc sụp đổ.", "example": "Cây cầu que kem chịu được vật nặng tối đa 2kg."}
            ]
            matching = [
                {"term": "Hình tam giác", "definition": "Hình học ổn định nhất, không bị biến dạng góc"},
                {"term": "Trụ cầu thẳng đứng", "definition": "Chịu lực nén ép từ trên xuống dưới"},
                {"term": "Dây cáp treo cầu", "definition": "Chịu lực kéo căng hai đầu"},
                {"term": "Mấu nối keo dán", "definition": "Điểm liên kết phân tán tải trọng giữa các thanh"}
            ]
            sequencing = [
                {"stepNumber": 1, "text": "Đọc yêu cầu độ dài nhịp cầu (30cm) và tải trọng tối thiểu (500g)"},
                {"stepNumber": 2, "text": "Vẽ bản vẽ kỹ thuật giàn tam giác tỷ lệ 1:1 lên giấy kẻ ô"},
                {"stepNumber": 3, "text": "Dán các que kem theo từng cụm tam giác trên mặt phẳng bản vẽ"},
                {"stepNumber": 4, "text": "Dựng 2 mặt giàn cầu và liên kết mặt sàn cầu bằng thanh giằng chéo"},
                {"stepNumber": 5, "text": "Đặt vật nặng thử tải ở giữa cầu, ghi nhận tải trọng tới hạn khi cầu sập"}
            ]
            cloze = [
                {
                    "sentence": "Hình học có khả năng chống biến dạng chịu lực tốt nhất trong kiến trúc cầu đường là [...].",
                    "options": ["hình tam giác", "hình chữ nhật", "hình thoi"],
                    "answer": "hình tam giác",
                    "explanation": "Hình tam giác có 3 cạnh cố định góc, không thể xô lệch khi bị ép."
                },
                {
                    "sentence": "Hiệu suất của cây cầu mô hình được đánh giá qua tỷ số giữa [...] và khối lượng bản thân cầu.",
                    "options": ["tải trọng chịu được", "chiều dài mặt cầu", "số lượng que kem"],
                    "answer": "tải trọng chịu được",
                    "explanation": "Tỷ số Strength-to-Weight Ratio = Tải trọng chịu được / Khối lượng cầu."
                }
            ]
        elif cat == "energy":
            flashcards = [
                {"term": "Quang điện (Photovoltaic)", "phonetic": "/ˌfoʊtoʊvɑːlˈteɪɪk/", "definition": "Hiện tượng biến đổi trực tiếp ánh sáng mặt trời thành dòng điện một chiều.", "example": "Tấm pin mặt trời hấp thụ photon ánh sáng."},
                {"term": "Năng lượng tái tạo", "phonetic": "/rɪˈnuːəbəl ˈɛnərdʒi/", "definition": "Nguồn năng lượng thiên nhiên liên tục tự bổ sung, không bao giờ cạn kiệt.", "example": "Nắng, gió và sóng biển là năng lượng sạch."},
                {"term": "Công suất điện", "phonetic": "/ɪˈlɛktrɪkəl ˈpaʊər/", "definition": "Tốc độ tiêu thụ hoặc sản sinh điện năng trong một đơn vị thời gian (Watt).", "example": "P = U * I đo hiệu năng tấm pin."},
                {"term": "Góc nghiêng đón sáng", "phonetic": "/ˈtɪlt ˈæŋɡəl/", "definition": "Góc đặt tấm pin vuông góc với tia nắng để thu nhận năng lượng tối đa.", "example": "Điều chỉnh góc pin theo mùa trong năm."}
            ]
            matching = [
                {"term": "Tấm pin mặt trời", "definition": "Chuyển quang năng thành điện năng"},
                {"term": "Tua-bin gió", "definition": "Chuyển động năng của gió thành điện năng"},
                {"term": "Đồng hồ đo Vôn/Ampe", "definition": "Đo hiệu điện thế và dòng điện sinh ra"},
                {"term": "Bộ tích điện (Pin sạc)", "definition": "Lưu trữ điện năng để dùng ban đêm"}
            ]
            sequencing = [
                {"stepNumber": 1, "text": "Khảo sát vị trí và cường độ ánh sáng mặt trời tại khu vực thử nghiệm"},
                {"stepNumber": 2, "text": "Thiết kế giá đỡ có khớp xoay điều chỉnh góc nghiêng của tấm pin"},
                {"stepNumber": 3, "text": "Nối dây điện từ tấm pin vào đồng hồ đo vạn năng và mô tơ mini"},
                {"stepNumber": 4, "text": "Thay đổi các góc đón sáng khác nhau và ghi chép hiệu điện thế U, dòng điện I"},
                {"stepNumber": 5, "text": "Tính công suất P = U * I và xác định góc nghiêng tối ưu nhất"}
            ]
            cloze = [
                {
                    "sentence": "Tấm pin năng lượng mặt trời biến đổi trực tiếp [...] thành điện năng.",
                    "options": ["quang năng (ánh sáng)", "nhiệt năng của lửa", "hóa năng của pin"],
                    "answer": "quang năng (ánh sáng)",
                    "explanation": "Hiệu ứng quang điện biến đổi các hạt photon ánh sáng thành dòng electron."
                },
                {
                    "sentence": "Công suất điện sinh ra từ tấm pin mặt trời được tính theo công thức [...].",
                    "options": ["P = U * I", "P = U / I", "P = s / t"],
                    "answer": "P = U * I",
                    "explanation": "Công suất P (Watt) = Hiệu điện thế U (Volt) * Cường độ dòng điện I (Ampe)."
                }
            ]
        else:
            flashcards = [
                {"term": "Quy trình thiết kế kỹ thuật (EDP)", "phonetic": "/ˌɛndʒɪˈnɪərɪŋ dɪˈzaɪn/", "definition": "Chu trình 5 bước lặp đi lặp lại để tìm ra giải pháp tối ưu cho một bài toán.", "example": "Hỏi ➔ Tưởng tượng ➔ Lập kế hoạch ➔ Chế tạo ➔ Thử nghiệm & Cải tiến."},
                {"term": "Mô hình thử nghiệm (Prototype)", "phonetic": "/ˈproʊtəˌtaɪp/", "definition": "Mẫu sản phẩm thực nghiệm đầu tiên dùng để kiểm tra tính khả thi của ý tưởng.", "example": "Chế tạo mô hình ban đầu bằng bìa carton và que gỗ."},
                {"term": "Ràng buộc kỹ thuật (Constraint)", "phonetic": "/kənˈstreɪnt/", "definition": "Các giới hạn về vật liệu, thời gian, chi phí hoặc kích thước phải tuân thủ.", "example": "Giới hạn thời gian hoàn thành trong 90 phút."},
                {"term": "Tiêu chí thành công (Criteria)", "phonetic": "/kraɪˈtɪəriə/", "definition": "Các tiêu chuẩn định lượng bắt buộc sản phẩm phải đạt được khi nghiệm thu.", "example": "Sản phẩm phải chịu được tải trọng hoặc di chuyển được quãng đường yêu cầu."}
            ]
            matching = [
                {"term": "Hỏi & Khảo sát", "definition": "Làm rõ yêu cầu đề bài và ràng buộc kỹ thuật"},
                {"term": "Lập kế hoạch", "definition": "Vẽ phác thảo bản vẽ chi tiết kèm số đo"},
                {"term": "Chế tạo mô hình", "definition": "Cắt ghép vật liệu theo đúng bản thiết kế"},
                {"term": "Thử nghiệm & Cải tiến", "definition": "Đo đạc số liệu và khắc phục các điểm yếu"}
            ]
            sequencing = [
                {"stepNumber": 1, "text": "Bước 1: Hỏi (Ask) - Làm rõ vấn đề và các ràng buộc kỹ thuật"},
                {"stepNumber": 2, "text": "Bước 2: Tưởng tượng (Imagine) - Động não nhiều ý tưởng thiết kế khác nhau"},
                {"stepNumber": 3, "text": "Bước 3: Lập kế hoạch (Plan) - Vẽ phác thảo chi tiết và chọn vật liệu"},
                {"stepNumber": 4, "text": "Bước 4: Chế tạo (Create) - Lắp ráp mô hình mẫu thử nghiệm đầu tiên"},
                {"stepNumber": 5, "text": "Bước 5: Cải tiến (Improve) - Thử nghiệm, phân tích lỗi và hoàn thiện"}
            ]
            cloze = [
                {
                    "sentence": "Bước đầu tiên trong quy trình thiết kế kỹ thuật STEM là [...].",
                    "options": ["Hỏi và xác định vấn đề", "Mua vật liệu đắt nhất", "Bỏ qua thử nghiệm"],
                    "answer": "Hỏi và xác định vấn đề",
                    "explanation": "Quy trình EDP luôn khởi đầu bằng việc làm rõ mục tiêu và ràng buộc."
                },
                {
                    "sentence": "Mẫu sản phẩm thực nghiệm đầu tiên dùng để kiểm tra ý tưởng được gọi là [...].",
                    "options": ["mô hình mẫu (prototype)", "sản phẩm thương mại", "bản nháp bỏ đi"],
                    "answer": "mô hình mẫu (prototype)",
                    "explanation": "Prototype là bản thử nghiệm để đánh giá và cải tiến liên tục."
                }
            ]
    else:
        flashcards = [
            {"term": "Elastic Potential Energy", "phonetic": "/ɪˈlæstɪk pəˈtɛnʃəl/", "definition": "Energy stored in an object when it is temporarily deformed (stretched or compressed).", "example": "Winding a rubber band stores potential energy."},
            {"term": "Kinetic Energy", "phonetic": "/kɪˈnɛtɪk ˈɛnərdʒi/", "definition": "Energy that an object possesses by virtue of its motion.", "example": "The faster the vehicle moves, the greater its kinetic energy."},
            {"term": "Friction Force", "phonetic": "/ˈfrɪkʃən fɔːrs/", "definition": "Resistance force encountered when one surface moves across another.", "example": "Rubber treads improve tire traction on the track."},
            {"term": "Engineering Design Process (EDP)", "phonetic": "/ˌɛndʒɪˈnɪərɪŋ dɪˈzaɪn/", "definition": "A series of steps engineers use to guide them in problem-solving.", "example": "Ask -> Imagine -> Plan -> Create -> Test & Improve."}
        ]
        matching = [
            {"term": "Rubber band", "definition": "Stores elastic potential energy"},
            {"term": "Rotating axle", "definition": "Transmits mechanical torque to wheels"},
            {"term": "Rubber tread", "definition": "Increases friction grip and traction"},
            {"term": "Straw bushing", "definition": "Minimizes axle contact friction"}
        ]
        sequencing = [
            {"stepNumber": 1, "text": "Define the challenge constraints and review available tools"},
            {"stepNumber": 2, "text": "Brainstorm and sketch initial design configurations"},
            {"stepNumber": 3, "text": "Draft a dimensioned blueprint with precise wheel spacing"},
            {"stepNumber": 4, "text": "Assemble chassis, axle bushings, and wheels"},
            {"stepNumber": 5, "text": "Test performance on designated track, measure distance, and iterate"}
        ]
        cloze = [
            {
                "sentence": "Winding a rubber band around an axle converts manual work into [...].",
                "options": ["elastic potential energy", "thermal radiation", "magnetic flux"],
                "answer": "elastic potential energy",
                "explanation": "Stretching polymer chains stores elastic potential energy."
            },
            {
                "sentence": "Average velocity is calculated by dividing distance by [...].",
                "options": ["time", "mass", "acceleration"],
                "answer": "time",
                "explanation": "Velocity equals displacement divided by elapsed time."
            }
        ]

    return {
        "flashcards": flashcards,
        "matching": matching,
        "sequencing": sequencing,
        "cloze": cloze
    }

def create_diversified_quiz(topic_name, title, lang):
    cat = get_topic_category(topic_name)
    is_vie = (lang == "VIE")

    if is_vie:
        if cat == "mechanics":
            q1 = {
                "type": "multiple_choice",
                "badge": "🎯 Trắc nghiệm Nguyên lý",
                "question": f"Khi quấn căng dây cao su của {title}, bạn đang tích trữ dạng năng lượng nào để chuẩn bị chuyển động?",
                "options": ["Động năng trực tiếp", "Thế năng đàn hồi", "Năng lượng hóa học", "Năng lượng nhiệt"],
                "answer": "Thế năng đàn hồi",
                "explanation": "Công cơ học do tay xoay trục làm biến dạng đàn hồi dây cao su, tích lũy thành thế năng đàn hồi."
            }
            q2 = {
                "type": "true_false",
                "badge": "⚖️ Nhận định Đúng / Sai",
                "question": "Nhận định sau ĐÚNG hay SAI: 'Để xe chạy được nhanh và xa nhất, bề mặt tiếp xúc giữa bánh xe với mặt sàn cần phải nhẵn bóng hoàn toàn và có ma sát bằng 0'?",
                "options": ["Đúng (True)", "Sai (False)"],
                "answer": "Sai (False)",
                "explanation": "Sai! Nếu ma sát giữa bánh xe và sàn bằng 0, bánh xe sẽ trượt quay tít tại chỗ mà không có lực bám để đẩy xe tiến lên."
            }
            q3 = {
                "type": "troubleshooting",
                "badge": "🔧 Khắc phục Sự cố Kỹ thuật",
                "question": "Tình huống: Khi thả xe trên đường đua, bạn nhận thấy bánh sau quay rất nhanh nhưng xe bị trượt bánh tại chỗ không thể tiến lên. Đâu là biện pháp kỹ thuật tối ưu nhất?",
                "options": [
                    "Bọc thêm các vòng dây cao su quanh vành bánh xe để tăng độ bám đường",
                    "Bôi dầu mỡ bôi trơn lên bề mặt ngoài của bánh xe",
                    "Gắn thêm một vật nặng 2kg lên đầu xe",
                    "Cắt ngắn bớt chiều dài trục xe lại"
                ],
                "answer": "Bọc thêm các vòng dây cao su quanh vành bánh xe để tăng độ bám đường",
                "explanation": "Bọc cao su giúp tăng hệ số ma sát nghỉ giữa bánh xe và mặt sàn, ngăn hiện tượng trượt quay khi mô men xoắn nhả ra đột ngột."
            }
            q4 = {
                "type": "calculation",
                "badge": "🧮 Ứng dụng Tính toán Thực nghiệm",
                "question": "Trong một lượt chạy thử nghiệm, chiếc xe đua hoàn thành quãng đường s = 4.8 mét trong khoảng thời gian t = 2.4 giây. Vận tốc trung bình của xe là bao nhiêu?",
                "options": ["2.0 m/s", "1.2 m/s", "11.5 m/s", "0.5 m/s"],
                "answer": "2.0 m/s",
                "explanation": "Áp dụng công thức v = s / t = 4.8 / 2.4 = 2.0 m/s."
            }
        elif cat == "structural":
            q1 = {
                "type": "multiple_choice",
                "badge": "🎯 Trắc nghiệm Nguyên lý",
                "question": f"Tại sao các kỹ sư kết cấu luôn ưu tiên sử dụng hình tam giác trong thiết kế {title}?",
                "options": [
                    "Hình tam giác có góc cố định vững chắc, không thể bị biến dạng khi chịu nén",
                    "Hình tam giác nhìn đẹp mắt và tốn ít que kem nhất",
                    "Hình tam giác triệt tiêu hoàn toàn lực hấp dẫn của Trái Đất",
                    "Hình tam giác làm cây cầu nặng hơn"
                ],
                "answer": "Hình tam giác có góc cố định vững chắc, không thể bị biến dạng khi chịu nén",
                "explanation": "Tam giác là hình học cứng vững nhất trong cơ học kết cấu; 3 cạnh khóa chặt 3 góc phân tán tải trọng đều đặn."
            }
            q2 = {
                "type": "true_false",
                "badge": "⚖️ Nhận định Đúng / Sai",
                "question": "Nhận định sau ĐÚNG hay SAI: 'Một cây cầu tốt trong tiêu chuẩn kỹ thuật không chỉ chịu được tải trọng lớn mà còn phải có trọng lượng bản thân nhẹ nhất có thể'?",
                "options": ["Đúng (True)", "Sai (False)"],
                "answer": "Đúng (True)",
                "explanation": "Đúng! Trong kỹ thuật xây dựng hiện đại, tỷ số Strength-to-Weight Ratio càng cao thì công trình càng hiệu quả và tiết kiệm vật liệu."
            }
            q3 = {
                "type": "troubleshooting",
                "badge": "🔧 Khắc phục Sự cố Kỹ thuật",
                "question": "Tình huống: Khi đặt vật thử tải ở giữa cầu, phần giữa nhịp cầu bị oằn võng xuống nghiêm trọng và các mối nối que kem có nguy cơ bung keo. Bạn nên cải tiến thế nào?",
                "options": [
                    "Bổ sung các thanh giằng chéo tạo thành mạng lưới giàn tam giác phân tán lực sang 2 mố cầu",
                    "Tháo bớt các thanh gỗ ở đáy cầu ra cho nhẹ",
                    "Dán keo trực tiếp mố cầu vào mép bàn thí nghiệm",
                    "Đổ nước lên thân cầu để làm mát keo"
                ],
                "answer": "Bổ sung các thanh giằng chéo tạo thành mạng lưới giàn tam giác phân tán lực sang 2 mố cầu",
                "explanation": "Thanh giằng chéo (cross-bracing) chuyển lực nén thẳng đứng thành lực dọc theo các thanh tam giác truyền về 2 mố cầu."
            }
            q4 = {
                "type": "calculation",
                "badge": "🧮 Ứng dụng Tính toán Thực nghiệm",
                "question": "Một cây cầu mô hình nặng 50 gam có khả năng nâng đỡ vật nặng tối đa 2500 gam trước khi sụp đổ. Tỷ số chịu tải (Strength-to-Weight Ratio) của cây cầu này là bao nhiêu?",
                "options": ["50 lần", "125 lần", "25 lần", "2550 lần"],
                "answer": "50 lần",
                "explanation": "Tỷ số chịu tải = 2500g / 50g = 50 lần. Nghĩa là cầu chịu được vật nặng gấp 50 lần trọng lượng của chính nó."
            }
        elif cat == "energy":
            q1 = {
                "type": "multiple_choice",
                "badge": "🎯 Trắc nghiệm Nguyên lý",
                "question": f"Thiết bị nào trong bài {title} thực hiện nhiệm vụ biến đổi trực tiếp năng lượng ánh sáng thành dòng điện một chiều?",
                "options": [
                    "Tấm pin quang điện (Solar Photovoltaic Cell)",
                    "Cối xay gió đón gió",
                    "Máy biến áp cuộn dây",
                    "Điện trở nhiệt"
                ],
                "answer": "Tấm pin quang điện (Solar Photovoltaic Cell)",
                "explanation": "Tế bào quang điện bán dẫn hấp thụ hạt photon ánh sáng để giải phóng electron tạo dòng điện."
            }
            q2 = {
                "type": "true_false",
                "badge": "⚖️ Nhận định Đúng / Sai",
                "question": "Nhận định sau ĐÚNG hay SAI: 'Tấm pin năng lượng mặt trời sinh ra điện năng cao nhất khi tia sáng mặt trời chiếu song song với bề mặt tấm pin'?",
                "options": ["Đúng (True)", "Sai (False)"],
                "answer": "Sai (False)",
                "explanation": "Sai! Tấm pin đạt hiệu suất tối đa khi tia sáng chiếu thẳng góc vuông (90 độ) vào bề mặt tế bào quang điện."
            }
            q3 = {
                "type": "troubleshooting",
                "badge": "🔧 Khắc phục Sự cố Kỹ thuật",
                "question": "Tình huống: Khi đưa mô hình năng lượng mặt trời ra ngoài sân nắng, đồng hồ vạn năng đo được hiệu điện thế nhưng mô tơ quạt vẫn không quay. Nguyên nhân kỹ thuật nào có khả năng nhất?",
                "options": [
                    "Cường độ dòng điện (Ampe) sinh ra chưa đủ lớn để thắng ma sát khởi động của mô tơ",
                    "Ánh sáng mặt trời quá sáng làm mô tơ bị chói",
                    "Dây điện bị đảo ngược từ trường Trái Đất",
                    "Không khí ngoài trời quá nóng"
                ],
                "answer": "Cường độ dòng điện (Ampe) sinh ra chưa đủ lớn để thắng ma sát khởi động của mô tơ",
                "explanation": "Mô tơ cần cả điện áp đủ lớn và dòng điện đủ mạnh để tạo ra mô men từ trường khởi động rotor."
            }
            q4 = {
                "type": "calculation",
                "badge": "🧮 Ứng dụng Tính toán Thực nghiệm",
                "question": "Đồng hồ đo được trên tấm pin mặt trời ghi nhận hiệu điện thế U = 3.0 Vôn và cường độ dòng điện I = 0.5 Ampe. Công suất điện P của tấm pin đạt được là bao nhiêu?",
                "options": ["1.5 Watt", "6.0 Watt", "3.5 Watt", "0.17 Watt"],
                "answer": "1.5 Watt",
                "explanation": "Áp dụng công thức P = U * I = 3.0 * 0.5 = 1.5 Watt."
            }
        else:
            q1 = {
                "type": "multiple_choice",
                "badge": "🎯 Trắc nghiệm Nguyên lý",
                "question": f"Trong quy trình thiết kế kỹ thuật (EDP) khi thực hiện {title}, bước nào giúp bạn hiện thực hóa ý tưởng từ bản vẽ thành mô hình thực tế?",
                "options": [
                    "Bước Chế tạo mô hình mẫu (Create)",
                    "Bước Hỏi và khảo sát (Ask)",
                    "Bước Nghiệm thu báo cáo",
                    "Bước Mua sắm dụng cụ"
                ],
                "answer": "Bước Chế tạo mô hình mẫu (Create)",
                "explanation": "Bước Chế tạo (Create) là giai đoạn lắp ráp mẫu thử nghiệm thực tế theo bản vẽ thiết kế."
            }
            q2 = {
                "type": "true_false",
                "badge": "⚖️ Nhận định Đúng / Sai",
                "question": "Nhận định sau ĐÚNG hay SAI: 'Nếu mô hình thử nghiệm lần đầu tiên bị thất bại hoặc gãy vỡ, toàn bộ dự án coi như bỏ đi và không có giá trị học tập'?",
                "options": ["Đúng (True)", "Sai (False)"],
                "answer": "Sai (False)",
                "explanation": "Sai! Trong STEM, thất bại thực nghiệm là cơ hội vàng để phân tích nguyên nhân hư hỏng và tìm ra phương án cải tiến tối ưu."
            }
            q3 = {
                "type": "troubleshooting",
                "badge": "🔧 Khắc phục Sự cố Kỹ thuật",
                "question": "Tình huống: Khi kiểm tra mô hình kỹ thuật, sản phẩm của nhóm bạn không đạt một trong các tiêu chí kiểm tra bắt buộc. Thái độ và hành động chuẩn mực của một kỹ sư là gì?",
                "options": [
                    "Ghi chép chính xác điểm lỗi, cùng nhóm tìm nguyên nhân gốc rễ và sửa đổi thiết kế",
                    "Giấu số liệu sai đi và ghi kết quả giả vào báo cáo",
                    "Đổ lỗi cho vật liệu của giáo viên",
                    "Bỏ cuộc không làm tiếp"
                ],
                "answer": "Ghi chép chính xác điểm lỗi, cùng nhóm tìm nguyên nhân gốc rễ và sửa đổi thiết kế",
                "explanation": "Đạo đức kỹ thuật đòi hỏi tính trung thực khoa học, lấy số liệu thực tế làm cơ sở cải tiến giải pháp."
            }
            q4 = {
                "type": "calculation",
                "badge": "🧮 Ứng dụng Tính toán Thực nghiệm",
                "question": "Một nhóm học sinh đặt mục tiêu chế tạo mô hình đạt hiệu suất lý thuyết 100 điểm. Khi thử nghiệm thực tế, mô hình đạt được 85 điểm. Tỷ lệ hiệu suất đạt được là bao nhiêu phần trăm?",
                "options": ["85%", "15%", "185%", "1.17%"],
                "answer": "85%",
                "explanation": "Hiệu suất = (85 / 100) * 100% = 85%."
            }
    else:
        q1 = {
            "type": "multiple_choice",
            "badge": "🎯 Scientific Principle",
            "question": f"What fundamental energy transformation takes place in {title}?",
            "options": [
                "Elastic potential energy converts into kinetic energy",
                "Chemical energy turns into nuclear energy",
                "Electrical energy disappears completely",
                "Thermal energy creates gravity"
            ],
            "answer": "Elastic potential energy converts into kinetic energy",
            "explanation": "Stored potential energy is released and converted into motion energy (kinetic energy)."
        }
        q2 = {
            "type": "true_false",
            "badge": "⚖️ True / False Analysis",
            "question": "Statement TRUE or FALSE: 'In real-world engineering, friction between wheels and the track surface is completely unnecessary and should be zero'?",
            "options": ["True", "False"],
            "answer": "False",
            "explanation": "False! Without static friction between wheels and the floor, wheels would spin in place with zero traction."
        }
        q3 = {
            "type": "troubleshooting",
            "badge": "🔧 Engineering Troubleshooting",
            "question": "Scenario: Upon release, the wheels spin rapidly in place without moving forward. What is the most effective engineering solution?",
            "options": [
                "Wrap rubber bands around the outer rims to increase track traction",
                "Apply lubricant oil on the tire tread",
                "Remove all axles from the vehicle",
                "Place a 5kg weight on the chassis"
            ],
            "answer": "Wrap rubber bands around the outer rims to increase track traction",
            "explanation": "Rubber rims dramatically enhance friction grip, allowing the torque to propel the vehicle forward."
        }
        q4 = {
            "type": "calculation",
            "badge": "🧮 Empirical Calculation",
            "question": "A model prototype travels a measured distance of s = 6.0 meters in t = 2.0 seconds. What is its average velocity?",
            "options": ["3.0 m/s", "12.0 m/s", "0.33 m/s", "4.0 m/s"],
            "answer": "3.0 m/s",
            "explanation": "v = s / t = 6.0 / 2.0 = 3.0 m/s."
        }

    return [q1, q2, q3, q4]

def create_discussion_qa(topic_name, title, lang):
    cat = get_topic_category(topic_name)
    is_vie = (lang == "VIE")

    if is_vie:
        if cat == "mechanics":
            return [
                {
                    "question": "Điều gì xảy ra khi bạn xoắn dây cao su nhiều vòng hơn? Có giới hạn vật lý nào cho số vòng xoắn không?",
                    "answer": "Khi quấn nhiều vòng hơn, độ biến dạng đàn hồi tăng lên giúp tích lũy thế năng lớn hơn (Ep = 1/2*k*Δl²), xe sẽ có nhiều năng lượng để chạy nhanh và xa hơn. Tuy nhiên có 2 giới hạn vật lý quan trọng: 1) Nếu xoắn vượt quá giới hạn đàn hồi của cao su, các liên kết polymer sẽ bị đứt; 2) Nếu năng lượng nhả ra quá đột ngột, lực kéo vượt quá ma sát nghỉ cực đại của mặt đường làm bánh sau bị trượt quay tít tại chỗ thay vì chuyển động tịnh tiến."
                },
                {
                    "question": "Tại sao một số mô hình xe bị chạy quẹo vòng tròn thay vì chạy thẳng? Cách điều chỉnh góc đặt trục xe như thế nào?",
                    "answer": "Xe bị lệch hướng chủ yếu do 2 nguyên nhân kỹ thuật: 1) Trục trước và trục sau không song song tuyệt đối với nhau; 2) Lực ma sát ở 2 bên bánh xe không đều nhau (một bên bị kẹt chặt hơn bên kia). Cách khắc phục: Dùng thước vuông góc căn chỉnh lại 2 trục xe song song hoàn hảo với khung gầm và đảm bảo khe hở giữa bánh xe và ống lót ở cả 2 bên đều thông thoáng như nhau."
                },
                {
                    "question": "Nếu muốn xe chạy được quãng đường xa nhất có thể, bạn sẽ chọn bánh xe lớn hay bánh xe nhỏ? Phân tích ưu nhược điểm.",
                    "answer": "Bánh xe lớn có chu vi lớn hơn (C = π*d), do đó với cùng một số vòng quay của trục xe, bánh lớn sẽ đưa xe đi quãng đường dài hơn rất nhiều so với bánh nhỏ. Nhược điểm: Bánh lớn cần lực mô-men xoắn ban đầu mạnh hơn để khởi động và dễ bị đảo nếu không đồng tâm. Thiết kế tối ưu là dùng bánh xe đường kính lớn có trọng lượng nhẹ ở trục dẫn động và bánh nhỏ thanh thoát ở trục lái."
                },
                {
                    "question": "Theo em, sự khác biệt căn bản giữa một người thợ làm theo cảm tính và một kỹ sư thiết kế STEM nằm ở điểm nào?",
                    "answer": "Kỹ sư STEM không đoán mò mà luôn làm việc dựa trên dữ liệu định lượng: 1) Có bản vẽ kỹ thuật tỷ lệ trước khi làm; 2) Bấm giờ, đo quãng đường và tính toán vận tốc trung bình (v = s/t) sau mỗi lần thử; 3) Phân tích chính xác nguyên nhân lỗi (do ma sát trục, do thiếu độ bám bánh hay do lệch trọng tâm) và cải tiến có mục tiêu theo Quy trình Thiết kế Kỹ thuật (EDP)."
                }
            ]
        elif cat == "structural":
            return [
                {
                    "question": "Tại sao kết cấu giàn tam giác (Truss) lại chịu tải trọng tốt hơn rất nhiều so with kết cấu hình chữ nhật?",
                    "answer": "Hình tam giác là hình học cố định góc duy nhất trong tự nhiên: khi chiều dài 3 cạnh đã được cố định thì 3 góc không thể thay đổi mà không làm gãy hoặc kéo đứt một cạnh. Khi có tải trọng đè lên đỉnh tam giác, lực lập tức được phân tách thành 2 thành phần dọc theo 2 cạnh bên truyền đều xuống chân đế. Ngược lại, hình chữ nhật rất dễ bị xô lệch thành hình bình hành khi chịu lực tác dụng nghiêng."
                },
                {
                    "question": "Trong một cây cầu chịu tải trọng ở giữa nhịp, phần dầm nào chịu lực nén và phần nào chịu lực kéo?",
                    "answer": "Khi có vật nặng đè ở giữa cầu, dầm phía trên (Top Chord) sẽ bị uốn cong võng xuống, làm các phân tử vật liệu bị ép chặt lại gần nhau -> Chịu lực nén (Compression). Ngược lại, dầm dưới đáy (Bottom Chord) bị kéo căng giãn dài ra -> Chịu lực kéo (Tension). Các thanh giằng chéo ở giữa đóng vai trò truyền và cân bằng hai hệ lực này về các mố cầu ở hai đầu."
                },
                {
                    "question": "Làm thế nào để nâng cao tỷ số chịu tải (Strength-to-Weight Ratio) của cây cầu thay vì chỉ đắp thật nhiều que kem?",
                    "answer": "Tỷ số chịu tải = Tải trọng chịu được / Khối lượng cầu. Đắp quá nhiều que kem và keo dán thừa sẽ làm tăng trọng lượng bản thân cây cầu mà không làm tăng độ bền tương ứng. Kỹ sư tối ưu bằng cách: 1) Bố trí thanh chịu lực đúng theo hướng vector lực chính; 2) Dùng thanh kép ở các vị trí chịu nén cao; 3) Cắt gọt và chấm keo gọn gàng, để keo khô hoàn toàn trước khi thử tải."
                },
                {
                    "question": "Nếu cây cầu bị sập ở một vị trí cụ thể trong lần thử tải đầu tiên, kỹ sư sẽ rút ra bài học gì?",
                    "answer": "Kỹ sư sẽ ghi nhận vị trí gãy là 'Điểm yếu tập trung ứng suất' (Stress concentration point). Họ sẽ kiểm tra xem que kem tại đó bị gãy ngang do nén oằn (buckling) hay do bung mối nối keo (joint failure). Từ đó, họ cải tiến thiết kế bằng cách gia cố thêm thanh giằng chéo hoặc tăng diện tích tiếp xúc của mối dán tại đúng vị trí đó trong mẫu thử nghiệm tiếp theo."
                }
            ]
        elif cat == "energy":
            return [
                {
                    "question": "Góc nghiêng đón ánh sáng ảnh hưởng như thế nào đến công suất điện sinh ra từ tấm pin mặt trời?",
                    "answer": "Tấm pin mặt trời hấp thụ các hạt photon ánh sáng để giải phóng electron. Khi tia nắng chiếu vuông góc (90 độ) vào bề mặt tế bào quang điện, mật độ năng lượng ánh sáng trên một đơn vị diện tích là lớn nhất, sinh ra dòng điện cực đại. Khi góc chiếu bị nghiêng, diện tích đón sáng bị thu hẹp và một phần ánh sáng bị phản xạ ra ngoài, làm giảm đáng kể công suất điện (P = U * I)."
                },
                {
                    "question": "Tại sao trong các hệ thống điện mặt trời thực tế, người ta luôn cần bộ điều khiển sạc và bình ắc quy lưu trữ?",
                    "answer": "Năng lượng mặt trời có tính chất gián đoạn: cường độ thay đổi liên tục theo mây trời và hoàn toàn biến mất vào ban đêm. Bộ điều khiển sạc bảo vệ thiết bị không bị quá áp khi trời nắng gắt, đồng thời bình ắc quy giúp lưu trữ lượng điện dư thừa vào ban ngày để cung cấp nguồn điện ổn định, liên tục 24/7 cho các thiết bị sinh hoạt."
                },
                {
                    "question": "Đâu là những yếu tố tự nhiên làm suy giảm hiệu suất của tấm pin mặt trời ngoài trời và cách khắc phục?",
                    "answer": "1) Bụi bẩn và lá cây che khuất tế bào quang điện -> Cần vệ sinh bề mặt định kỳ; 2) Nhiệt độ môi trường quá cao làm giảm hiệu suất dẫn điện của chất bán dẫn silic -> Cần thiết kế khe thoáng khí làm mát phía sau tấm pin; 3) Góc bóng râm che một phần tấm pin -> Sử dụng các diode chặn (bypass diode) để tránh làm hỏng toàn bộ chuỗi tế bào."
                }
            ]
        else:
            return [
                {
                    "question": "Điểm khó khăn lớn nhất mà nhóm bạn gặp phải khi chế tạo mô hình là gì và các bạn đã khắc phục như thế nào?",
                    "answer": "Khó khăn thường gặp nhất là sai số kích thước khi gia công vật liệu thủ công bằng kéo và độ bền các mối dán chưa đồng đều. Cách khắc phục: Sử dụng bản vẽ dưỡng mẫu tỷ lệ 1:1, đo đạc cẩn thận 2 lần trước khi cắt và phân công chuyên môn hóa công việc cho từng thành viên trong nhóm."
                },
                {
                    "question": "Nếu có thêm thời gian và ngân sách vật liệu nâng cao, bạn sẽ cải tiến chi tiết nào của mô hình?",
                    "answer": "Sẽ thay thế bìa carton và que kem bằng vật liệu nhựa in 3D hoặc sợi carbon siêu nhẹ và cứng vững; thay thế các ống hút lót trục bằng vòng bi kim loại (ball bearings) để triệt tiêu ma sát quay; và thiết kế các mối ghép dạng ngàm chốt cơ khí tháo lắp nhanh thay vì chỉ dán keo cố định."
                },
                {
                    "question": "Làm thế nào để áp dụng bài học STEM này vào việc giải quyết một vấn đề thực tế trong đời sống hàng ngày?",
                    "answer": "Học sinh có thể vận dụng tư duy 5 bước EDP (Hỏi ➔ Tưởng tượng ➔ Kế hoạch ➔ Chế tạo ➔ Cải tiến) vào các dự án thực tiễn như: chế tạo hệ thống tự tưới cây từ chai nhựa bỏ đi, thiết kế thùng rác phân loại thông minh, làm giá đỡ máy tính bảng chống mỏi cổ hoặc sửa chữa các vật dụng hỏng hóc trong gia đình."
                },
                {
                    "question": "Tại sao việc ghi chép số liệu đo lường thực nghiệm trung thực lại là tiêu chuẩn đạo đức cao nhất của một kỹ sư?",
                    "answer": "Số liệu thực tế phản ánh đúng quy luật tự nhiên. Chỉ khi có số liệu trung thực, kỹ sư mới phát hiện được nguyên nhân hư hỏng thực sự của công trình và đưa ra phương án gia cố chuẩn xác. Việc làm giả hoặc giấu bớt số liệu sai có thể dẫn đến những thảm họa kỹ thuật nghiêm trọng khi sản phẩm được đưa vào sử dụng thực tế."
                }
            ]
    else:
        return [
            {
                "question": "What happens when you wind the rubber band more times? Are there physical limits?",
                "answer": "Winding the rubber band further increases elastic potential energy (Ep = 1/2*k*Δl²), providing more mechanical work to propel the racer faster. However, there are two physical limits: 1) Exceeding polymer elasticity will snap the rubber band; 2) Excessive sudden torque will exceed the tires' static friction, causing wheels to spin uselessly in place rather than translating into forward acceleration."
            },
            {
                "question": "Why do some vehicle prototypes veer off to the side instead of driving straight? How can you fix it?",
                "answer": "Veering is caused by non-parallel axles or uneven friction between the left and right wheels. Fix: Use a square ruler to align the front and rear axles perfectly perpendicular to the chassis centerline, and ensure both wheel hubs rotate with equal minimal resistance."
            },
            {
                "question": "How does an engineer differentiate themselves from a craft hobbyist when solving technical problems?",
                "answer": "Engineers rely on systematic empirical data rather than guesswork: dimensioned blueprints, controlled trials, quantitative metrics (velocity = distance / time), failure analysis, and iterative refinement following the formal Engineering Design Process (EDP)."
            }
        ]

def update_entire_curriculum_with_qa():
    with open("data.json", "r", encoding="utf-8") as f:
        dataset = json.load(f)

    total_lectures = 0
    for lvl in dataset:
        for lg in lvl["languages"]:
            lang = lg["lang"]
            for t in lg["topics"]:
                topic_name = t["topicName"]
                for lec in t["lectures"]:
                    title = lec.get("title", "STEM Lesson")
                    
                    # 1. Update practice & quiz
                    lec["thumbnailUrl"] = None
                    lec["media"] = None
                    lec["practiceData"] = create_diversified_practice(topic_name, title, lang)
                    lec["quizData"] = create_diversified_quiz(topic_name, title, lang)

                    # 2. Add rich Q&A with answers to lessonPlan
                    if "lessonPlan" in lec:
                        lec["lessonPlan"]["discussionQuestions"] = create_discussion_qa(topic_name, title, lang)

                    total_lectures += 1

    # Save to data.json
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)

    # Save to data.js
    js_content = "/**\n * E-Learning Resource Tree Mock Data with Rich Discussion Q&A and Diversified Practice/Assessments\n */\nwindow.APP_DATA = " + json.dumps(dataset, ensure_ascii=False, indent=2) + ";\n"
    with open("data.js", "w", encoding="utf-8") as f:
        f.write(js_content)

    print(f"Successfully updated all {total_lectures} lectures with full discussion questions and detailed answers.")

if __name__ == "__main__":
    update_entire_curriculum_with_qa()
