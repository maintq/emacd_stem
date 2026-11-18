#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master STEM Curriculum Practice & Assessment Generator
Generates dedicated, mathematically precise, physics-grounded questions
and practice activities across all 12 STEM domains for 450 lessons.
"""

import json

def detect_category(title, topic_name):
    s = ((title or "") + " " + (topic_name or "")).lower()
    if any(k in s for k in ["drone", "máy bay", "tên lửa", "dù lượn", "phi thuyền", "khí cầu", "rocket", "plane", "aerospace", "parachute", "glider", "wing", "flight", "hàng không", "không lưu", "aviation", "air traffic", "fly"]):
        return "aerospace"
    if any(k in s for k in ["thuyền", "tàu thủy", "chìm nổi", "phao", "submarine", "boat", "ship", "buoyancy", "sail", "thủy sinh", "biển", "nước", "watermill", "cối xay nước", "ocean", "marine", "hydro", "flotation", "raft"]):
        return "marine"
    if any(k in s for k in ["cầu", "bridge", "vòm", "giàn", "trụ cầu", "tháp", "tower", "kết cấu", "chịu lực", "trọng tải", "mái nhà", "nhà", "beam", "truss", "arch", "building", "structure"]):
        return "bridge"
    if any(k in s for k in ["gió", "mặt trời", "năng lượng", "solar", "wind", "turbine", "cối xay gió", "renewable", "energy", "sun"]):
        return "energy_renewable"
    if any(k in s for k in ["mạch", "led", "dây dẫn", "công tắc", "điện trở", "circuit", "voltage", "pin", "battery", "sensor", "cảm biến", "điện", "electric", "ohm", "switch", "wire", "resistor"]):
        return "circuit"
    if any(k in s for k in ["lọc", "nước sạch", "filter", "filtration", "môi trường", "chất thải", "ô nhiễm", "đất", "water purify", "tái chế", "recycle", "waste", "clean water"]):
        return "filtration"
    if any(k in s for k in ["robot", "cánh tay", "băng chuyền", "tự động", "gripper", "pneumatic", "khí nén", "hydraulic", "thủy lực", "robotic", "automation", "arm", "conveyor"]):
        return "robotics"
    if any(k in s for k in ["con quay", "ròng rọc", "bánh răng", "đòn bẩy", "pulley", "gear", "lever", "cam", "cơ cấu", "máy móc", "con lắc", "pendulum", "simple machine", "machine"]):
        return "mechanism"
    if any(k in s for k in ["vật liệu", "polyme", "composite", "cách nhiệt", "cách âm", "bao bì", "túi", "chống sốc", "áo giáp", "keo", "slime", "nano", "tinh thể", "crystal", "material", "plastic", "copper plating", "mạ đồng"]):
        return "materials_science"
    if any(k in s for k in ["máy tính", "thuật toán", "mã hóa", "binary", "computer", "scratch", "code", "logic", "mạng", "mã vạch", "barcode", "html", "computing", "algorithm", "mouse"]):
        return "computing"
    if any(k in s for k in ["xe", "ô tô", "car", "vehicle", "tốc độ", "ma sát", "dây cao su", "balloon car", "xe đua", "speed", "friction", "road", "chassis"]):
        return "vehicle"
    return "biology"

# All 12 Domains Specs
DOMAINS = {
    "aerospace": {
        "vie": {
            "law_name": "Định luật Bernoulli & Lực nâng Khí động học",
            "formula": "L = (1/2) · ρ · v² · S · Cl",
            "formula_unit": "N (Newton)",
            "mech": "Biên dạng cánh khí động & Cánh tà đuôi (Airfoil & Elevator)",
            "metric": "Tỷ số Lực nâng/Lực cản (L/D) ≥ 6.0",
            "matching": [
                {"term": "L = (1/2) · ρ · v² · S · Cl", "definition": "Công thức tính lực nâng khí động học theo vận tốc và diện tích cánh"},
                {"term": "Định luật III Newton", "definition": "Cánh đẩy luồng khí xuống dưới tạo phản lực nâng cánh bay lên trên"},
                {"term": "Đơn vị Newton (N)", "definition": "Đơn vị đo lực nâng (Lift) và lực cản (Drag) trong hệ SI"},
                {"term": "Tỷ số L/D (Glide Ratio)", "definition": "Đại lượng đo lường hiệu suất lướt xa của tàu lượn từ độ cao ban đầu"}
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
                "explanation": "Độ cong của mặt trên cánh làm đường dòng khí lưu thông nhanh hơn, tạo áp suất tĩnh thấp hơn áp suất mặt dưới theo phương trình Bernoulli: p + 1/2·ρ·v² = const. Chênh lệch áp suất này tạo lực nâng thẳng đứng."
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
            "law_name": "Định luật Ohm & Mạch Điện Đa Nhánh",
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
            "law_name": "Ohm's Law & Circuit Analysis",
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
    "energy_renewable": {
        "vie": {
            "law_name": "Năng lượng Tái tạo & Định luật Khí động học Gió Betz",
            "formula": "P_gió = (1/2) · ρ · A · v³  và  P_quang = η · A · G",
            "formula_unit": "W (Watt), J (Joule)",
            "mech": "Rotor cánh turbine xoắn & Biến tần nghịch lưu (Inverter)",
            "metric": "Giới hạn lý thuyết Betz Cp_max = 59.3%",
            "matching": [
                {"term": "P = (1/2) · ρ · A · v³", "definition": "Công suất gió tỉ lệ với diện tích quét cánh quạt và lập phương vận tốc gió (v³)"},
                {"term": "P_quang = η · A · G", "definition": "Công suất điện mặt trời bằng diện tích tấm pin nhân bức xạ và hiệu suất quang điện"},
                {"term": "Giới hạn Betz (59.3%)", "definition": "Hiệu suất khí động học cực đại theo lý thuyết của một tuabin gió trong khí quyển"},
                {"term": "Đơn vị Watt (W)", "definition": "Đơn vị đo công suất phát điện tương đương 1 Joule năng lượng trên 1 giây"}
            ],
            "cloze": [
                {"text": "Công suất động năng của gió tỉ lệ với [lập phương] vận tốc gió; nếu vận tốc gió tăng gấp đôi thì công suất gió tăng gấp tám lần.", "answer": "lập phương", "options": ["lập phương", "bình phương", "căn bậc hai", "tỉ lệ nghịch"]},
                {"text": "Theo giới hạn Betz, một cánh quạt tuabin gió lý tưởng chỉ có thể trích xuất tối đa [59.3%] động năng của luồng gió thổi qua.", "answer": "59.3%", "options": ["59.3%", "100%", "85.0%", "50.0%"]},
                {"text": "Tấm pin quang điện chuyển đổi trực tiếp năng lượng ánh sáng mặt trời thành dòng điện [một chiều] (DC).", "answer": "một chiều", "options": ["một chiều", "xoay chiều", "từ tính", "nhiệt năng"]},
                {"text": "Góc nghiêng tối ưu của tấm pin mặt trời được điều chỉnh theo [vĩ độ] địa lý để đón bức xạ vuông góc lớn nhất.", "answer": "vĩ độ", "options": ["vĩ độ", "kinh độ", "độ cao", "áp suất"]}
            ],
            "q_physics": {
                "badge": "⚛️ Vật lý & Nguyên lý Cơ chế",
                "question": "Tại sao khi vận tốc gió tăng gấp 2 lần (từ 3 m/s lên 6 m/s), công suất năng lượng gió có thể tạo ra lại tăng vọt gấp 8 lần?",
                "options": [
                    "Vì công suất gió tỉ lệ với lập phương vận tốc gió P ∝ v³ (vừa tăng lưu lượng khối lượng gió, vừa tăng động năng mỗi kg gió)",
                    "Vì không khí bị nóng lên gấp đôi khi gió thổi mạnh",
                    "Vì cánh tuabin gió tự động dài thêm gấp đôi khi gió mạnh",
                    "Do ma sát giữa không khí và mặt đất giảm về 0"
                ],
                "answer": "Vì công suất gió tỉ lệ với lập phương vận tốc gió P ∝ v³ (vừa tăng lưu lượng khối lượng gió, vừa tăng động năng mỗi kg gió)",
                "explanation": "Lưu lượng khối lượng gió qua rotor dm/dt = ρ·A·v tỉ lệ với v, trong khi động năng riêng 1/2·v² tỉ lệ với v². Do đó công suất P = 1/2·(dm/dt)·v² = 1/2·ρ·A·v³ (tỉ lệ với lập phương v³, 2³ = 8)."
            },
            "q_math": {
                "badge": "📐 Toán học Ứng dụng & Tính toán",
                "question": "Một tấm pin năng lượng mặt trời có diện tích A = 0.04 m², hiệu suất quang điện η = 15% (0.15), đặt dưới cường độ bức xạ mặt trời G = 800 W/m². Công suất điện P sinh ra là bao nhiêu?",
                "options": ["4.80 W", "6.40 W", "12.00 W", "3.20 W"],
                "answer": "4.80 W",
                "explanation": "Áp dụng công thức: P = η · A · G = 0.15 × 0.04 m² × 800 W/m² = 4.80 W."
            },
            "q_troubleshoot": {
                "badge": "🔧 Xử lý Sự cố Kỹ thuật",
                "question": "Khi gió thổi rất mạnh, tuabin gió mini quay nhanh nhưng điện áp phát ra từ máy phát điện một chiều bị sụt giảm bất thường. Nguyên nhân kỹ thuật nào sau đây là chuẩn xác?",
                "options": [
                    "Hiện tượng trượt chổi than tiếp điện hoặc dây curoa truyền động bị trượt do mô-men cản vượt quá ma sát bám",
                    "Gió quá mạnh làm electron trong dây đồng bị thổi bay mất",
                    "Không khí bị ion hóa làm chập mạch cuộn cảm",
                    "Từ trường của nam châm vĩnh cửu bị biến mất hoàn toàn"
                ],
                "answer": "Hiện tượng trượt chổi than tiếp điện hoặc dây curoa truyền động bị trượt do mô-men cản vượt quá ma sát bám",
                "explanation": "Khi tốc độ quay cao, lực ly tâm và mô-men xoắn lớn làm dây curoa bị trượt trên puli hoặc chổi than tiếp điện bị rung lắc nảy khỏi cổ góp, làm tăng điện trở tiếp xúc và sụt áp."
            },
            "q_materials": {
                "badge": "🔬 Khoa học Vật liệu & Kết cấu",
                "question": "Tại sao cánh quạt tuabin gió hiện đại thường được chế tạo bằng vật liệu composite sợi thủy tinh hoặc sợi carbon thay vì thép hoặc gỗ đặc?",
                "options": [
                    "Vật liệu composite có độ bền mỏi (Fatigue strength) cực cao, kháng ăn mòn thời tiết và trọng lượng nhẹ để giảm mô-men quán tính khởi động",
                    "Vì sợi carbon có khả năng tự phát sinh điện từ gió",
                    "Vì sợi thủy tinh có giá thành rẻ hơn bùn đất",
                    "Để cánh quạt có thể uốn cong 360 độ mà không gãy"
                ],
                "answer": "Vật liệu composite có độ bền mỏi (Fatigue strength) cực cao, kháng ăn mòn thời tiết và trọng lượng nhẹ để giảm mô-men quán tính khởi động",
                "explanation": "Cánh tuabin phải chịu hàng triệu chu kỳ uốn khí động học. Composite sợi carbon/thủy tinh nhẹ giúp giảm tải trọng quán tính ly tâm và chịu mỏi cơ học tốt hơn kim loại."
            },
            "q_data": {
                "badge": "📊 Phân tích Dữ liệu Thực nghiệm",
                "question": "Đo công suất phát điện theo số lượng cánh quạt: 2 cánh (P = 3.2W); 3 cánh (P = 4.5W); 4 cánh (P = 4.6W); 6 cánh (P = 3.8W). Tại sao cấu hình 3 cánh lại là tiêu chuẩn công nghiệp phổ biến nhất?",
                "options": [
                    "Cấu hình 3 cánh đạt điểm tối ưu giữa hiệu suất khí động học cao, độ cân bằng động học tuyệt hảo và tiết kiệm chi phí vật liệu",
                    "Vì 3 cánh luôn tạo ra công suất điện gấp mười lần 4 cánh",
                    "Vì gió chỉ có thể thổi qua các khoảng trống chia hết cho 3",
                    "Do quy định ngẫu nhiên trong hội họa cổ điển"
                ],
                "answer": "Cấu hình 3 cánh đạt điểm tối ưu giữa hiệu suất khí động học cao, độ cân bằng động học tuyệt hảo và tiết kiệm chi phí vật liệu",
                "explanation": "3 cánh cung cấp mô-men quán tính phân bố đối xứng qua 3 trục cách đều 120°, triệt tiêu rung động con quay (gyroscopic precession) khi đổi hướng đón gió, mang lại độ bền cơ học cao nhất."
            }
        },
        "eng": {
            "law_name": "Renewable Energy & Betz's Law",
            "formula": "P_wind = (1/2) · ρ · A · v³  and  P_solar = η · A · G",
            "formula_unit": "W (Watt), J (Joule)",
            "mech": "Twisted Airfoil Rotor & Inverter Regulation",
            "metric": "Betz Theoretical Limit Cp_max = 59.3%",
            "matching": [
                {"term": "P = (1/2) · ρ · A · v³", "definition": "Wind power proportional to swept area and wind velocity cubed (v³)"},
                {"term": "P_solar = η · A · G", "definition": "Solar power equals area times irradiance times photovoltaic efficiency"},
                {"term": "Betz Limit (59.3%)", "definition": "Maximum theoretical kinetic energy extractable by a wind rotor"},
                {"term": "Watt (W)", "definition": "Standard SI unit of power representing one Joule of energy per second"}
            ],
            "cloze": [
                {"text": "Wind kinetic power scales with the [cube] of wind velocity; doubling velocity multiplies power by eightfold.", "answer": "cube", "options": ["cube", "square", "square root", "reciprocal"]},
                {"text": "According to Betz's limit, a turbine rotor can capture at most [59.3%] of incoming wind kinetic energy.", "answer": "59.3%", "options": ["59.3%", "100%", "85.0%", "50.0%"]},
                {"text": "Photovoltaic cells convert incident sunlight photons directly into [direct current] (DC) electricity.", "answer": "direct current", "options": ["direct current", "alternating current", "magnetic", "thermal"]},
                {"text": "Solar panel tilt angles are calibrated relative to geographical [latitude] to maximize normal irradiance.", "answer": "latitude", "options": ["latitude", "longitude", "altitude", "pressure"]}
            ],
            "q_physics": {
                "badge": "⚛️ Physics Principles & Mechanisms",
                "question": "Why does doubling wind velocity from 3 m/s to 6 m/s produce an eightfold surge in available wind power?",
                "options": [
                    "Wind power scales cubically with velocity P ∝ v³ (both mass flow rate and kinetic energy per kg scale with speed)",
                    "Air temperature automatically doubles at higher wind speeds",
                    "Rotor blades double in physical span in high winds",
                    "Ground friction disappears completely"
                ],
                "answer": "Wind power scales cubically with velocity P ∝ v³ (both mass flow rate and kinetic energy per kg scale with speed)",
                "explanation": "Mass flow rate dm/dt = ρ·A·v scales with v, while kinetic energy per unit mass 1/2·v² scales with v². Hence P = 1/2·(dm/dt)·v² = 1/2·ρ·A·v³ (2³ = 8)."
            },
            "q_math": {
                "badge": "📐 Applied Math & Calculation",
                "question": "A photovoltaic cell has surface area A = 0.04 m², efficiency η = 15% (0.15), and receives solar irradiance G = 800 W/m². Calculate power output P:",
                "options": ["4.80 W", "6.40 W", "12.00 W", "3.20 W"],
                "answer": "4.80 W",
                "explanation": "Using P = η · A · G = 0.15 × 0.04 m² × 800 W/m² = 4.80 W."
            },
            "q_troubleshoot": {
                "badge": "🔧 Engineering Troubleshooting",
                "question": "During high wind trials, the turbine spins rapidly but generator terminal voltage drops sharply. What is the probable mechanical cause?",
                "options": [
                    "Drive belt slippage or commutator brush bounce under excessive torque and centrifugal force",
                    "Electrons being blown out of the copper coil wires",
                    "Atmospheric ionization shorting the rotor windings",
                    "Permanent magnets spontaneously losing all magnetic flux"
                ],
                "answer": "Drive belt slippage or commutator brush bounce under excessive torque and centrifugal force",
                "explanation": "High rotational speeds induce belt slip or brush chatter, causing intermittent electrical contact and sharp voltage drop."
            },
            "q_materials": {
                "badge": "🔬 Materials & Structural Mechanics",
                "question": "Why are commercial wind turbine blades fabricated from carbon or glass fiber reinforced polymers rather than solid metals?",
                "options": [
                    "Composite materials provide superior cyclic fatigue resistance, environmental corrosion immunity, and low rotational inertia",
                    "Carbon fibers generate their own auxiliary electrical current",
                    "Fiberglass costs less than plain soil",
                    "So blades can twist 360 degrees without damage"
                ],
                "answer": "Composite materials provide superior cyclic fatigue resistance, environmental corrosion immunity, and low rotational inertia",
                "explanation": "Rotor blades endure millions of aeroelastic flexural load cycles. Carbon/glass composites resist fatigue failure while keeping rotational mass low."
            },
            "q_data": {
                "badge": "📊 Empirical Data Analysis",
                "question": "Power generation data records: 2 blades (3.2W); 3 blades (4.5W); 4 blades (4.6W); 6 blades (3.8W). Why is the 3-bladed configuration the global industry standard?",
                "options": [
                    "3 blades deliver an optimal balance of high aerodynamic efficiency, gyroscopic rotational balance, and material economy",
                    "3 blades generate tenfold more power than 4 blades",
                    "Wind only travels through gaps divisible by 3",
                    "Historical architectural convention"
                ],
                "answer": "3 blades deliver an optimal balance of high aerodynamic efficiency, gyroscopic rotational balance, and material economy",
                "explanation": "A 3-bladed rotor possesses symmetric polar moments of inertia spaced at 120°, eliminating gyroscopic yaw vibration during wind tracking."
            }
        }
    }
}

print("Specs dictionary built.")
