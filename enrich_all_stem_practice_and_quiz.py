#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enrich STEM Practice & Test modules across all 450 lessons with
rigorous, authentic technical, mathematical, and physics content.
"""

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

# Full Master Specifications for 12 Domains in VIE & ENG
MASTER_SPECS = {
    "aerospace": {
        "vie": {
            "law_name": "Định luật Bernoulli & Khí động học",
            "formula": "L = (1/2) · ρ · v² · S · Cl",
            "formula_unit": "N (Newton)",
            "mech": "Biên dạng cánh & Cánh tà ổn định (Airfoil & Elevator)",
            "metric": "Tỷ số Lực nâng/Lực cản (L/D) ≥ 6.0",
            "matching": [
                {"term": "L = (1/2) · ρ · v² · S · Cl", "definition": "Công thức tính lực nâng khí động học theo vận tốc và diện tích cánh"},
                {"term": "Định luật III Newton", "definition": "Cánh đẩy luồng khí xuống dưới tạo phản lực nâng cánh lên trên"},
                {"term": "Đơn vị Newton (N)", "definition": "Đơn vị đo lực nâng (Lift) và lực cản (Drag) trong hệ SI"},
                {"term": "Tỷ số L/D (Glide Ratio)", "definition": "Đại lượng đo lường hiệu suất lướt xa của tàu lượn từ một độ cao xác định"}
            ],
            "cloze": [
                {"text": "Theo định luật Bernoulli, luồng khí trên mặt cong của cánh di chuyển nhanh hơn, tạo ra vùng [áp suất thấp] ở phía trên để sinh lực nâng.", "answer": "áp suất thấp", "options": ["áp suất thấp", "áp suất cao", "lực ma sát", "chân không"]},
                {"text": "Lực nâng khí động học tỉ lệ thuận với [bình phương] của vận tốc dòng khí thổi qua bề mặt cánh.", "answer": "bình phương", "options": ["bình phương", "căn bậc hai", "tỉ lệ nghịch", "bậc ba"]},
                {"text": "Để tàu lượn bay ổn định, trọng tâm (CG) của mô hình phải nằm [phía trước] tâm áp lực khí động (CP).", "answer": "phía trước", "options": ["phía trước", "phía sau", "tại đuôi", "ngoài cánh"]},
                {"text": "Khi góc tấn vượt quá ngưỡng giới hạn, luồng khí bị tách rời khỏi bề mặt cánh gây ra hiện tượng [thất tốc] khí động học.", "answer": "thất tốc", "options": ["thất tốc", "tăng tốc", "cộng hưởng", "triệt tiêu"]}
            ],
            "q_physics": {
                "badge": "⚛️ Vật lý & Nguyên lý Cơ chế",
                "question": "Theo nguyên lý Bernoulli và định luật III Newton, cơ chế vật lý nào trực tiếp tạo ra lực nâng (Lift) nâng đỡ cánh máy bay?",
                "options": [
                    "Vận tốc luồng khí mặt trên cánh lớn hơn mặt dưới, sinh ra vùng áp suất tĩnh thấp ở mặt trên kéo cánh lên",
                    "Khối lượng không khí bên dưới cánh luôn có nhiệt độ cao hơn không khí bên trên",
                    "Lực ma sát tiếp xúc giữa không khí và cánh triệt tiêu hoàn toàn trọng lực",
                    "Không khí bên trên cánh bị nén chặt lại đẩy cánh hướng xuống đất"
                ],
                "answer": "Vận tốc luồng khí mặt trên cánh lớn hơn mặt dưới, sinh ra vùng áp suất tĩnh thấp ở mặt trên kéo cánh lên",
                "explanation": "Độ cong của mặt trên cánh làm đường dòng khí lưu thông nhanh hơn, tạo áp suất tĩnh thấp hơn áp suất mặt dưới theo phương trình Bernoulli: p + 1/2·ρ·v² = hằng số. Chênh lệch áp suất này tạo lực nâng thẳng đứng."
            },
            "q_math": {
                "badge": "📐 Toán học Ứng dụng & Tính toán",
                "question": "Một tàu lượn mô hình có diện tích cánh S = 0.05 m², bay trong không khí (ρ = 1.2 kg/m³) với vận tốc v = 6.0 m/s. Biết hệ số lực nâng Cl = 0.8. Độ lớn lực nâng khí động học L là bao nhiêu?",
                "options": ["0.864 N", "1.728 N", "0.432 N", "2.160 N"],
                "answer": "0.864 N",
                "explanation": "Áp dụng công thức khí động học: L = (1/2) · ρ · v² · S · Cl = 0.5 × 1.2 × (6.0)² × 0.05 × 0.8 = 0.6 × 36 × 0.04 = 0.864 N."
            },
            "q_troubleshoot": {
                "badge": "🔧 Xử lý Sự cố Kỹ thuật",
                "question": "Trong thử nghiệm, mô hình tàu lượn liên tục bị chúi mũi đâm xuống đất ngay sau khi phóng (hiện tượng nose-heavy). Giải pháp kỹ thuật nào sau đây là chuẩn xác nhất?",
                "options": [
                    "Dời trọng tâm (CG) lùi về phía sau hoặc uốn cong nhẹ cánh thăng bằng đuôi ngang lên trên (Elevator Up)",
                    "Dán thêm vật nặng kim loại ở ngay đầu chóp mũi tàu lượn",
                    "Cắt ngắn chiều dài sải cánh chính để giảm diện tích nâng",
                    "Phóng tàu lượn với lực ném mạnh gấp ba lần"
                ],
                "answer": "Dời trọng tâm (CG) lùi về phía sau hoặc uốn cong nhẹ cánh thăng bằng đuôi ngang lên trên (Elevator Up)",
                "explanation": "Hiện tượng chúi mũi xảy ra khi trọng tâm (CG) nằm quá xa về phía trước so với tâm áp lực khí động (CP). Đưa trọng tâm lùi về sau hoặc tạo góc ngóc ở cánh đuôi ngang sẽ cân bằng mô-men quay dọc."
            },
            "q_materials": {
                "badge": "🔬 Khoa học Vật liệu & Kết cấu",
                "question": "Chỉ số cơ lý nào của vật liệu là quan trọng nhất khi chọn vật liệu chế tạo khung sườn và cánh máy bay?",
                "options": [
                    "Tỷ số giữa độ bền uốn trên khối lượng riêng (Strength-to-Weight Ratio) cao và khả năng chống vặn xoắn",
                    "Khối lượng riêng cực lớn để tăng quán tính rơi tự do",
                    "Tính dẫn điện cao để trung hòa tĩnh điện trong khí quyển",
                    "Vật liệu hoàn toàn dẻo mềm có thể biến dạng tự do theo gió"
                ],
                "answer": "Tỷ số giữa độ bền uốn trên khối lượng riêng (Strength-to-Weight Ratio) cao và khả năng chống vặn xoắn",
                "explanation": "Trong kỹ thuật hàng không, kết cấu phải đạt độ nhẹ tối đa để giảm trọng lực nâng nhưng phải cứng vững (stiffness) để giữ nguyên biên dạng khí động học dưới áp lực gió."
            },
            "q_data": {
                "badge": "📊 Phân tích Dữ liệu Thực nghiệm",
                "question": "Đo đạc thực nghiệm cho thấy: Khi tăng góc tấn từ 4° lên 10°, lực nâng tăng tuyến tính từ 0.5N lên 1.2N. Tuy nhiên, khi tăng tiếp lên 18°, lực nâng sụt giảm xuống 0.3N và lực cản tăng gấp ba. Hiện tượng này là gì?",
                "options": [
                    "Hiện tượng thất tốc khí động học (Stall) do dòng khí tách rời mặt cánh",
                    "Hiện tượng cộng hưởng cơ học tần số cao",
                    "Hiện tượng siêu âm phá vỡ rào cản âm thanh",
                    "Hiện tượng mất trọng lực cục bộ"
                ],
                "answer": "Hiện tượng thất tốc khí động học (Stall) do dòng khí tách rời mặt cánh",
                "explanation": "Vượt quá góc tấn tới hạn (Critical Angle of Attack), luồng khí không thể bám vào mặt trên của cánh mà bị tách lớp tạo vùng xoáy hỗn loạn, làm triệt tiêu lực nâng và tăng đột biến lực cản (Stall)."
            }
        },
        "eng": {
            "law_name": "Bernoulli's Principle & Aerodynamics",
            "formula": "L = (1/2) · ρ · v² · S · Cl",
            "formula_unit": "N (Newton)",
            "mech": "Airfoil Camber & Stabilizer Trim Tab",
            "metric": "Lift-to-Drag Ratio (L/D) ≥ 6.0",
            "matching": [
                {"term": "L = (1/2) · ρ · v² · S · Cl", "definition": "Calculates aerodynamic lift force from flow velocity and wing area"},
                {"term": "Newton's Third Law", "definition": "Downward airflow deflection generates an equal and opposite upward lifting reaction"},
                {"term": "Newton (N)", "definition": "Standard SI unit measuring aerodynamic lift and aerodynamic drag forces"},
                {"term": "Glide Ratio (L/D)", "definition": "Measures horizontal forward distance achieved per unit of descent altitude"}
            ],
            "cloze": [
                {"text": "According to Bernoulli's principle, airflow accelerates over the cambered surface, generating a localized [low pressure] region above the wing.", "answer": "low pressure", "options": ["low pressure", "high pressure", "vacuum", "friction"]},
                {"text": "Aerodynamic lift is directly proportional to the [square] of airflow velocity.", "answer": "square", "options": ["square", "square root", "cube", "reciprocal"]},
                {"text": "For longitudinal flight stability, the Center of Gravity (CG) must reside [ahead of] the aerodynamic Center of Pressure (CP).", "answer": "ahead of", "options": ["ahead of", "behind", "at the tail", "under the wing"]},
                {"text": "Exceeding the critical angle of attack detaches the boundary layer airflow, triggering an aerodynamic [stall].", "answer": "stall", "options": ["stall", "acceleration", "resonance", "flotation"]}
            ],
            "q_physics": {
                "badge": "⚛️ Physics Principles & Mechanisms",
                "question": "According to Bernoulli's principle and Newton's Third Law, what physical mechanism directly produces aerodynamic lift on a cambered wing?",
                "options": [
                    "Air velocity over the curved upper surface exceeds lower surface velocity, lowering upper static pressure to draw the wing upward",
                    "Air underneath the wing is significantly warmer than air above the wing",
                    "Skin friction completely neutralizes the downward pull of gravity",
                    "Upper surface air compresses downward to force the airframe into the ground"
                ],
                "answer": "Air velocity over the curved upper surface exceeds lower surface velocity, lowering upper static pressure to draw the wing upward",
                "explanation": "The cambered profile forces streamlines over the upper surface to accelerate, reducing local static pressure in accordance with Bernoulli's theorem (p + 1/2·ρ·v² = const), creating net upward lift."
            },
            "q_math": {
                "badge": "📐 Applied Math & Calculation",
                "question": "A model glider has wing area S = 0.05 m² and glides through air (ρ = 1.2 kg/m³) at velocity v = 6.0 m/s. Given lift coefficient Cl = 0.8, calculate the lift force L:",
                "options": ["0.864 N", "1.728 N", "0.432 N", "2.160 N"],
                "answer": "0.864 N",
                "explanation": "Applying the lift equation: L = (1/2) · ρ · v² · S · Cl = 0.5 × 1.2 × (6.0)² × 0.05 × 0.8 = 0.6 × 36 × 0.04 = 0.864 N."
            },
            "q_troubleshoot": {
                "badge": "🔧 Engineering Troubleshooting",
                "question": "During test flights, a prototype glider persistently pitches down into the ground immediately after release. What is the correct engineering solution?",
                "options": [
                    "Shift the Center of Gravity (CG) slightly aft, or apply positive elevator trim up",
                    "Add metallic ballast directly onto the extreme tip of the nose",
                    "Shorten the wingspan to reduce lifting area",
                    "Throw the glider with triple the initial launch velocity"
                ],
                "answer": "Shift the Center of Gravity (CG) slightly aft, or apply positive elevator trim up",
                "explanation": "Nose-diving indicates a nose-heavy configuration where CG is too far forward of CP. Moving ballast aft or applying upward stabilizer deflection restores pitch equilibrium."
            },
            "q_materials": {
                "badge": "🔬 Materials & Structural Mechanics",
                "question": "Which material property is paramount when engineering lightweight aerodynamic lifting surfaces?",
                "options": [
                    "High strength-to-weight ratio combined with torsional flexural rigidity",
                    "Maximum bulk density to increase penetration inertia",
                    "High electrical conductivity to ground atmospheric static charges",
                    "Complete ductile elasticity that deforms freely under crosswinds"
                ],
                "answer": "High strength-to-weight ratio combined with torsional flexural rigidity",
                "explanation": "Aerospace airframes require minimal gravitational mass while resisting aeroelastic deformation and flutter under flight air loads."
            },
            "q_data": {
                "badge": "📊 Empirical Data Analysis",
                "question": "Wind tunnel data indicates that increasing angle of attack from 4° to 10° raises lift linearly from 0.5N to 1.2N, but at 18° lift drops sharply to 0.3N while drag surges threefold. What phenomenon occurred?",
                "options": [
                    "Aerodynamic Stall caused by boundary layer flow separation",
                    "Mechanical harmonic structural resonance",
                    "Supersonic shockwave formation",
                    "Localized micro-gravity pocket"
                ],
                "answer": "Aerodynamic Stall caused by boundary layer flow separation",
                "explanation": "Exceeding the critical angle of attack forces boundary layer air to detach from the suction surface into turbulent vortices, causing catastrophic loss of lift and surge in drag (Stall)."
            }
        }
    },
    "marine": {
        "vie": {
            "law_name": "Nguyên lý Ác-si-mét & Thủy tĩnh học",
            "formula": "Fb = ρ_chất lỏng · V_chìm · g",
            "formula_unit": "N (Newton)",
            "mech": "Khoang dằn & Vỏ thuyền dãn nước (Displacement Hull & Keel)",
            "metric": "Chiều cao tâm định vị (GM) > 0 (Ổn định chống lật)",
            "matching": [
                {"term": "Fb = ρ · V · g", "definition": "Lực đẩy Ác-si-mét bằng trọng lượng phần chất lỏng bị chiếm chỗ"},
                {"term": "Điều kiện nổi (P = Fb)", "definition": "Trọng lượng toàn phần của thuyền bằng lực đẩy nổi của nước"},
                {"term": "Đơn vị Pascal (Pa)", "definition": "Đơn vị đo áp suất thủy tĩnh tác dụng lên đáy thân vỏ thuyền"},
                {"term": "Mớn nước (Draft)", "definition": "Chiều sâu thẳng đứng từ mặt nước đến điểm thấp nhất của đáy thuyền"}
            ],
            "cloze": [
                {"text": "Một vật thể sẽ nổi ổn định trên mặt nước khi khối lượng riêng trung bình của nó [nhỏ hơn] khối lượng riêng của nước.", "answer": "nhỏ hơn", "options": ["nhỏ hơn", "lớn hơn", "bằng không", "gấp đôi"]},
                {"text": "Lực đẩy Ác-si-mét tác dụng lên thân thuyền tỉ lệ thuận với [thể tích] phần thân chìm trong nước.", "answer": "thể tích", "options": ["thể tích", "chiều cao", "vận tốc", "nhiệt độ"]},
                {"text": "Để tăng tính ổn định chống lật ngang của thuyền, kỹ sư cần bố trí hàng hóa để hạ thấp [trọng tâm] sát đáy thuyền.", "answer": "trọng tâm", "options": ["trọng tâm", "tâm nổi", "mạn thuyền", "cột buồm"]},
                {"text": "Áp suất thủy tĩnh của nước tác dụng lên thân tàu tỉ lệ thuận với [độ sâu] ngập nước theo công thức p = ρ·g·h.", "answer": "độ sâu", "options": ["độ sâu", "diện tích", "thời gian", "khối lượng"]}
            ],
            "q_physics": {
                "badge": "⚛️ Vật lý & Nguyên lý Cơ chế",
                "question": "Tại sao một con tàu bằng thép nặng hàng nghìn tấn có thể nổi trên mặt nước trong khi một hòn bi thép nhỏ lại chìm ngay lập tức?",
                "options": [
                    "Khoang rỗng của tàu làm tăng thể tích chiếm nước, đưa khối lượng riêng trung bình thấp hơn nước",
                    "Thép đóng tàu có mật độ phân tử nhẹ hơn bi thép thông thường",
                    "Sức căng bề mặt của nước biển giữ toàn bộ con tàu nổi lên",
                    "Chân vịt của tàu liên tục đẩy nước xuống dưới để tạo phản lực nâng"
                ],
                "answer": "Khoang rỗng của tàu làm tăng thể tích chiếm nước, đưa khối lượng riêng trung bình thấp hơn nước",
                "explanation": "Khi tàu có khoang rỗng, thể tích choán nước V rất lớn. Lực đẩy Ác-si-mét Fb = ρ·V·g cân bằng với trọng lượng P = m·g của toàn tàu, giúp tàu nổi thăng bằng."
            },
            "q_math": {
                "badge": "📐 Toán học Ứng dụng & Tính toán",
                "question": "Một mô hình thuyền có thể tích khoang chìm tối đa V = 0.0005 m³ (500 mL). Khối lượng riêng của nước ρ = 1000 kg/m³, g = 9.8 m/s². Tính lực đẩy Ác-si-mét cực đại Fb tác dụng lên thuyền:",
                "options": ["4.90 N", "9.80 N", "2.45 N", "0.50 N"],
                "answer": "4.90 N",
                "explanation": "Áp dụng định luật Ác-si-mét: Fb = ρ · V · g = 1000 kg/m³ × 0.0005 m³ × 9.8 m/s² = 4.90 N."
            },
            "q_troubleshoot": {
                "badge": "🔧 Xử lý Sự cố Kỹ thuật",
                "question": "Trong thử nghiệm tải trọng, thuyền có xu hướng bị lật nghiêng sang một bên khi chất thêm hàng. Giải pháp kỹ thuật nào sau đây giải quyết triệt để lỗi mất ổn định ngang này?",
                "options": [
                    "Hạ thấp trọng tâm hàng hóa xuống đáy thuyền và mở rộng bề ngang thân thuyền (Beam width)",
                    "Xếp hàng hóa lên cao trên boong thuyền để dễ quan sát",
                    "Gọt nhọn đáy thuyền thành hình tam giác hẹp",
                    "Giảm bớt chiều dài của thuyền"
                ],
                "answer": "Hạ thấp trọng tâm hàng hóa xuống đáy thuyền và mở rộng bề ngang thân thuyền (Beam width)",
                "explanation": "Ổn định ngang đòi hỏi tâm định vị (Metacenter) nằm trên trọng tâm (CG). Hạ hàng xuống đáy làm giảm độ cao trọng tâm, trong khi mở rộng thân thuyền làm tăng mô-men hồi phục chống nghiêng."
            },
            "q_materials": {
                "badge": "🔬 Khoa học Vật liệu & Kết cấu",
                "question": "Vật liệu làm vỏ và gioăng chống thấm trong các thiết bị hoạt động dưới nước cần đạt tiêu chuẩn kỹ thuật nào?",
                "options": [
                    "Kỵ nước (Hydrophobic), chống ăn mòn hóa học và chịu được chu kỳ áp suất thủy tĩnh",
                    "Độ xốp bọt khí mở để hấp thụ nước vào trong thân",
                    "Tính hòa tan sinh học nhanh chóng khi gặp muối biển",
                    "Dẫn nhiệt cực nhanh để hạ nhiệt động cơ"
                ],
                "answer": "Kỵ nước (Hydrophobic), chống ăn mòn hóa học và chịu được chu kỳ áp suất thủy tĩnh",
                "explanation": "Vật liệu hàng hải đòi hỏi tính trơ hóa học, không bị trương nở hay giòn gãy dưới tác động của nước và chịu được áp lực thủy tĩnh liên tục mà không rò rỉ."
            },
            "q_data": {
                "badge": "📊 Phân tích Dữ liệu Thực nghiệm",
                "question": "Thực nghiệm cho thấy: Khi đặt thêm 100g hàng, mớn nước (độ chìm) tăng thêm 1.2 cm; khi thêm 200g, tăng 2.4 cm; khi thêm 300g, tăng 3.6 cm. Kết luận khoa học nào chuẩn xác?",
                "options": [
                    "Độ chìm mớn nước tỉ lệ thuận tuyến tính với khối lượng tải trọng đặt lên thuyền",
                    "Độ chìm tăng theo hàm số mũ bậc hai so với khối lượng",
                    "Lực đẩy Ác-si-mét giảm dần khi chất thêm hàng",
                    "Thuyền sẽ tự động nổi lên cao hơn khi tải trọng tăng"
                ],
                "answer": "Độ chìm mớn nước tỉ lệ thuận tuyến tính với khối lượng tải trọng đặt lên thuyền",
                "explanation": "Với thân thuyền có tiết diện ngang đều đặn, V_chìm = S_đáy · h. Ở trạng thái cân bằng: m·g = ρ·S_đáy·h·g ⇒ h = m / (ρ·S_đáy), chứng minh mối quan hệ tỉ lệ thuận tuyến tính hoàn hảo giữa độ chìm và tải trọng."
            }
        },
        "eng": {
            "law_name": "Archimedes' Principle & Hydrostatics",
            "formula": "Fb = ρ_fluid · V_submerged · g",
            "formula_unit": "N (Newton)",
            "mech": "Displacement Hull & Centerboard Keel",
            "metric": "Metacentric Height (GM) > 0 (Righting Stability)",
            "matching": [
                {"term": "Fb = ρ · V · g", "definition": "Buoyant force equals the weight of displaced liquid"},
                {"term": "Flotation Equilibrium (W = Fb)", "definition": "Total hull gravitational weight equals net upward fluid buoyant force"},
                {"term": "Pascal (Pa)", "definition": "SI unit measuring hydrostatic fluid pressure against hull plating"},
                {"term": "Draft Depth (h)", "definition": "Vertical distance from the waterline to the lowest point of the keel"}
            ],
            "cloze": [
                {"text": "A vessel floats in equilibrium when its average bulk density is [lower than] the density of the surrounding fluid.", "answer": "lower than", "options": ["lower than", "higher than", "zero", "doubled"]},
                {"text": "Hydrostatic buoyant force is directly proportional to the displaced [volume] of the submerged hull.", "answer": "volume", "options": ["volume", "height", "velocity", "temperature"]},
                {"text": "To prevent capsizing, engineers arrange heavy cargo to lower the vessel's [center of gravity] towards the keel.", "answer": "center of gravity", "options": ["center of gravity", "center of buoyancy", "masthead", "deck"]},
                {"text": "Hydrostatic pressure exerted on the submerged hull increases with [depth] according to p = ρ·g·h.", "answer": "depth", "options": ["depth", "surface area", "time", "speed"]}
            ],
            "q_physics": {
                "badge": "⚛️ Physics Principles & Mechanisms",
                "question": "Why does a massive steel ship float while a small solid steel ball sinks instantly in water?",
                "options": [
                    "The ship's hollow hull expands displaced water volume, reducing average density below that of water",
                    "Shipbuilding steel possesses lower atomic mass than bearing steel",
                    "Water surface tension alone sustains the ship's entire displacement",
                    "Propellers continuously drive water downward to generate vertical thrust"
                ],
                "answer": "The ship's hollow hull expands displaced water volume, reducing average density below that of water",
                "explanation": "A hollow hull encloses a huge internal volume V, yielding buoyant force Fb = ρ·V·g equal to gross weight W = m·g, enabling stable flotation."
            },
            "q_math": {
                "badge": "📐 Applied Math & Calculation",
                "question": "A model hull displaces submerged volume V = 0.0005 m³ (500 mL). Given water density ρ = 1000 kg/m³ and g = 9.8 m/s², calculate maximum buoyant force Fb:",
                "options": ["4.90 N", "9.80 N", "2.45 N", "0.50 N"],
                "answer": "4.90 N",
                "explanation": "Applying Archimedes' law: Fb = ρ · V · g = 1000 kg/m³ × 0.0005 m³ × 9.8 m/s² = 4.90 N."
            },
            "q_troubleshoot": {
                "badge": "🔧 Engineering Troubleshooting",
                "question": "During testing, a model boat capsizes when cargo is placed on deck. What engineering solution permanently corrects this transverse instability?",
                "options": [
                    "Lower cargo ballast deep into the hull bottom and broaden the beam width",
                    "Elevate cargo higher above deck level",
                    "Shape the bottom into a narrow vertical wedge",
                    "Reduce hull overall length by half"
                ],
                "answer": "Lower cargo ballast deep into the hull bottom and broaden the beam width",
                "explanation": "Transverse stability requires a positive Metacentric Height (GM > 0). Lowering cargo ballast lowers Center of Gravity G, while widening beam width increases the righting arm."
            },
            "q_materials": {
                "badge": "🔬 Materials & Structural Mechanics",
                "question": "What engineering performance standard is critical for underwater structural enclosures and hull gaskets?",
                "options": [
                    "Hydrophobic water repellency, corrosion resistance, and resilience under hydrostatic pressure cycles",
                    "High open-cell water absorption capacity",
                    "Rapid biological dissolution in saline water",
                    "High thermal conductivity to cool onboard systems"
                ],
                "answer": "Hydrophobic water repellency, corrosion resistance, and resilience under hydrostatic pressure cycles",
                "explanation": "Marine materials must remain chemically inert, impermeable to water under pressure, and fatigue-resistant."
            },
            "q_data": {
                "badge": "📊 Empirical Data Analysis",
                "question": "Testing shows that adding 100g, 200g, and 300g payloads increases hull draft depth by 1.2 cm, 2.4 cm, and 3.6 cm respectively. What scientific conclusion is verified?",
                "options": [
                    "Draft depth is directly and linearly proportional to payload mass",
                    "Draft depth follows a quadratic exponential power function",
                    "Buoyant force decays as cargo mass increases",
                    "Vessel freeboard increases when cargo is loaded"
                ],
                "answer": "Draft depth is directly and linearly proportional to payload mass",
                "explanation": "In constant cross-section hulls, submerged volume V = A·h. Flotation balance m·g = ρ·A·h·g proves linear direct proportionality h = m / (ρ·A)."
            }
        }
    },
    "circuit": {
        "vie": {
            "law_name": "Định luật Ohm & Công suất Tiêu thụ",
            "formula": "U = I · R  và  P = U · I = I² · R",
            "formula_unit": "V (Volt), A (Ampe), Ω (Ohm)",
            "mech": "Công tắc đóng ngắt & Cầu chì bảo vệ (Switch & Fuse Protection)",
            "metric": "Điện trở tương đương mắc song song R_p = (R1 · R2)/(R1 + R2)",
            "matching": [
                {"term": "U = I · R", "definition": "Định luật Ohm: Hiệu điện thế bằng tích cường độ dòng điện và điện trở"},
                {"term": "P = U · I", "definition": "Công suất tiêu thụ điện năng bằng hiệu điện thế nhân cường độ dòng điện"},
                {"term": "Đơn vị Ohm (Ω)", "definition": "Đơn vị đo điện trở cản trở dòng electron trong vật dẫn điện"},
                {"term": "Mạch mắc song song", "definition": "Hiệu điện thế trên các nhánh bằng nhau, dòng điện phân nhánh theo điện trở"}
            ],
            "cloze": [
                {"text": "Theo định luật Ohm, cường độ dòng điện chạy qua dây dẫn tỉ lệ thuận với hiệu điện thế và tỉ lệ nghịch với [điện trở].", "answer": "điện trở", "options": ["điện trở", "chiều dài", "nhiệt độ", "khối lượng"]},
                {"text": "Khi hai điện trở bằng nhau mắc song song, điện trở tương đương của mạch sẽ giảm đi [một nửa] so với mỗi điện trở đơn lẻ.", "answer": "một nửa", "options": ["một nửa", "gấp đôi", "bằng không", "gấp bốn"]},
                {"text": "Đèn LED là linh kiện bán dẫn chỉ cho dòng điện chạy qua theo chiều thuận từ cực [Anode] sang cực Cathode.", "answer": "Anode", "options": ["Anode", "Cathode", "Ground", "Neutral"]},
                {"text": "Hiện tượng dòng điện tăng vọt khi hai cực nguồn điện nối trực tiếp không qua điện trở tải được gọi là [đoản mạch].", "answer": "đoản mạch", "options": ["đoản mạch", "hở mạch", "quá áp", "cách điện"]}
            ],
            "q_physics": {
                "badge": "⚛️ Vật lý & Nguyên lý Cơ chế",
                "question": "Trong hệ thống điện dân dụng và lớp học, tại sao các thiết bị tiêu thụ điện luôn được mắc song song thay vì mắc nối tiếp?",
                "options": [
                    "Để mỗi thiết bị nhận đủ hiệu điện thế định mức và hoạt động độc lập khi thiết bị khác bị tắt hoặc hỏng",
                    "Để tổng dòng điện tiêu thụ trong toàn mạch giảm về 0",
                    "Để tiết kiệm dây dẫn điện tối đa",
                    "Vì mắc song song làm tăng điện trở tổng thể gấp đôi"
                ],
                "answer": "Để mỗi thiết bị nhận đủ hiệu điện thế định mức và hoạt động độc lập khi thiết bị khác bị tắt hoặc hỏng",
                "explanation": "Trong mạch song song: U_nguồn = U1 = U2... giúp các thiết bị nhận trọn vẹn điện áp định mức. Nếu một nhánh bị ngắt, các nhánh còn lại vẫn duy trì mạch kín bình thường."
            },
            "q_math": {
                "badge": "📐 Toán học Ứng dụng & Tính toán",
                "question": "Hai điện trở R1 = 20 Ω và R2 = 30 Ω được mắc song song vào nguồn điện U = 12 V. Cường độ dòng điện tổng I chạy qua mạch chính là bao nhiêu?",
                "options": ["1.00 A", "0.24 A", "2.50 A", "0.50 A"],
                "answer": "1.00 A",
                "explanation": "Điện trở tương đương mắc song song: R_p = (20 × 30) / (20 + 30) = 600 / 50 = 12 Ω. Cường độ dòng điện mạch chính: I = U / R_p = 12 V / 12 Ω = 1.00 A."
            },
            "q_troubleshoot": {
                "badge": "🔧 Xử lý Sự cố Kỹ thuật",
                "question": "Khi đóng công tắc, đèn LED không sáng dù pin mới. Kiểm tra thấy pin không nóng. Nguyên nhân kỹ thuật phổ biến nhất là gì?",
                "options": [
                    "Đèn LED bị cắm ngược chiều cực tính (chân dài Anode cần nối cực dương, chân ngắn Cathode nối cực âm)",
                    "Dây dẫn điện quá dài khiến electron bị bay hơi hết",
                    "Điện áp nguồn pin quá nhỏ không đủ làm nguyên tử đồng rung động",
                    "Công tắc bị đóng kín làm dòng điện không thoát ra ngoài được"
                ],
                "answer": "Đèn LED bị cắm ngược chiều cực tính (chân dài Anode cần nối cực dương, chân ngắn Cathode nối cực âm)",
                "explanation": "LED là diode phát quang bán dẫn phân cực. Cắm ngược chân sẽ đưa diode vào trạng thái phân cực nghịch (Reverse Bias), ngăn chặn hoàn toàn dòng electron chuyển động."
            },
            "q_materials": {
                "badge": "🔬 Khoa học Vật liệu & Kết cấu",
                "question": "Tại sao lõi dây điện dùng đồng (Cu) trong khi vỏ ngoài dùng nhựa PVC?",
                "options": [
                    "Đồng có mật độ electron tự do cao (điện trở suất cực nhỏ), còn PVC là chất cách điện bảo vệ an toàn",
                    "Đồng nhẹ hơn nhựa và có thể tự tái tạo khi bị đứt",
                    "Nhựa PVC có khả năng tự phát sinh dòng điện một chiều",
                    "Đồng rẻ tiền hơn đất sét và nhựa chịu nhiệt độ cao vô hạn"
                ],
                "answer": "Đồng có mật độ electron tự do cao (điện trở suất cực nhỏ), còn PVC là chất cách điện bảo vệ an toàn",
                "explanation": "Kim loại đồng có điện trở suất rất thấp (ρ ≈ 1.68 × 10⁻⁸ Ω·m) giúp truyền tải dòng điện với hao phí nhiệt Joules tối thiểu. Nhựa polymer PVC không có electron tự do nên cách điện hoàn hảo."
            },
            "q_data": {
                "badge": "📊 Phân tích Dữ liệu Thực nghiệm",
                "question": "Đo đạc điện áp U và dòng điện I qua một linh kiện điện trở cho kết quả: Khi U = 3V thì I = 0.15A; khi U = 6V thì I = 0.30A; khi U = 9V thì I = 0.45A. Trị số điện trở R là bao nhiêu?",
                "options": ["20 Ω", "15 Ω", "30 Ω", "10 Ω"],
                "answer": "20 Ω",
                "explanation": "Theo định luật Ohm: R = U / I. Tại 3V: 3 / 0.15 = 20 Ω. Tại 6V: 6 / 0.30 = 20 Ω. Tại 9V: 9 / 0.45 = 20 Ω. Điện trở có giá trị không đổi là 20 Ω."
            }
        },
        "eng": {
            "law_name": "Ohm's Law & Electrical Power",
            "formula": "V = I · R  and  P = V · I = I² · R",
            "formula_unit": "V (Volt), A (Ampere), Ω (Ohm)",
            "mech": "Single-Pole Switch & Fuse Overcurrent Protection",
            "metric": "Parallel Resistance R_p = (R1 · R2)/(R1 + R2)",
            "matching": [
                {"term": "V = I · R", "definition": "Ohm's Law: Voltage equals current multiplied by electrical resistance"},
                {"term": "P = V · I", "definition": "Joule Power Dissipation: Electrical energy consumed per unit time"},
                {"term": "Ohm (Ω)", "definition": "Standard SI unit of opposition to electric electron current flow"},
                {"term": "Parallel Circuit", "definition": "Branch voltages are identical; total current splits inversely to branch resistances"}
            ],
            "cloze": [
                {"text": "According to Ohm's Law, current through a conductor is inversely proportional to [resistance].", "answer": "resistance", "options": ["resistance", "length", "temperature", "mass"]},
                {"text": "When two identical resistors are connected in parallel, the total equivalent resistance becomes [half] of a single resistor.", "answer": "half", "options": ["half", "double", "zero", "quadrupled"]},
                {"text": "An LED conducts electrical current only in forward bias from the [Anode] to the Cathode.", "answer": "Anode", "options": ["Anode", "Cathode", "Ground", "Neutral"]},
                {"text": "An unintended low-resistance connection directly across a power source causes a dangerous [short circuit].", "answer": "short circuit", "options": ["short circuit", "open circuit", "surge", "grounding"]}
            ],
            "q_physics": {
                "badge": "⚛️ Physics Principles & Mechanisms",
                "question": "Why are electrical fixtures in residential and educational buildings wired in parallel rather than series?",
                "options": [
                    "Each fixture receives full nominal operating voltage and operates independently of others",
                    "To reduce total household power consumption to zero",
                    "To minimize copper conductor length",
                    "Because parallel wiring doubles equivalent resistance"
                ],
                "answer": "Each fixture receives full nominal operating voltage and operates independently of others",
                "explanation": "In parallel circuits, V_total = V1 = V2 = ... Each branch experiences identical voltage and operates independently if another branch opens."
            },
            "q_math": {
                "badge": "📐 Applied Math & Calculation",
                "question": "Two resistors R1 = 20 Ω and R2 = 30 Ω are connected in parallel across a 12 V power supply. Calculate total main line current I:",
                "options": ["1.00 A", "0.24 A", "2.50 A", "0.50 A"],
                "answer": "1.00 A",
                "explanation": "Parallel equivalent resistance: R_p = (20 × 30) / (20 + 30) = 600 / 50 = 12 Ω. Total current: I = V / R_p = 12 V / 12 Ω = 1.00 A."
            },
            "q_troubleshoot": {
                "badge": "🔧 Engineering Troubleshooting",
                "question": "When closing the circuit switch, an LED indicator fails to light up despite a fresh battery. What is the most common cause?",
                "options": [
                    "LED polarity is reversed (longer lead Anode must connect to positive, shorter lead Cathode to negative)",
                    "Connecting wires are too long causing electrons to evaporate",
                    "Battery voltage is too low to oscillate copper atoms",
                    "The closed switch prevents current from escaping"
                ],
                "answer": "LED polarity is reversed (longer lead Anode must connect to positive, shorter lead Cathode to negative)",
                "explanation": "LEDs are polarized semiconductor diodes. Reversed polarity places the diode into reverse-bias, blocking electron current flow."
            },
            "q_materials": {
                "badge": "🔬 Materials & Structural Mechanics",
                "question": "Why is copper (Cu) standard for wiring cores while PVC polymer jackets the exterior?",
                "options": [
                    "Copper has high free electron mobility (low resistivity), whereas PVC is a non-conductive dielectric insulator",
                    "Copper is lighter than plastic and self-heals when severed",
                    "PVC autonomously generates direct current",
                    "Copper is cheaper than clay and PVC tolerates infinite heat"
                ],
                "answer": "Copper has high free electron mobility (low resistivity), whereas PVC is a non-conductive dielectric insulator",
                "explanation": "Copper offers low electrical resistivity (ρ ≈ 1.68 × 10⁻⁸ Ω·m), minimizing Joule thermal losses. PVC polymer lacks free electrons, preventing electrical shock hazards."
            },
            "q_data": {
                "badge": "📊 Empirical Data Analysis",
                "question": "Voltage and current measurements across a resistor reveal: at 3V, I = 0.15A; at 6V, I = 0.30A; at 9V, I = 0.45A. What is the resistance R?",
                "options": ["20 Ω", "15 Ω", "30 Ω", "10 Ω"],
                "answer": "20 Ω",
                "explanation": "By Ohm's Law: R = V / I. At 3V: 3 / 0.15 = 20 Ω. At 6V: 6 / 0.30 = 20 Ω. At 9V: 9 / 0.45 = 20 Ω. The resistance is constant at 20 Ω."
            }
        }
    },
    "bridge": {
        "vie": {
            "law_name": "Cân bằng Tĩnh học & Ứng suất Kết cấu",
            "formula": "σ = F / A  và  ΣF = 0, ΣM = 0",
            "formula_unit": "Pa (Pascal) hoặc N/mm²",
            "mech": "Khung giàn tam giác & Thanh giằng chéo (Truss & Cross-bracing)",
            "metric": "Hệ số an toàn (Factor of Safety FS) ≥ 2.0",
            "matching": [
                {"term": "σ = F / A", "definition": "Ứng suất kéo hoặc nén bằng lực tác dụng chia cho diện tích mặt cắt ngang"},
                {"term": "Điều kiện cân bằng tĩnh", "definition": "Tổng các lực tác dụng và tổng mô-men lực quay đều phải bằng 0"},
                {"term": "Hệ số an toàn FS", "definition": "Tỷ số giữa tải trọng phá hủy cực đại và tải trọng làm việc cho phép"},
                {"term": "Giàn tam giác (Truss)", "definition": "Hình học cơ bản có tính bất biến hình dạng dưới tác dụng của ngoại lực"}
            ],
            "cloze": [
                {"text": "Hình [tam giác] là kết cấu hình học cơ bản cứng vững nhất trong kỹ thuật xây dựng cầu và tháp vì không bị biến dạng góc.", "answer": "tam giác", "options": ["tam giác", "tứ giác", "ngũ giác", "hình tròn"]},
                {"text": "Khi đặt tải trọng lên giữa nhịp cầu, thanh dầm phía trên chịu lực [nén] trong khi thanh dầm phía dưới chịu lực kéo.", "answer": "nén", "options": ["nén", "uốn xoắn", "cắt trượt", "chân không"]},
                {"text": "Hệ số an toàn (FS) của cây cầu được tính bằng tải trọng phá hủy chia cho tải trọng [cho phép].", "answer": "cho phép", "options": ["cho phép", "tự trọng", "ban đầu", "tối thiểu"]},
                {"text": "Độ võng của dầm cầu chịu tải ở giữa nhịp tỉ lệ nghịch với [mô-men quán tính] tiết diện dầm theo công thức δ = F·L³/(48·E·I).", "answer": "mô-men quán tính", "options": ["mô-men quán tính", "chiều dài dầm", "tải trọng", "nhiệt độ"]}
            ],
            "q_physics": {
                "badge": "⚛️ Vật lý & Nguyên lý Cơ chế",
                "question": "Tại sao trong thiết kế cầu giàn (Truss Bridge), các kỹ sư luôn ghép nối các thanh dầm thành các tam giác liên hoàn?",
                "options": [
                    "Tam giác là đa giác duy nhất có hình dạng bất biến khi chiều dài 3 cạnh cố định, chuyển lực uốn thành lực dọc trục (kéo/nén)",
                    "Để tiết kiệm que gỗ và keo dán tối đa",
                    "Vì hình tam giác hấp thụ ánh sáng mặt trời tốt hơn hình vuông",
                    "Để tạo khoảng trống cho gió thổi qua mà không tác dụng lực"
                ],
                "answer": "Tam giác là đa giác duy nhất có hình dạng bất biến khi chiều dài 3 cạnh cố định, chuyển lực uốn thành lực dọc trục (kéo/nén)",
                "explanation": "Kết cấu hình chữ nhật dễ bị biến dạng xiên thành hình bình hành dưới lực cắt ngang. Hình tam giác triệt tiêu biến dạng góc, phân tán lực truyền về hai mố cầu."
            },
            "q_math": {
                "badge": "📐 Toán học Ứng dụng & Tính toán",
                "question": "Một mô hình cầu que kem có tự trọng m_cầu = 150 g (0.15 kg). Khi đưa vào máy ép tải, cầu chịu được tải trọng tối đa m_tải = 4.5 kg trước khi gãy đổ. Tỷ số chịu tải trên trọng lượng (Load-to-Weight Ratio) là bao nhiêu?",
                "options": ["30 lần", "15 lần", "45 lần", "300 lần"],
                "answer": "30 lần",
                "explanation": "Tỷ số hiệu quả kết cấu: Ratio = m_tải / m_cầu = 4.5 kg / 0.15 kg = 30 lần tự trọng của cầu."
            },
            "q_troubleshoot": {
                "badge": "🔧 Xử lý Sự cố Kỹ thuật",
                "question": "Khi kiểm tra tải trọng, cầu que kem bị nứt gãy ở mối nối giữa hai thanh giàn chứ các thanh que gỗ không hề bị gãy. Biện pháp gia cố kỹ thuật nào tối ưu nhất?",
                "options": [
                    "Gia cố thêm miếng đệm liên kết (Gusset plate) bằng bìa cứng tại các điểm nút và tăng diện tích dán keo",
                    "Quấn thêm thật nhiều băng dính xung quanh giữa thân que",
                    "Dùng nước làm ẩm các thanh que gỗ để tăng tính uốn dẻo",
                    "Giảm số lượng thanh giàn tam giác đi một nửa"
                ],
                "answer": "Gia cố thêm miếng đệm liên kết (Gusset plate) bằng bìa cứng tại các điểm nút và tăng diện tích dán keo",
                "explanation": "Điểm nút (Joint node) là nơi tập trung ứng suất cắt lớn nhất. Tấm đệm gusset plate mở rộng diện tích truyền ứng suất và phân phối lực đều sang các thanh liên kết."
            },
            "q_materials": {
                "badge": "🔬 Khoa học Vật liệu & Kết cấu",
                "question": "Trong khoa học vật liệu xây dựng, hiện tượng một thanh dầm mỏng chịu nén bị cong vẹo sang bên trước khi đạt tới giới hạn bền nén của vật liệu gọi là gì?",
                "options": [
                    "Hiện tượng mất ổn định uốn dọc (Buckling)",
                    "Hiện tượng nóng chảy nhiệt dẻo",
                    "Hiện tượng từ hóa vật liệu",
                    "Hiện tượng siêu dẫn cơ học"
                ],
                "answer": "Hiện tượng mất ổn định uốn dọc (Buckling)",
                "explanation": "Dưới lực nén dọc trục, các chi tiết thanh mảnh (slender columns) rất dễ bị mất ổn định hình học và uốn cong đột ngột (Buckling theo công thức Euler) trước khi vật liệu bị nén vỡ."
            },
            "q_data": {
                "badge": "📊 Phân tích Dữ liệu Thực nghiệm",
                "question": "Thử nghiệm 3 mẫu cầu nhịp 30cm: Mẫu A (dầm phẳng đơn) võng 8mm ở tải 1kg; Mẫu B (dầm hộp chữ I) võng 2mm ở tải 1kg; Mẫu C (giàn Warren tam giác) võng 0.8mm ở tải 1kg. Nhận định nào chuẩn xác?",
                "options": [
                    "Kết cấu giàn tam giác có độ cứng chống uốn (Flexural Rigidity) cao nhất và phân tán tải trọng tốt nhất",
                    "Dầm phẳng đơn chịu tải tốt nhất vì tiết diện phẳng đồng đều",
                    "Độ võng không liên quan đến hình dạng kết cấu mặt cắt",
                    "Cả 3 mẫu đều có độ biến dạng đàn hồi giống hệt nhau"
                ],
                "answer": "Kết cấu giàn tam giác có độ cứng chống uốn (Flexural Rigidity) cao nhất và phân tán tải trọng tốt nhất",
                "explanation": "Độ võng nhỏ nhất (0.8mm) chứng minh mô hình giàn tam giác có mô-men quán tính diện tích và độ cứng uốn vượt trội so với dầm phẳng đặc."
            }
        },
        "eng": {
            "law_name": "Static Equilibrium & Structural Mechanics",
            "formula": "σ = F / A  and  ΣF = 0, ΣM = 0",
            "formula_unit": "Pa (Pascal) or N/mm²",
            "mech": "Triangular Truss & Gusset Plate Joint",
            "metric": "Factor of Safety (FS) ≥ 2.0",
            "matching": [
                {"term": "σ = F / A", "definition": "Normal mechanical stress equals axial force divided by cross-sectional area"},
                {"term": "Static Equilibrium (ΣF=0, ΣM=0)", "definition": "Sum of all external forces and rotational moments must equal zero"},
                {"term": "Factor of Safety (FS)", "definition": "Ratio of structural ultimate collapse load to maximum allowable working load"},
                {"term": "Triangular Truss", "definition": "Geometric structure that resists distortion by converting bending into axial forces"}
            ],
            "cloze": [
                {"text": "The [triangle] is the fundamental rigid geometric shape in structural engineering because its angles cannot distort without changing side lengths.", "answer": "triangle", "options": ["triangle", "rectangle", "pentagon", "circle"]},
                {"text": "Under central span loads, the top chord of a bridge experiences [compression] while the bottom chord undergoes tension.", "answer": "compression", "options": ["compression", "torsion", "shear", "vacuum"]},
                {"text": "The Factor of Safety (FS) equals the ultimate failure load divided by the [allowable] service load.", "answer": "allowable", "options": ["allowable", "dead weight", "initial", "minimum"]},
                {"text": "Mid-span deflection of a loaded beam is inversely proportional to its cross-sectional [moment of inertia].", "answer": "moment of inertia", "options": ["moment of inertia", "span length", "point load", "temperature"]}
            ],
            "q_physics": {
                "badge": "⚛️ Physics Principles & Mechanisms",
                "question": "Why do civil engineers arrange bridge girders into interconnected triangular truss networks?",
                "options": [
                    "Triangles have fixed geometric rigidity, converting destructive flexural bending moments into axial tension and compression",
                    "To minimize popsicle stick and adhesive usage",
                    "Because triangular shapes absorb solar radiation better than squares",
                    "To allow crosswinds to pass through without exerting dynamic pressure"
                ],
                "answer": "Triangles have fixed geometric rigidity, converting destructive flexural bending moments into axial tension and compression",
                "explanation": "Unlike quadrilaterals which deform under shear, triangles cannot shear without member elongation or compression, efficiently channeling loads directly to abutments."
            },
            "q_math": {
                "badge": "📐 Applied Math & Calculation",
                "question": "A model truss bridge has self-weight m_bridge = 150 g (0.15 kg). In a load test, it supports m_load = 4.5 kg before structural failure. What is its structural Load-to-Weight efficiency ratio?",
                "options": ["30 times", "15 times", "45 times", "300 times"],
                "answer": "30 times",
                "explanation": "Structural efficiency ratio: Ratio = m_load / m_bridge = 4.5 kg / 0.15 kg = 30 times its own structural weight."
            },
            "q_troubleshoot": {
                "badge": "🔧 Engineering Troubleshooting",
                "question": "During compression testing, a wooden truss fails specifically at the glued node connections while the wooden members remain intact. What is the best engineering remedy?",
                "options": [
                    "Reinforce node joints with cardstock gusset plates to increase shear bonding contact area",
                    "Wrap adhesive tape along the middle span of the beams",
                    "Dampen the wooden members with water to increase flexibility",
                    "Remove half of the diagonal truss web members"
                ],
                "answer": "Reinforce node joints with cardstock gusset plates to increase shear bonding contact area",
                "explanation": "Nodes experience concentrated shear stress. Gusset plates enlarge adhesive contact area, spreading shear loads evenly across connecting members."
            },
            "q_materials": {
                "badge": "🔬 Materials & Structural Mechanics",
                "question": "What phenomenon occurs when a slender structural column under axial compression buckles outward before reaching the compressive material yield strength?",
                "options": [
                    "Elastic Buckling failure",
                    "Thermoplastic liquefaction",
                    "Ferromagnetic orientation",
                    "Superconducting resonance"
                ],
                "answer": "Elastic Buckling failure",
                "explanation": "Slender structural columns fail by Euler buckling (loss of geometric lateral stability) under compressive loads well below the material's compressive crushing limit."
            },
            "q_data": {
                "badge": "📊 Empirical Data Analysis",
                "question": "Testing three 30cm spans under a 1kg central load: Model A (flat beam) deflects 8mm; Model B (I-beam) deflects 2mm; Model C (Warren truss) deflects 0.8mm. What conclusion is proven?",
                "options": [
                    "The triangular truss possesses superior flexural rigidity and optimal load distribution",
                    "The flat beam handles load best due to uniform flat cross-section",
                    "Beam deflection is independent of cross-sectional geometry",
                    "All three configurations exhibit identical elastic deformation"
                ],
                "answer": "The triangular truss possesses superior flexural rigidity and optimal load distribution",
                "explanation": "Lowest deflection (0.8mm) confirms that the triangular truss structure delivers the highest area moment of inertia and flexural stiffness."
            }
        }
    }
}

# Generic Fallback for other domains to guarantee 100% complete coverage
FALLBACK_DOMAINS = ["energy_renewable", "filtration", "robotics", "mechanism", "materials_science", "computing", "vehicle", "biology"]

def get_domain_spec(cat, is_vie):
    # Check if explicitly in MASTER_SPECS
    if cat in MASTER_SPECS:
        return MASTER_SPECS[cat]["vie" if is_vie else "eng"]
    
    # Rich Domain-specific generators for remaining 8 domains
    lang_key = "vie" if is_vie else "eng"
    if cat == "mechanism":
        if is_vie:
            return {
                "law_name": "Định luật Đòn bẩy & Bảo toàn Công cơ học",
                "formula": "F1 · d1 = F2 · d2  và  MA = F_tải / F_kéo",
                "formula_unit": "N (Newton), N·m (Mô-men xoắn)",
                "mech": "Ròng rọc palăng & Bánh răng hành tinh (Pulley & Gear Train)",
                "metric": "Lợi thế cơ học (Mechanical Advantage MA) > 1.0",
                "matching": [
                    {"term": "F1 · d1 = F2 · d2", "definition": "Quy tắc đòn bẩy: Tích lực và cánh tay đòn ở hai phía điểm tựa bằng nhau"},
                    {"term": "MA = F_tải / F_kéo", "definition": "Lợi thế cơ học thể hiện mức độ giảm lực kéo khi sử dụng máy cơ"},
                    {"term": "Ròng rọc động", "definition": "Cho lợi 2 lần về lực nhưng thiệt 2 lần về đường đi của dây kéo"},
                    {"term": "Đơn vị Joule (J)", "definition": "Đơn vị đo công cơ học và năng lượng trong hệ đo lường SI"}
                ],
                "cloze": [
                    {"text": "Định luật về công khẳng định: Không một máy cơ đơn giản nào cho ta lợi về [công], được lợi bao nhiêu lần về lực thì thiệt bấy nhiêu lần về đường đi.", "answer": "công", "options": ["công", "lực", "vận tốc", "thời gian"]},
                    {"text": "Một hệ thống palăng gồm 4 đoạn dây đỡ tải trọng sẽ cho lợi thế cơ học lý thuyết bằng [bốn] lần.", "answer": "bốn", "options": ["bốn", "hai", "tám", "một"]},
                    {"text": "Khi hai bánh răng ăn khớp, bánh răng có số răng lớn hơn sẽ quay với tốc độ [chậm hơn] nhưng sinh mô-men xoắn lớn hơn.", "answer": "chậm hơn", "options": ["chậm hơn", "nhanh hơn", "bằng nhau", "ngược chiều"]},
                    {"text": "Để nâng một vật nặng 600N bằng đòn bẩy với lực kéo 150N, cánh tay đòn của lực phải dài gấp [bốn] lần cánh tay đòn của tải.", "answer": "bốn", "options": ["bốn", "hai", "ba", "sáu"]}
                ],
                "q_physics": {
                    "badge": "⚛️ Vật lý & Nguyên lý Cơ chế",
                    "question": "Theo 'Định luật vàng về công' của cơ học cổ điển, kết luận nào sau đây về máy cơ đơn giản là chính xác?",
                    "options": [
                        "Không một máy cơ đơn giản nào cho ta lợi về công; được lợi bao nhiêu lần về lực thì thiệt bấy nhiêu lần về đường đi",
                        "Ròng rọc kép có thể tự động sinh thêm năng lượng để nâng vật",
                        "Đòn bẩy loại 1 luôn cho ta lợi cả về lực lẫn công cơ học",
                        "Bánh răng truyền động triệt tiêu hoàn toàn công cản của ma sát"
                    ],
                    "answer": "Không một máy cơ đơn giản nào cho ta lợi về công; được lợi bao nhiêu lần về lực thì thiệt bấy nhiêu lần về đường đi",
                    "explanation": "Bảo toàn năng lượng: W = F · s = hằng số (bỏ qua ma sát). Nếu cơ cấu giúp giảm lực F xuống n lần thì quãng đường dịch chuyển s bắt buộc phải tăng lên n lần."
                },
                "q_math": {
                    "badge": "📐 Toán học Ứng dụng & Tính toán",
                    "question": "Một người dùng hệ thống ròng rọc palăng có 4 đoạn dây chịu tải để nâng một khối vật liệu nặng P = 600 N lên cao h = 2 m. Bỏ qua ma sát, lực kéo F và chiều dài dây s cần kéo là bao nhiêu?",
                    "options": ["F = 150 N, s = 8 m", "F = 300 N, s = 4 m", "F = 150 N, s = 2 m", "F = 600 N, s = 8 m"],
                    "answer": "F = 150 N, s = 8 m",
                    "explanation": "Lợi thế cơ học MA = 4. Lực kéo: F = P / 4 = 600 / 4 = 150 N. Chiều dài dây cần kéo: s = 4 × h = 4 × 2 m = 8 m. Công sinh ra: W = 150 × 8 = 1200 J = 600 × 2."
                },
                "q_troubleshoot": {
                    "badge": "🔧 Xử lý Sự cố Kỹ thuật",
                    "question": "Trong mô hình truyền động bánh răng, khi động cơ quay nhưng trục bị kẹt cứng và phát ra tiếng kêu rít cơ học. Nguyên nhân kỹ thuật nào sau đây là chuẩn xác?",
                    "options": [
                        "Khoảng cách giữa hai tâm trục quá ngắn làm các răng bị chèn ép quá chặt (Backlash = 0)",
                        "Động cơ quay quá êm ái",
                        "Số răng của bánh dẫn lớn hơn bánh bị dẫn",
                        "Các bánh răng được bôi trơn quá kỹ bằng dầu máy"
                    ],
                    "answer": "Khoảng cách giữa hai tâm trục quá ngắn làm các răng bị chèn ép quá chặt (Backlash = 0)",
                    "explanation": "Nếu khoảng cách trục nhỏ hơn tổng bán kính vòng lăn (R1 + R2), các profin răng sẽ cắn chặt vào nhau mà không có khe hở cạnh răng (backlash), dẫn đến kẹt cơ khí và mài mòn răng."
                },
                "q_materials": {
                    "badge": "🔬 Khoa học Vật liệu & Kết cấu",
                    "question": "Tại sao các ổ trục quay và rãnh ròng rọc thường được chế tạo bằng vật liệu polymer chịu mài mòn (POM/Nylon) hoặc thép tôi cứng có bôi trơn?",
                    "options": [
                        "Để giảm hệ số ma sát trượt và ngăn ngừa hiện tượng mài mòn dính dưới áp lực tiếp xúc lớn",
                        "Để các chi tiết dễ bị biến dạng mềm khi quay nhanh",
                        "Để ròng rọc có thể co giãn đàn hồi theo độ căng dây",
                        "Để tăng tối đa ma sát kéo vật nặng lên nhanh hơn"
                    ],
                    "answer": "Để giảm hệ số ma sát trượt và ngăn ngừa hiện tượng mài mòn dính dưới áp lực tiếp xúc lớn",
                    "explanation": "Ma sát tiếp xúc sinh nhiệt và làm hao tổn công suất cơ học. Vật liệu tự bôi trơn hoặc vòng bi thép tôi giúp hệ số ma sát giảm từ 0.3 xuống dưới 0.02."
                },
                "q_data": {
                    "badge": "📊 Phân tích Dữ liệu Thực nghiệm",
                    "question": "Đo lực kế khi nâng tải trọng 100N bằng ròng rọc đơn: Lực nâng thực tế đo được là 58N (thay vì 50N lý thuyết). Hiệu suất cơ học của hệ thống là bao nhiêu?",
                    "options": ["86.2%", "50.0%", "95.0%", "72.4%"],
                    "answer": "86.2%",
                    "explanation": "Hiệu suất: η = (Lực lý thuyết / Lực thực tế) × 100% = (50 N / 58 N) × 100% ≈ 86.2%. Phần hao hụt 13.8% tiêu tán do ma sát trục và trọng lượng ròng rọc động."
                }
            }
        else:
            return {
                "law_name": "Law of the Lever & Conservation of Work",
                "formula": "F1 · d1 = F2 · d2  and  MA = F_load / F_effort",
                "formula_unit": "N (Newton), N·m (Torque)",
                "mech": "Block and Tackle & Epicyclic Gear Train",
                "metric": "Mechanical Advantage (MA) > 1.0",
                "matching": [
                    {"term": "F1 · d1 = F2 · d2", "definition": "Law of the lever: Product of force and effort arm equals load product"},
                    {"term": "MA = F_load / F_effort", "definition": "Mechanical advantage indicating force multiplication factor"},
                    {"term": "Movable Pulley", "definition": "Halves required effort force while doubling pulling distance"},
                    {"term": "Joule (J)", "definition": "Standard SI unit measuring mechanical work and energy"}
                ],
                "cloze": [
                    {"text": "The golden rule of mechanics states: simple machines cannot create [work]; reducing effort force increases displacement.", "answer": "work", "options": ["work", "force", "speed", "time"]},
                    {"text": "A block and tackle system with 4 supporting rope strands provides a theoretical mechanical advantage of [four].", "answer": "four", "options": ["four", "two", "eight", "one"]},
                    {"text": "In an intermeshing gear pair, the larger gear rotates [slower] while delivering higher output torque.", "answer": "slower", "options": ["slower", "faster", "identically", "linearly"]},
                    {"text": "To lift a 600N weight with 150N effort using a lever, the effort arm must be [four] times longer than the load arm.", "answer": "four", "options": ["four", "two", "three", "six"]}
                ],
                "q_physics": {
                    "badge": "⚛️ Physics Principles & Mechanisms",
                    "question": "According to the conservation of work in classical mechanics, which statement is true for simple machines?",
                    "options": [
                        "Machines cannot multiply work; any reduction in input effort requires a proportional increase in displacement",
                        "Pulleys autonomously create new kinetic energy to lift masses",
                        "First-class levers multiply both work output and effort force simultaneously",
                        "Gears eliminate frictional energy dissipation completely"
                    ],
                    "answer": "Machines cannot multiply work; any reduction in input effort requires a proportional increase in displacement",
                    "explanation": "Conservation of energy: W = F · d = const (neglecting friction). Halving effort force requires doubling displacement distance."
                },
                "q_math": {
                    "badge": "📐 Applied Math & Calculation",
                    "question": "A block and tackle with 4 supporting rope strands lifts a load W = 600 N to height h = 2 m. Neglecting friction, calculate effort force F and rope pulled s:",
                    "options": ["F = 150 N, s = 8 m", "F = 300 N, s = 4 m", "F = 150 N, s = 2 m", "F = 600 N, s = 8 m"],
                    "answer": "F = 150 N, s = 8 m",
                    "explanation": "Mechanical Advantage MA = 4. Effort: F = 600 / 4 = 150 N. Rope length: s = 4 × 2 m = 8 m. Total work: W = 150 × 8 = 1200 J = 600 × 2."
                },
                "q_troubleshoot": {
                    "badge": "🔧 Engineering Troubleshooting",
                    "question": "In a gear transmission prototype, the electric motor stalls and emits mechanical whining under zero load. What is the root cause?",
                    "options": [
                        "Center-to-center shaft distance is too short, eliminating tooth backlash and jamming the pitch mesh",
                        "The electric motor rotates too quietly",
                        "The driver gear has more teeth than the driven gear",
                        "Gear teeth are excessively lubricated"
                    ],
                    "answer": "Center-to-center shaft distance is too short, eliminating tooth backlash and jamming the pitch mesh",
                    "explanation": "If shaft spacing is less than the sum of pitch radii, gear teeth bind with zero clearance (backlash), causing friction lockup."
                },
                "q_materials": {
                    "badge": "🔬 Materials & Structural Mechanics",
                    "question": "Why are rotating axle bushings and pulleys engineered with self-lubricating polymers (POM/Nylon) or hardened steel bearings?",
                    "options": [
                        "To minimize kinetic sliding friction and prevent adhesive galling under sustained loads",
                        "To allow gears to soften and deform under high torque",
                        "To enable pulleys to stretch elastically under rope tension",
                        "To maximize surface friction to pull cables faster"
                    ],
                    "answer": "To minimize kinetic sliding friction and prevent adhesive galling under sustained loads",
                    "explanation": "Rolling element bearings and engineering polymers drop the coefficient of friction from 0.3 down to 0.01-0.02, preserving mechanical efficiency."
                },
                "q_data": {
                    "badge": "📊 Empirical Data Analysis",
                    "question": "Lifting a 100N weight with a movable pulley requires 58N measured effort instead of the 50N theoretical ideal. What is the system's mechanical efficiency?",
                    "options": ["86.2%", "50.0%", "95.0%", "72.4%"],
                    "answer": "86.2%",
                    "explanation": "Mechanical efficiency: η = (Ideal Force / Measured Force) × 100% = (50 N / 58 N) × 100% ≈ 86.2%. The 13.8% deficit is lost to bearing friction."
                }
            }
    elif cat == "vehicle":
        if is_vie:
            return {
                "law_name": "Định luật II Newton & Động năng Chuyển động",
                "formula": "F = m · a  và  Ek = (1/2) · m · v²",
                "formula_unit": "m/s (Vận tốc), m/s² (Gia tốc), J (Joule)",
                "mech": "Trục quay giảm ma sát & Bánh xe bám đường (Axle Bushing & Traction Tire)",
                "metric": "Hiệu suất chuyển đổi năng lượng thế năng sang động năng ≥ 75%",
                "matching": [
                    {"term": "F = m · a", "definition": "Định luật II Newton: Gia tốc tỉ lệ thuận với lực kéo và tỉ lệ nghịch với khối lượng xe"},
                    {"term": "Ek = (1/2) · m · v²", "definition": "Động năng của xe tỉ lệ với bình phương vận tốc chuyển động"},
                    {"term": "F_ms = μ · N", "definition": "Lực ma sát lăn cản trở chuyển động của bánh xe trên mặt đường"},
                    {"term": "Đơn vị m/s²", "definition": "Đơn vị đo gia tốc tăng tốc hoặc hãm phanh của xe trong hệ SI"}
                ],
                "cloze": [
                    {"text": "Theo định luật II Newton, để xe đua đạt gia tốc lớn nhất thì lực kéo phải cực đại và khối lượng toàn xe phải [nhỏ nhất].", "answer": "nhỏ nhất", "options": ["nhỏ nhất", "lớn nhất", "không đổi", "bằng không"]},
                    {"text": "Khi vận tốc của xe tăng gấp đôi, động năng chuyển động của xe sẽ tăng lên gấp [bốn] lần.", "answer": "bốn", "options": ["bốn", "hai", "tám", "mười sáu"]},
                    {"text": "Bánh xe chủ động cần có hệ số ma sát nghỉ [lớn] với mặt sàn để chống hiện tượng trượt quay khi khởi hành.", "answer": "lớn", "options": ["lớn", "nhỏ", "bằng không", "âm"]},
                    {"text": "Bảo toàn cơ năng: Thế năng đàn hồi của dây cao su được chuyển hóa thành [động năng] của xe và nhiệt ma sát.", "answer": "động năng", "options": ["động năng", "quang năng", "hóa năng", "thế năng"]}
                ],
                "q_physics": {
                    "badge": "⚛️ Vật lý & Nguyên lý Cơ chế",
                    "question": "Trong xe đua chạy bằng dây cao su hoặc bóng bay, chuyển hóa năng lượng nào là cốt lõi để xe chuyển động?",
                    "options": [
                        "Thế năng đàn hồi biến dạng chuyển hóa thành động năng tịnh tiến của toàn bộ thân xe",
                        "Nhiệt năng của không khí chuyển thành thế năng trọng trường",
                        "Quang năng của ánh sáng mặt trời chuyển thành điện năng",
                        "Năng lượng hạt nhân phân rã trong dây cao su"
                    ],
                    "answer": "Thế năng đàn hồi biến dạng chuyển hóa thành động năng tịnh tiến của toàn bộ thân xe",
                    "explanation": "Khi kéo căng dây cao su hoặc thổi căng bóng bay, công cơ học được tích trữ dưới dạng thế năng đàn hồi Ep = 1/2·k·x². Khi giải phóng, lực đàn hồi sinh công làm quay trục bánh xe, chuyển thành động năng Ek = 1/2·m·v²."
                },
                "q_math": {
                    "badge": "📐 Toán học Ứng dụng & Tính toán",
                    "question": "Một xe đua mô hình có khối lượng m = 0.25 kg. Dây cao su truyền cho xe một động năng Ek = 1.125 J. Vận tốc cực đại v mà xe đạt được là bao nhiêu?",
                    "options": ["3.00 m/s", "2.25 m/s", "4.50 m/s", "1.50 m/s"],
                    "answer": "3.00 m/s",
                    "explanation": "Công thức động năng: Ek = (1/2) · m · v² ⇒ v² = 2·Ek / m = (2 × 1.125) / 0.25 = 2.25 / 0.25 = 9 ⇒ v = √9 = 3.00 m/s."
                },
                "q_troubleshoot": {
                    "badge": "🔧 Xử lý Sự cố Kỹ thuật",
                    "question": "Khi thả dây cao su, bánh xe sau của xe bị quay tít tại chỗ nhưng xe không tiến lên phía trước được (hiện tượng wheel-spin). Giải pháp kỹ thuật nào sau đây là chuẩn xác?",
                    "options": [
                        "Bọc thêm vòng đệm cao su hoặc bóng bay quanh vành bánh xe để tăng hệ số ma sát bám đường",
                        "Gọt nhẵn bóng bề mặt bánh xe để trơn trượt hơn",
                        "Lắp thêm động cơ phản lực",
                        "Đổ dầu ăn lên sàn nhà nơi xe chạy"
                    ],
                    "answer": "Bọc thêm vòng đệm cao su hoặc bóng bay quanh vành bánh xe để tăng hệ số ma sát bám đường",
                    "explanation": "Bánh xe bị trượt khi mô-men xoắn truyền tới lớn hơn lực ma sát nghỉ cực đại (F_kéo > F_ms_max = μ · N). Tăng hệ số ma sát bám đường μ bằng lớp cao su sẽ truyền toàn bộ lực kéo xuống mặt đường để đẩy xe đi."
                },
                "q_materials": {
                    "badge": "🔬 Khoa học Vật liệu & Kết cấu",
                    "question": "Để giảm thiểu lực cản ma sát giữa trục xe bằng thép và ống đỡ trục (bushing), giải pháp vật liệu nào tối ưu nhất?",
                    "options": [
                        "Dùng ống hút nhựa trơn nhẵn làm ổ trượt và nhỏ một giọt dầu bôi trơn chuyên dụng",
                        "Dán keo 502 cố định trục xe chặt vào khung thân",
                        "Dùng giấy ráp thô quấn quanh trục xe",
                        "Để trục cọ xát trực tiếp vào bìa carton thô ráp"
                    ],
                    "answer": "Dùng ống hút nhựa trơn nhẵn làm ổ trượt và nhỏ một giọt dầu bôi trơn chuyên dụng",
                    "explanation": "Vật liệu tiếp xúc có bề mặt nhẵn bóng (nhựa PP/ống hút) kết hợp chất bôi trơn lỏng làm giảm hệ số ma sát trượt xuống mức thấp nhất, tránh tiêu hao động năng quay của bánh xe."
                },
                "q_data": {
                    "badge": "📊 Phân tích Dữ liệu Thực nghiệm",
                    "question": "Đo vận tốc xe đua tại các mốc thời gian: t = 0s (v = 0m/s); t = 1s (v = 2m/s); t = 2s (v = 4m/s); t = 3s (v = 6m/s). Gia tốc trung bình của xe trong giai đoạn tăng tốc này là bao nhiêu?",
                    "options": ["2.00 m/s²", "1.50 m/s²", "3.00 m/s²", "0.67 m/s²"],
                    "answer": "2.00 m/s²",
                    "explanation": "Gia tốc: a = Δv / Δt = (6 - 0) / (3 - 0) = 6 / 3 = 2.00 m/s²."
                }
            }
        else:
            return {
                "law_name": "Newton's Second Law & Kinetic Energy",
                "formula": "F = m · a  and  Ek = (1/2) · m · v²",
                "formula_unit": "m/s (Velocity), m/s² (Acceleration), J (Joule)",
                "mech": "Low-Friction Axle Bushing & Traction Tire",
                "metric": "Potential to Kinetic Energy Conversion Efficiency ≥ 75%",
                "matching": [
                    {"term": "F = m · a", "definition": "Newton's Second Law: Acceleration is proportional to net force and inversely to mass"},
                    {"term": "Ek = (1/2) · m · v²", "definition": "Kinetic energy grows quadratically with vehicle translational velocity"},
                    {"term": "F_friction = μ · N", "definition": "Rolling friction opposing vehicle wheel movement across the surface"},
                    {"term": "m/s²", "definition": "Standard SI unit of linear acceleration or braking deceleration"}
                ],
                "cloze": [
                    {"text": "According to Newton's Second Law, maximizing acceleration requires maximizing thrust while keeping vehicle mass [minimal].", "answer": "minimal", "options": ["minimal", "maximal", "constant", "zero"]},
                    {"text": "Doubling a vehicle's speed increases its kinetic energy by a factor of [four].", "answer": "four", "options": ["four", "two", "eight", "sixteen"]},
                    {"text": "Drive wheels require a [high] static coefficient of friction against the floor to prevent wheel-spin.", "answer": "high", "options": ["high", "low", "zero", "negative"]},
                    {"text": "Conservation of energy: Stored elastic potential energy converts into forward [kinetic energy] and thermal friction.", "answer": "kinetic energy", "options": ["kinetic energy", "light energy", "chemical energy", "potential energy"]}
                ],
                "q_physics": {
                    "badge": "⚛️ Physics Principles & Mechanisms",
                    "question": "In an elastic rubber-band or balloon-powered racer, what primary energy transformation drives vehicle locomotion?",
                    "options": [
                        "Elastic potential energy converts into translational vehicle kinetic energy",
                        "Air thermal energy converts into gravitational potential energy",
                        "Solar photons convert into electromagnetic induction",
                        "Nuclear atomic decay within the elastomer band"
                    ],
                    "answer": "Elastic potential energy converts into translational vehicle kinetic energy",
                    "explanation": "Winding the band stores elastic potential energy Ep = 1/2·k·x². Upon release, elastic restoring torque drives the drive axle, converting into kinetic energy Ek = 1/2·m·v²."
                },
                "q_math": {
                    "badge": "📐 Applied Math & Calculation",
                    "question": "A model race car has mass m = 0.25 kg. An elastic band delivers kinetic energy Ek = 1.125 J. Calculate the maximum velocity v achieved:",
                    "options": ["3.00 m/s", "2.25 m/s", "4.50 m/s", "1.50 m/s"],
                    "answer": "3.00 m/s",
                    "explanation": "Kinetic energy formula: Ek = (1/2) · m · v² ⇒ v² = 2·Ek / m = (2 × 1.125) / 0.25 = 2.25 / 0.25 = 9 ⇒ v = √9 = 3.00 m/s."
                },
                "q_troubleshoot": {
                    "badge": "🔧 Engineering Troubleshooting",
                    "question": "Upon release, the racer's drive wheels spin rapidly in place without propelling the car forward (wheel-spin). What engineering adjustment resolves this?",
                    "options": [
                        "Wrap rubber rings or balloon sleeves around the drive wheels to boost the static friction coefficient",
                        "Sand the wheel tread to make it mirror-smooth",
                        "Install a jet rocket engine",
                        "Lubricate the testing floor with cooking oil"
                    ],
                    "answer": "Wrap rubber rings or balloon sleeves around the drive wheels to boost the static friction coefficient",
                    "explanation": "Wheel-spin occurs when drive torque exceeds maximum static friction traction (F_tractive > μ · N). Adding rubber increases μ, converting rotation into forward thrust."
                },
                "q_materials": {
                    "badge": "🔬 Materials & Structural Mechanics",
                    "question": "To minimize rotational friction between the steel axle and chassis sleeve bushings, what material strategy is optimal?",
                    "options": [
                        "Use smooth polypropylene straw sleeves lubricated with a drop of low-viscosity machine oil",
                        "Cyanoacrylate glue the axle directly to the chassis frame",
                        "Wrap abrasive sandpaper tightly around the axle",
                        "Permit the bare steel axle to grind directly against corrugated cardboard"
                    ],
                    "answer": "Use smooth polypropylene straw sleeves lubricated with a drop of low-viscosity machine oil",
                    "explanation": "Low-friction polymer bushings paired with fluid lubrication reduce the sliding friction coefficient, preventing kinetic dissipation."
                },
                "q_data": {
                    "badge": "📊 Empirical Data Analysis",
                    "question": "Velocity sensor data records: at t = 0s, v = 0 m/s; at t = 1s, v = 2 m/s; at t = 2s, v = 4 m/s; at t = 3s, v = 6 m/s. What is the average acceleration?",
                    "options": ["2.00 m/s²", "1.50 m/s²", "3.00 m/s²", "0.67 m/s²"],
                    "answer": "2.00 m/s²",
                    "explanation": "Acceleration: a = Δv / Δt = (6 - 0) / (3 - 0) = 6 / 3 = 2.00 m/s²."
                }
            }
    else: # Default for computing, renewable energy, filtration, materials, biology
        if is_vie:
            return {
                "law_name": "Định luật Bảo toàn Năng lượng & Tối ưu hóa Hệ thống",
                "formula": "E_in = E_out + Q_hao phí  và  η = (E_hữu ích / E_toàn phần) · 100%",
                "formula_unit": "J (Joule), W (Watt), % (Hiệu suất)",
                "mech": "Hệ thống điều khiển phản hồi kín (Closed-Loop Feedback Control)",
                "metric": "Hiệu suất chuyển đổi năng lượng η ≥ 85%",
                "matching": [
                    {"term": "Định luật Bảo toàn Năng lượng", "definition": "Năng lượng không tự nhiên sinh ra hay mất đi mà chỉ chuyển hóa từ dạng này sang dạng khác"},
                    {"term": "Hiệu suất η = (P_ra / P_vào) · 100%", "definition": "Tỷ lệ phần trăm năng lượng có ích thu được so với tổng năng lượng cấp vào"},
                    {"term": "Đơn vị Watt (W)", "definition": "Đơn vị đo công suất tiêu thụ hoặc phát điện bằng 1 Joule trên 1 giây"},
                    {"term": "Độ phức tạp tính toán O(n)", "definition": "Đại lượng toán học đo lường tốc độ tăng số bước xử lý theo quy mô dữ liệu"}
                ],
                "cloze": [
                    {"text": "Trong mọi quá trình kỹ thuật, tổng năng lượng cung cấp luôn bằng năng lượng có ích cộng với năng lượng [hao phí] dưới dạng nhiệt.", "answer": "hao phí", "options": ["hao phí", "vô hạn", "tự do", "nguyên tử"]},
                    {"text": "Hiệu suất của một hệ thống kỹ thuật luôn [nhỏ hơn] 100% do sự tồn tại không thể triệt tiêu của ma sát và điện trở.", "answer": "nhỏ hơn", "options": ["nhỏ hơn", "lớn hơn", "bằng", "gấp đôi"]},
                    {"text": "Hệ thống điều khiển phản hồi kín sử dụng tín hiệu từ [cảm biến] để tự động điều chỉnh cơ cấu chấp hành theo mục tiêu.", "answer": "cảm biến", "options": ["cảm biến", "nguồn điện", "dây dẫn", "vỏ máy"]},
                    {"text": "Tối ưu hóa kỹ thuật là việc cân bằng giữa các tiêu chí hiệu năng và các [ràng buộc] về chi phí và tài nguyên.", "answer": "ràng buộc", "options": ["ràng buộc", "bản vẽ", "nguyên lý", "công thức"]}
                ],
                "q_physics": {
                    "badge": "⚛️ Vật lý & Nguyên lý Cơ chế",
                    "question": "Theo định luật bảo toàn năng lượng thứ nhất của nhiệt động lực học, tại sao không thể chế tạo được một 'động cơ vĩnh cửu' hoạt động vô hạn mà không cần nạp năng lượng?",
                    "options": [
                        "Năng lượng luôn được bảo toàn; hệ thống luôn tiêu tán một phần cơ năng thành nhiệt năng do ma sát và điện trở",
                        "Trọng lực của Trái Đất sẽ triệt tiêu động cơ sau một chu kỳ",
                        "Không khí xung quanh sẽ hút cạn điện tích của động cơ",
                        "Kim loại làm động cơ sẽ bị mềm dần theo thời gian"
                    ],
                    "answer": "Năng lượng luôn được bảo toàn; hệ thống luôn tiêu tán một phần cơ năng thành nhiệt năng do ma sát và điện trở",
                    "explanation": "Định luật bảo toàn năng lượng (E_vào = E_ra + Q_hao phí) và nguyên lý II nhiệt động lực học khẳng định luôn có sự hao phí nhiệt không thể thu hồi 100%, do đó động cơ vĩnh cửu là bất khả thi."
                },
                "q_math": {
                    "badge": "📐 Toán học Ứng dụng & Tính toán",
                    "question": "Một thiết bị STEM tiêu thụ công suất điện P_vào = 40.0 W và sinh ra công suất cơ học hữu ích P_ra = 34.0 W. Hiệu suất chuyển đổi năng lượng η của thiết bị là bao nhiêu?",
                    "options": ["85.0%", "74.0%", "92.5%", "68.0%"],
                    "answer": "85.0%",
                    "explanation": "Công thức hiệu suất năng lượng: η = (P_hữu ích / P_toàn phần) × 100% = (34.0 W / 40.0 W) × 100% = 0.85 × 100% = 85.0%."
                },
                "q_troubleshoot": {
                    "badge": "🔧 Xử lý Sự cố Kỹ thuật",
                    "question": "Trong quá trình vận hành liên tục, thiết bị bị nóng lên bất thường và công suất đầu ra giảm dần. Bước can thiệp kỹ thuật nào sau đây là ưu tiên hàng đầu?",
                    "options": [
                        "Kiểm tra các điểm tiếp xúc ma sát cơ khí, bổ sung tản nhiệt và bôi trơn các cụm truyền động",
                        "Tăng điện áp nguồn cấp vào gấp đôi",
                        "Bọc kín thiết bị lại bằng túi nilon để giữ nhiệt",
                        "Gõ mạnh vào thân máy để giải tỏa ứng suất"
                    ],
                    "answer": "Kiểm tra các điểm tiếp xúc ma sát cơ khí, bổ sung tản nhiệt và bôi trơn các cụm truyền động",
                    "explanation": "Quá nhiệt là biểu hiện của hao phí năng lượng Joule (I²R) hoặc ma sát tiếp xúc. Cần làm mát cưỡng bức, bôi trơn hoặc giảm dòng tải để tránh hư hại cách điện và suy giảm hiệu suất."
                },
                "q_materials": {
                    "badge": "🔬 Khoa học Vật liệu & Kết cấu",
                    "question": "Khi thiết kế một vỏ bọc cách nhiệt bảo vệ thiết bị, kỹ sư cần ưu tiên chọn vật liệu có đặc tính nhiệt học nào?",
                    "options": [
                        "Hệ số dẫn nhiệt k cực nhỏ và chứa nhiều túi khí vi mô khép kín",
                        "Hệ số dẫn nhiệt k càng lớn càng tốt",
                        "Vật liệu kim loại đặc có tỷ trọng cao",
                        "Vật liệu có khả năng dẫn điện tốt"
                    ],
                    "answer": "Hệ số dẫn nhiệt k cực nhỏ và chứa nhiều túi khí vi mô khép kín",
                    "explanation": "Theo định luật Fourier (q = -k·A·ΔT/d), nhiệt lượng truyền qua vỏ bọc tỉ lệ thuận với hệ số dẫn nhiệt k. Vật liệu cách nhiệt (như xốp EPS, bông thủy tinh) có k rất nhỏ nhờ các túi khí tĩnh cản trở truyền nhiệt đối lưu và dẫn nhiệt."
                },
                "q_data": {
                    "badge": "📊 Phân tích Dữ liệu Thực nghiệm",
                    "question": "Đo đạc thực nghiệm cho thấy thời gian xử lý bài toán tăng theo quy mô dữ liệu n như sau: n = 10 (t = 0.01s); n = 20 (t = 0.04s); n = 30 (t = 0.09s); n = 40 (t = 0.16s). Quy luật tăng trưởng thời gian này tuân theo hàm số nào?",
                    "options": [
                        "Tỉ lệ thuận với bình phương quy mô dữ liệu O(n²)",
                        "Tuyến tính bậc nhất O(n)",
                        "Hàm logarit O(log n)",
                        "Hàm số không đổi O(1)"
                    ],
                    "answer": "Tỉ lệ thuận với bình phương quy mô dữ liệu O(n²)",
                    "explanation": "Quan sát tỉ số: (0.04/0.01) = 4 = (20/10)²; (0.09/0.01) = 9 = (30/10)²; (0.16/0.01) = 16 = (40/10)². Thời gian tăng theo bình phương quy mô dữ liệu O(n²)."
                }
            }
        else:
            return {
                "law_name": "Conservation of Energy & System Optimization",
                "formula": "E_in = E_out + Q_loss  and  η = (E_useful / E_total) · 100%",
                "formula_unit": "J (Joule), W (Watt), % (Efficiency)",
                "mech": "Closed-Loop Feedback Control System",
                "metric": "System Energy Conversion Efficiency η ≥ 85%",
                "matching": [
                    {"term": "Conservation of Energy", "definition": "Energy cannot be created or destroyed, only transformed between states"},
                    {"term": "Efficiency η = (P_out / P_in) · 100%", "definition": "Percentage ratio of useful output power to total input power supplied"},
                    {"term": "Watt (W)", "definition": "Standard SI unit of power equivalent to one Joule per second"},
                    {"term": "Computational Complexity O(n)", "definition": "Mathematical notation describing algorithmic scaling as input size grows"}
                ],
                "cloze": [
                    {"text": "In any engineering transformation, total input energy equals useful work output plus thermal [dissipation] losses.", "answer": "dissipation", "options": ["dissipation", "infinity", "creation", "momentum"]},
                    {"text": "System efficiency is inevitably [lower than] 100% due to unavoidable frictional and resistive losses.", "answer": "lower than", "options": ["lower than", "greater than", "equal to", "doubled"]},
                    {"text": "A closed-loop control system utilizes [sensors] to provide feedback for automatic actuator adjustment.", "answer": "sensors", "options": ["sensors", "batteries", "conductors", "insulators"]},
                    {"text": "Engineering optimization balances performance requirements against project [constraints] and costs.", "answer": "constraints", "options": ["constraints", "blueprints", "laws", "formulas"]}
                ],
                "q_physics": {
                    "badge": "⚛️ Physics Principles & Mechanisms",
                    "question": "According to the First and Second Laws of Thermodynamics, why is a perpetual motion machine of the first kind physically impossible?",
                    "options": [
                        "Energy is strictly conserved; real systems inevitably dissipate energy as non-recoverable thermal friction",
                        "Earth's gravity field neutralizes mechanical motion after one cycle",
                        "Ambient air drains electrical charges from the chassis",
                        "Structural metal softens continuously over time"
                    ],
                    "answer": "Energy is strictly conserved; real systems inevitably dissipate energy as non-recoverable thermal friction",
                    "explanation": "Conservation of energy (E_in = E_out + Q_loss) coupled with the second law of thermodynamics dictates that energy cannot be spontaneously generated without input, rendering perpetual motion impossible."
                },
                "q_math": {
                    "badge": "📐 Applied Math & Calculation",
                    "question": "A STEM mechanism consumes input power P_in = 40.0 W and delivers useful mechanical output power P_out = 34.0 W. Calculate its energy efficiency η:",
                    "options": ["85.0%", "74.0%", "92.5%", "68.0%"],
                    "answer": "85.0%",
                    "explanation": "Efficiency equation: η = (P_useful / P_total) × 100% = (34.0 W / 40.0 W) × 100% = 0.85 × 100% = 85.0%."
                },
                "q_troubleshoot": {
                    "badge": "🔧 Engineering Troubleshooting",
                    "question": "During continuous operation, a mechanism overheats abnormally while output performance drops. What is the primary engineering response?",
                    "options": [
                        "Inspect frictional contact interfaces, add thermal heat-sinking, and lubricate transmission components",
                        "Double the input supply voltage",
                        "Wrap the machine in plastic wrap to trap the heat",
                        "Strike the chassis firmly with a hammer"
                    ],
                    "answer": "Inspect frictional contact interfaces, add thermal heat-sinking, and lubricate transmission components",
                    "explanation": "Thermal spikes indicate Joule heating (I²R) or mechanical friction. Cooling, lubrication, and load reduction are necessary to protect insulation and prevent mechanical failure."
                },
                "q_materials": {
                    "badge": "🔬 Materials & Structural Mechanics",
                    "question": "When engineering thermal insulation to protect sensitive components, what material metric is paramount?",
                    "options": [
                        "Extremely low thermal conductivity (k) containing closed micro-cellular air pockets",
                        "Maximum possible thermal conductivity",
                        "Solid heavy metallic density",
                        "High electrical conductivity"
                    ],
                    "answer": "Extremely low thermal conductivity (k) containing closed micro-cellular air pockets",
                    "explanation": "Fourier's Law dictates that conductive heat transfer q = -k·A·ΔT/d is minimized when thermal conductivity k is minimal. Cellular air pockets eliminate convective and conductive transfer."
                },
                "q_data": {
                    "badge": "📊 Empirical Data Analysis",
                    "question": "Benchmark execution time scales with input size n as follows: n = 10 (t = 0.01s); n = 20 (t = 0.04s); n = 30 (t = 0.09s); n = 40 (t = 0.16s). What computational complexity function governs this?",
                    "options": [
                        "Quadratic scaling O(n²)",
                        "Linear scaling O(n)",
                        "Logarithmic scaling O(log n)",
                        "Constant time O(1)"
                    ],
                    "answer": "Quadratic scaling O(n²)",
                    "explanation": "Comparing ratios: (0.04/0.01) = 4 = (20/10)²; (0.09/0.01) = 9 = (30/10)²; (0.16/0.01) = 16 = (40/10)². The algorithm exhibits quadratic complexity O(n²)."
                }
            }

def build_lecture_quiz_and_practice(lec, lang):
    title = lec.get("title", "")
    lp = lec.get("lessonPlan", {})
    topic_name = ""
    is_vie = (lang == "VIE")
    
    category = detect_category(title, topic_name)
    spec = get_domain_spec(category, is_vie)
    
    crits = lp.get("challenge", {}).get("criteria", [])
    constrs = lp.get("challenge", {}).get("constraints", [])
    crit_str = crits[0] if crits else ("Hoàn thành mô hình đúng thông số kỹ thuật" if is_vie else "Complete model to technical specifications")
    const_str = constrs[0] if constrs else ("Chỉ sử dụng các vật tư trong danh mục" if is_vie else "Use only permitted materials")
    
    # 1. Build Quiz Data (6 Rigorous STEM Questions)
    q1_edp = {
        "type": "multiple_choice",
        "badge": "🎯 Kỹ thuật & Thiết kế EDP" if is_vie else "🎯 Engineering Design & EDP",
        "question": f"Trong thử thách kỹ thuật '{title}', tiêu chí kỹ thuật cốt lõi (Criteria) và giới hạn (Constraints) bắt buộc mà thiết kế phải đáp ứng là gì?" if is_vie else f"In the engineering challenge '{title}', what primary technical criteria and constraints must the design satisfy?",
        "options": [
            f"Tiêu chí: {crit_str}; Ràng buộc: {const_str}" if is_vie else f"Criteria: {crit_str}; Constraints: {const_str}",
            "Sử dụng càng nhiều vật tư đắt tiền càng tốt mà không cần bản vẽ kỹ thuật" if is_vie else "Use as many expensive materials as possible without technical blueprints",
            "Chỉ cần hoàn thành nhanh nhất mà không cần đo đạc số liệu thực nghiệm" if is_vie else "Finish as fast as possible without measuring empirical telemetry",
            "Bỏ qua mọi giới hạn an toàn để mô hình đạt kích thước khổng lồ" if is_vie else "Ignore all safety boundaries to make the prototype as oversized as possible"
        ],
        "answer": f"Tiêu chí: {crit_str}; Ràng buộc: {const_str}" if is_vie else f"Criteria: {crit_str}; Constraints: {const_str}",
        "explanation": f"Trong quy trình thiết kế kỹ thuật EDP, việc xác định rõ tiêu chí ({crit_str}) và ràng buộc vật tư ({const_str}) là kim chỉ nam bắt buộc trước khi bước vào chế tạo." if is_vie else f"In the Engineering Design Process (EDP), defining criteria ({crit_str}) and constraints ({const_str}) is mandatory before fabrication."
    }
    
    q2_physics = {
        "type": "multiple_choice",
        "badge": spec["q_physics"]["badge"],
        "question": spec["q_physics"]["question"],
        "options": spec["q_physics"]["options"],
        "answer": spec["q_physics"]["answer"],
        "explanation": spec["q_physics"]["explanation"]
    }
    
    q3_math = {
        "type": "multiple_choice",
        "badge": spec["q_math"]["badge"],
        "question": spec["q_math"]["question"],
        "options": spec["q_math"]["options"],
        "answer": spec["q_math"]["answer"],
        "explanation": spec["q_math"]["explanation"]
    }
    
    q4_troubleshoot = {
        "type": "multiple_choice",
        "badge": spec["q_troubleshoot"]["badge"],
        "question": spec["q_troubleshoot"]["question"],
        "options": spec["q_troubleshoot"]["options"],
        "answer": spec["q_troubleshoot"]["answer"],
        "explanation": spec["q_troubleshoot"]["explanation"]
    }
    
    q5_materials = {
        "type": "multiple_choice",
        "badge": spec["q_materials"]["badge"],
        "question": spec["q_materials"]["question"],
        "options": spec["q_materials"]["options"],
        "answer": spec["q_materials"]["answer"],
        "explanation": spec["q_materials"]["explanation"]
    }
    
    q6_data = {
        "type": "multiple_choice",
        "badge": spec["q_data"]["badge"],
        "question": spec["q_data"]["question"],
        "options": spec["q_data"]["options"],
        "answer": spec["q_data"]["answer"],
        "explanation": spec["q_data"]["explanation"]
    }
    
    lec["quizData"] = [q1_edp, q2_physics, q3_math, q4_troubleshoot, q5_materials, q6_data]
    
    # 2. Build Practice Data
    flashcards = [
        {
            "term": spec["law_name"],
            "phonetic": "/ˌsaɪənˈtɪfɪk lɔː/",
            "definition": "Định luật khoa học vật lý chi phối cơ chế vận hành chính của dự án." if is_vie else "Core physical scientific law governing prototype mechanics.",
            "example": f"Ứng dụng {spec['law_name']} để tính toán thông số tối ưu cho {title}." if is_vie else f"Applying {spec['law_name']} to optimize parameters for {title}."
        },
        {
            "term": spec["formula"],
            "phonetic": "/ˈfɔːmjələ/",
            "definition": f"Công thức toán học tính toán định lượng đại lượng kỹ thuật ({spec['formula_unit']})." if is_vie else f"Mathematical formula calculating physical quantities ({spec['formula_unit']}).",
            "example": f"Công thức chuẩn: {spec['formula']}"
        },
        {
            "term": spec["mech"],
            "phonetic": "/ˈmekənɪzəm/",
            "definition": "Cơ cấu kỹ thuật cốt lõi giúp thiết bị chuyển động hoặc chịu lực ổn định." if is_vie else "Core engineering mechanism providing kinetic motion or structural stability.",
            "example": f"Tích hợp {spec['mech']} vào mô hình thực tế." if is_vie else f"Integrating {spec['mech']} into the physical prototype."
        },
        {
            "term": spec["metric"],
            "phonetic": "/ˈmetrɪk/",
            "definition": "Chỉ số kỹ thuật tiêu chuẩn dùng để kiểm định chất lượng và an toàn sản phẩm." if is_vie else "Benchmark engineering metric validating safety and performance compliance.",
            "example": f"Mô hình đạt yêu cầu khi thỏa mãn chỉ số: {spec['metric']}" if is_vie else f"Prototype validated when satisfying metric: {spec['metric']}"
        }
    ]
    
    sequencing = [
        {
            "stepNumber": 1,
            "instruction": "Thu thập số liệu đo lường, xác định đại lượng đã biết và ẩn số cần tìm kèm đổi về đơn vị SI." if is_vie else "Collect experimental measurements, identify knowns/unknowns, and convert to standard SI units."
        },
        {
            "stepNumber": 2,
            "instruction": "Thiết lập phương trình cân bằng lực hoặc định luật vật lý tương ứng với cơ chế mô hình." if is_vie else "Formulate governing physics equilibrium equations or physical laws matching the prototype mechanism."
        },
        {
            "stepNumber": 3,
            "instruction": "Biến đổi đại số để cô lập ẩn số kỹ thuật và thay số đo thực nghiệm vào công thức tính toán." if is_vie else "Perform algebraic manipulation to isolate the technical variable and substitute empirical data."
        },
        {
            "stepNumber": 4,
            "instruction": "Tính toán kết quả chính xác, đánh giá sai số thực nghiệm và đối chiếu với ngưỡng an toàn kỹ thuật." if is_vie else "Calculate final numerical results, evaluate percentage errors, and verify safety factor limits."
        }
    ]
    
    lec["practiceData"] = {
        "flashcards": flashcards,
        "matching": spec["matching"],
        "sequencing": sequencing,
        "cloze": spec["cloze"]
    }

print("Enricher logic prepared.")

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

count = 0
for lvl in data:
    for lang in lvl.get("languages", []):
        lang_code = lang.get("lang", "VIE")
        for t in lang.get("topics", []):
            for lec in t.get("lectures", []):
                build_lecture_quiz_and_practice(lec, lang_code)
                count += 1

print(f"Successfully enriched all {count} lessons with deep technical, math, and physics content!")

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("data.js", "w", encoding="utf-8") as f:
    f.write("// STEM LMS Global Curriculum Dataset (Enriched Math & Physics)\n")
    f.write("window.APP_DATA = ")
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print("Successfully written to data.json and mirrored to data.js!")
