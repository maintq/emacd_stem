#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re
import random

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

# Domain specs for Mathematics & Physics Practice & Test
DOMAIN_SPECS = {
    "aerospace": {
        "vie": {
            "law": "Định luật Bernoulli & Lực nâng Khí động học",
            "formula": "L = (1/2) · ρ · v² · S · Cl",
            "formula_desc": "Lực nâng tỉ lệ thuận với mật độ không khí (ρ), bình phương vận tốc (v²), diện tích cánh (S) và hệ số lực nâng (Cl).",
            "mech": "Cánh tà & Cánh đuôi cân bằng (Aileron & Stabilizer)",
            "metric": "Tỷ số Lực nâng trên Lực cản (L/D Ratio) ≥ 6.0",
            "math_q": {
                "question": "Một mô hình máy bay lượn có diện tích cánh S = 0.05 m², bay trong không khí (mật độ ρ = 1.2 kg/m³) với vận tốc v = 6.0 m/s. Biết hệ số lực nâng Cl = 0.8. Hãy tính độ lớn lực nâng khí động học L tác dụng lên máy bay:",
                "options": ["0.864 N", "1.728 N", "0.432 N", "2.160 N"],
                "answer": "0.864 N",
                "explanation": "Áp dụng công thức lực nâng khí động học: L = (1/2) · ρ · v² · S · Cl = 0.5 × 1.2 × (6.0)² × 0.05 × 0.8 = 0.6 × 36 × 0.04 = 0.864 N."
            },
            "physics_q": {
                "question": "Theo nguyên lý Bernoulli và định luật III Newton, hiện tượng nào là nguyên nhân trực tiếp tạo ra lực nâng (Lift) hướng lên trên một cánh máy bay có biên dạng khí động học?",
                "options": [
                    "Vận tốc luồng khí mặt trên cánh nhanh hơn mặt dưới, tạo ra vùng áp suất thấp ở mặt trên kéo cánh lên",
                    "Khối lượng không khí bên dưới cánh luôn ấm hơn không khí bên trên",
                    "Lực ma sát tiếp xúc giữa không khí và bề mặt cánh triệt tiêu trọng lực",
                    "Không khí bên trên cánh bị nén chặt lại làm tăng áp suất nén cánh xuống"
                ],
                "answer": "Vận tốc luồng khí mặt trên cánh nhanh hơn mặt dưới, tạo ra vùng áp suất thấp ở mặt trên kéo cánh lên",
                "explanation": "Biên dạng cong của mặt trên cánh làm các đường dòng khí chuyển động nhanh hơn, tạo ra áp suất tĩnh thấp hơn áp suất mặt dưới theo định luật Bernoulli. Hiệu áp suất này kết hợp góc tấn (Angle of Attack) sinh ra lực nâng."
            },
            "troubleshoot_q": {
                "question": "Trong các lần bay thử nghiệm, mô hình tàu lượn liên tục bị chúi mũi xuống đất ngay sau khi phóng (nguyên nhân mất ổn định dọc). Giải pháp kỹ thuật nào sau đây là chuẩn xác nhất?",
                "options": [
                    "Dời trọng tâm (CG) lùi về phía sau hoặc uốn cong nhẹ mép sau cánh đuôi ngang lên trên (Elevator Up)",
                    "Tăng thêm trọng lượng dằn ở ngay chóp mũi tàu lượn",
                    "Cắt ngắn sải cánh chính để giảm diện tích nâng",
                    "Gia tăng lực ném cực mạnh khi phóng mô hình"
                ],
                "answer": "Dời trọng tâm (CG) lùi về phía sau hoặc uốn cong nhẹ mép sau cánh đuôi ngang lên trên (Elevator Up)",
                "explanation": "Khi mũi bị chúi (nose-heavy), trọng tâm (Center of Gravity) đang nằm quá xa về phía trước so với tâm áp lực khí động (Center of Pressure). Cần đưa trọng tâm lùi về sau hoặc nâng cánh lái đuôi để tạo mô-men ngóc mũi lên."
            },
            "materials_q": {
                "question": "Khi lựa chọn vật liệu chế tạo cánh và thân cho mô hình khí động học, chỉ số kỹ thuật nào quan trọng nhất để tối ưu hóa hiệu suất bay?",
                "options": [
                    "Tỷ số giữa độ bền trên trọng lượng riêng (Strength-to-Weight Ratio) cao và độ cứng chống vặn xoắn",
                    "Khối lượng riêng càng lớn càng tốt để tăng quán tính đâm xuyên",
                    "Vật liệu có khả năng dẫn điện tốt để giảm ma sát",
                    "Vật liệu hoàn toàn dẻo mềm có thể biến dạng tự do theo gió"
                ],
                "answer": "Tỷ số giữa độ bền trên trọng lượng riêng (Strength-to-Weight Ratio) cao và độ cứng chống vặn xoắn",
                "explanation": "Trong kỹ thuật hàng không vũ trụ, vật liệu lý tưởng (như balsa, xốp EPP, sợi carbon) phải nhẹ nhất có thể để giảm trọng lực nhưng phải đủ độ cứng vững (rigidity) để không bị biến dạng hình học dưới tải trọng khí động."
            },
            "data_q": {
                "question": "Một nhóm kỹ sư đo được góc tấn α = 4° cho tỷ số L/D = 8, góc tấn α = 8° cho L/D = 10, nhưng khi tăng góc tấn lên α = 16° thì lực nâng giảm đột ngột và lực cản tăng vọt. Hiện tượng vật lý này gọi là gì?",
                "options": [
                    "Hiện tượng thất tốc khí động học (Aerodynamic Stall) do bong tróc dòng khí",
                    "Hiện tượng cộng hưởng cơ học tần số cao",
                    "Hiện tượng siêu âm phá vỡ rào cản âm thanh",
                    "Hiện tượng mất trọng lực cục bộ"
                ],
                "answer": "Hiện tượng thất tốc khí động học (Aerodynamic Stall) do bong tróc dòng khí",
                "explanation": "Khi vượt quá góc tấn giới hạn (Critical Angle of Attack, thường khoảng 12° - 15°), dòng khí không còn bám dính vào bề mặt trên của cánh mà bị tách rời xoáy loạn, gây sụt giảm lực nâng nghiêm trọng và tăng vọt lực cản (Stall)."
            }
        },
        "eng": {
            "law": "Bernoulli's Principle & Aerodynamic Lift",
            "formula": "L = (1/2) · ρ · v² · S · Cl",
            "formula_desc": "Aerodynamic lift is proportional to air density (ρ), velocity squared (v²), wing surface area (S), and lift coefficient (Cl).",
            "mech": "Aileron & Horizontal Stabilizer",
            "metric": "Lift-to-Drag Ratio (L/D Ratio) ≥ 6.0",
            "math_q": {
                "question": "A model glider has a wing area S = 0.05 m² and flies through air (density ρ = 1.2 kg/m³) at a velocity v = 6.0 m/s. Given a lift coefficient Cl = 0.8, calculate the aerodynamic lift force L:",
                "options": ["0.864 N", "1.728 N", "0.432 N", "2.160 N"],
                "answer": "0.864 N",
                "explanation": "Using the aerodynamic lift equation: L = (1/2) · ρ · v² · S · Cl = 0.5 × 1.2 × (6.0)² × 0.05 × 0.8 = 0.6 × 36 × 0.04 = 0.864 N."
            },
            "physics_q": {
                "question": "According to Bernoulli's principle and Newton's Third Law, which mechanism directly produces aerodynamic lift on a cambered airfoil?",
                "options": [
                    "Air travels faster over the curved upper surface, creating a localized low-pressure zone above the wing",
                    "Air underneath the wing is warmer than above the wing",
                    "Skin friction drag completely cancels gravitational pull",
                    "Air above the wing compresses, forcing the wing downward"
                ],
                "answer": "Air travels faster over the curved upper surface, creating a localized low-pressure zone above the wing",
                "explanation": "The cambered curvature forces air over the upper surface to accelerate, reducing static pressure in accordance with Bernoulli's equation. This pressure differential combined with downward flow deflection generates upward lift."
            },
            "troubleshoot_q": {
                "question": "During test flights, a prototype glider persistently pitches downwards into the ground immediately after release. What is the most effective engineering solution?",
                "options": [
                    "Shift the Center of Gravity (CG) slightly aft, or apply positive elevator deflection (trim tabs up)",
                    "Add more ballast weight to the extreme tip of the nose",
                    "Shorten the wingspan to minimize lifting area",
                    "Throw the glider with excessive kinetic force"
                ],
                "answer": "Shift the Center of Gravity (CG) slightly aft, or apply positive elevator deflection (trim tabs up)",
                "explanation": "Nose-diving indicates the Center of Gravity is situated too far forward relative to the Center of Pressure. Relocating ballast aft or deflecting the horizontal stabilizer upward restores longitudinal trim."
            },
            "materials_q": {
                "question": "When selecting materials for an aerodynamic airframe, which engineering index is most critical?",
                "options": [
                    "High strength-to-weight ratio combined with torsional rigidity",
                    "Maximum volumetric density to increase penetration inertia",
                    "High electrical conductivity to dissipate friction",
                    "High flexibility that deforms freely under crosswinds"
                ],
                "answer": "High strength-to-weight ratio combined with torsional rigidity",
                "explanation": "Aerospace materials must minimize total structural mass while sustaining flight loads without geometric distortion or flutter."
            },
            "data_q": {
                "question": "Telemetry indicates that increasing angle of attack beyond α = 15° causes a sudden collapse in lift accompanied by a surge in drag. What physical aerodynamic phenomenon causes this?",
                "options": [
                    "Aerodynamic Stall caused by boundary-layer flow separation",
                    "Structural mechanical harmonic resonance",
                    "Supersonic sonic boom wave formation",
                    "Localized micro-gravity pocket"
                ],
                "answer": "Aerodynamic Stall caused by boundary-layer flow separation",
                "explanation": "Exceeding the critical angle of attack causes boundary layer airflow to separate from the upper wing surface into turbulent vortices, resulting in sudden stall."
            }
        }
    },
    "marine": {
        "vie": {
            "law": "Nguyên lý Ác-si-mét & Cân bằng Thủy tĩnh",
            "formula": "Fb = ρ_lỏng · V_chìm · g",
            "formula_desc": "Lực đẩy Ác-si-mét (Fb) bằng trọng lượng phần chất lỏng bị vật chiếm chỗ.",
            "mech": "Khoang dằn & Vỏ thuyền biên dạng chữ V (Ballast & Displacement Hull)",
            "metric": "Chiều cao tâm định vị (Metacentric Height GM) > 0",
            "math_q": {
                "question": "Một mô hình thuyền có thể tích khoang ngập nước tối đa V = 0.0005 m³ (500 ml). Biết khối lượng riêng của nước ρ = 1000 kg/m³ và gia tốc trọng trường g = 9.8 m/s². Tính lực đẩy Ác-si-mét cực đại Fb tác dụng lên thuyền khi ngập nước:",
                "options": ["4.90 N", "9.80 N", "2.45 N", "0.50 N"],
                "answer": "4.90 N",
                "explanation": "Áp dụng định luật Ác-si-mét: Fb = ρ · V · g = 1000 kg/m³ × 0.0005 m³ × 9.8 m/s² = 4.90 N."
            },
            "physics_q": {
                "question": "Một chiếc tàu chở hàng bằng thép nổi được trên mặt nước trong khi một khối thép đặc cùng khối lượng sẽ chìm ngay lập tức. Nguyên lý vật lý nào giải thích điều này?",
                "options": [
                    "Tàu có khoang rỗng lớn giúp tăng thể tích chiếm nước, làm khối lượng riêng trung bình nhỏ hơn khối lượng riêng của nước",
                    "Thép làm vỏ tàu có khối lượng riêng nhẹ hơn thép đặc bình thường",
                    "Sức căng bề mặt của nước biển giữ con tàu nổi lên trên",
                    "Động cơ của tàu liên tục đẩy nước xuống dưới để tạo phản lực"
                ],
                "answer": "Tàu có khoang rỗng lớn giúp tăng thể tích chiếm nước, làm khối lượng riêng trung bình nhỏ hơn khối lượng riêng của nước",
                "explanation": "Điều kiện nổi là trọng lượng của vật bằng lực đẩy Ác-si-mét (P = Fb = ρ_nước · V_chìm · g). Khoang rỗng làm thể tích V tăng vọt, kéo khối lượng riêng trung bình của toàn tàu (m/V) xuống thấp hơn nước nên tàu nổi vững vàng."
            },
            "troubleshoot_q": {
                "question": "Trong thử nghiệm tải trọng, thuyền có xu hướng bị lật nghiêng sang một bên khi chất thêm hàng (mất ổn định ngang). Kỹ sư cần cải tiến kết cấu như thế nào?",
                "options": [
                    "Hạ thấp trọng tâm (CG) của hàng hóa xuống đáy thuyền và mở rộng bề ngang thân thuyền (Beam width)",
                    "Chất hàng hóa lên cao hơn để tạo tháp thăng bằng",
                    "Thu hẹp chiều rộng đáy thuyền thành hình tam giác nhọn",
                    "Gọt mỏng thành thuyền để giảm bớt lực cản nước"
                ],
                "answer": "Hạ thấp trọng tâm (CG) của hàng hóa xuống đáy thuyền và mở rộng bề ngang thân thuyền (Beam width)",
                "explanation": "Để tàu ổn định chống lật, tâm định vị (Metacenter M) phải nằm phía trên trọng tâm (Center of Gravity G), tức GM > 0. Hạ thấp hàng xuống sát đáy làm giảm chiều cao G, đồng thời mở rộng mạn thuyền làm tăng mô-men hồi phục chống nghiêng."
            },
            "materials_q": {
                "question": "Vật liệu làm gioăng chống thấm và lớp phủ vỏ tàu trong môi trường nước cần đạt tiêu chuẩn kỹ thuật nào?",
                "options": [
                    "Kháng nước kỵ nước (Hydrophobic), chống ăn mòn hóa học và duy trì độ kín khít cơ học",
                    "Khả năng hút nước nhanh để tăng tải trọng ngập sâu",
                    "Độ xốp bọt khí mở để nước thấm qua tự do",
                    "Dẫn nhiệt cực nhanh để cân bằng nhiệt độ đáy biển"
                ],
                "answer": "Kháng nước kỵ nước (Hydrophobic), chống ăn mòn hóa học và duy trì độ kín khít cơ học",
                "explanation": "Vật liệu trong hàng hải cần chống thấm tuyệt đối, không bị phân rã hoặc trương nở khi ngâm lâu trong nước và chịu được áp suất thủy tĩnh mà không bị rò rỉ."
            },
            "data_q": {
                "question": "Thực nghiệm cho thấy: Khi khối lượng tải là 100g, mớn nước (chiều sâu chìm) là 1.2 cm; khi tải là 200g, mớn nước là 2.4 cm; khi tải là 300g, mớn nước là 3.6 cm. Nhận xét nào sau đây phản ánh chính xác quy luật vật lý?",
                "options": [
                    "Mớn nước tỉ lệ thuận tuyến tính với khối lượng tải trọng đặt lên thuyền",
                    "Mớn nước tăng theo hàm số mũ bậc hai so với tải trọng",
                    "Độ chìm của thuyền không phụ thuộc vào tải trọng chở theo",
                    "Lực đẩy Ác-si-mét giảm dần khi tải trọng tăng lên"
                ],
                "answer": "Mớn nước tỉ lệ thuận tuyến tính với khối lượng tải trọng đặt lên thuyền",
                "explanation": "Với thân thuyền có tiết diện ngang đều đặn (thân hộp), thể tích ngập nước V = S_đáy · h_chìm. Khi cân bằng nổi: P = Fb ⇔ m · g = ρ · S_đáy · h_chìm · g ⇒ h_chìm = m / (ρ · S_đáy), tức độ chìm tỉ lệ thuận tuyến tính với tải trọng."
            }
        },
        "eng": {
            "law": "Archimedes' Principle & Hydrostatic Equilibrium",
            "formula": "Fb = ρ_fluid · V_submerged · g",
            "formula_desc": "Buoyant force equals the weight of fluid displaced by the submerged portion of the hull.",
            "mech": "Ballast Compartment & V-Hull Geometry",
            "metric": "Metacentric Height (GM) > 0",
            "math_q": {
                "question": "A model boat hull displaces a maximum submerged volume V = 0.0005 m³ (500 mL). Given water density ρ = 1000 kg/m³ and gravitational acceleration g = 9.8 m/s², calculate the maximum buoyant force Fb:",
                "options": ["4.90 N", "9.80 N", "2.45 N", "0.50 N"],
                "answer": "4.90 N",
                "explanation": "Applying Archimedes' principle: Fb = ρ · V · g = 1000 kg/m³ × 0.0005 m³ × 9.8 m/s² = 4.90 N."
            },
            "physics_q": {
                "question": "Why does a steel cargo ship float effortlessly while a solid steel sphere of identical mass sinks immediately?",
                "options": [
                    "The ship's hollow hull increases total displaced volume, lowering average density below that of water",
                    "Ship steel has a lower intrinsic atomic mass than sphere steel",
                    "Surface tension alone supports the ship's entire displacement",
                    "Propellers constantly pump water downward to generate vertical thrust"
                ],
                "answer": "The ship's hollow hull increases total displaced volume, lowering average density below that of water",
                "explanation": "Flotation occurs when buoyant force equals weight. The internal hollow compartment vastly expands displaced volume V, reducing average density (m/V) below fluid density."
            },
            "troubleshoot_q": {
                "question": "During cargo load testing, a prototype boat capsizes when additional weights are introduced. Which engineering modification resolves this transverse instability?",
                "options": [
                    "Lower the center of gravity (CG) of the cargo towards the keel and widen the hull beam",
                    "Stack cargo higher on deck to create a vertical stabilizing tower",
                    "Narrow the hull bottom into a sharp knife-edge cross-section",
                    "Reduce wall thickness to minimize skin drag"
                ],
                "answer": "Lower the center of gravity (CG) of the cargo towards the keel and widen the hull beam",
                "explanation": "Positive transverse stability requires the Metacenter (M) to remain above the Center of Gravity (G), giving a positive Metacentric Height (GM > 0). Lowering cargo ballast lowers G, while widening the beam increases righting moment."
            },
            "materials_q": {
                "question": "What engineering characteristic is critical for marine hull sealants and hull coatings?",
                "options": [
                    "Hydrophobic water repellency, chemical corrosion resistance, and mechanical elasticity",
                    "High open-cell water absorption capacity",
                    "Rapid thermal conductivity to balance seafloor temperatures",
                    "Water-soluble organic decomposition"
                ],
                "answer": "Hydrophobic water repellency, chemical corrosion resistance, and mechanical elasticity",
                "explanation": "Marine applications require impervious barrier properties that withstand hydrostatic pressure cycles without degrading or leaking."
            },
            "data_q": {
                "question": "Empirical testing reveals that adding 100g, 200g, and 300g cargo produces draft depths of 1.2 cm, 2.4 cm, and 3.6 cm respectively. Which conclusion is scientifically correct?",
                "options": [
                    "Draft depth is directly and linearly proportional to added cargo mass",
                    "Draft depth increases exponentially as an inverse square function",
                    "Buoyant force decreases monotonically as cargo mass increases",
                    "Submergence depth is independent of total gravitational load"
                ],
                "answer": "Draft depth is directly and linearly proportional to added cargo mass",
                "explanation": "For a constant cross-sectional hull, displaced volume V = A · h. Equilibrium dictates m · g = ρ · A · h · g, confirming linear proportionality between draft h and payload mass m."
            }
        }
    },
    "circuit": {
        "vie": {
            "law": "Định luật Ohm & Công suất Tiêu thụ Điện",
            "formula": "U = I · R  và  P = U · I = I² · R",
            "formula_desc": "Hiệu điện thế bằng dòng điện nhân điện trở; công suất tiêu thụ tỉ lệ với bình phương cường độ dòng điện.",
            "mech": "Công tắc điều khiển & Cầu chì bảo vệ quá tải (Switch & Fuse Protection)",
            "metric": "Điện trở tương đương mắc song song R_p = (R1 · R2)/(R1 + R2)",
            "math_q": {
                "question": "Một mạch điện gồm hai điện trở R1 = 20 Ω và R2 = 30 Ω được mắc song song vào nguồn điện có hiệu điện thế U = 12 V. Tính cường độ dòng điện tổng I chạy qua mạch chính:",
                "options": ["1.00 A", "0.24 A", "2.50 A", "0.50 A"],
                "answer": "1.00 A",
                "explanation": "Điện trở tương đương của mạch song song: R_p = (R1 · R2) / (R1 + R2) = (20 × 30) / (20 + 30) = 600 / 50 = 12 Ω. Cường độ dòng điện mạch chính: I = U / R_p = 12 V / 12 Ω = 1.00 A."
            },
            "physics_q": {
                "question": "Trong hệ thống điện gia đình và phòng học, tại sao các bóng đèn chiếu sáng luôn được mắc song song thay vì mắc nối tiếp?",
                "options": [
                    "Để mỗi bóng đèn nhận đủ hiệu điện thế định mức và khi một bóng bị cháy thì các bóng khác vẫn sáng bình thường",
                    "Để giảm tổng dòng điện tiêu thụ xuống mức bằng 0",
                    "Để tiết kiệm dây dẫn điện tối đa",
                    "Vì mắc song song làm điện trở tương đương tăng lên gấp đôi"
                ],
                "answer": "Để mỗi bóng đèn nhận đủ hiệu điện thế định mức và khi một bóng bị cháy thì các bóng khác vẫn sáng bình thường",
                "explanation": "Trong mạch song song: U_mạch = U1 = U2... nên các thiết bị đều hoạt động đúng công suất thiết kế. Hơn nữa, mỗi nhánh hoạt động độc lập, ngắt một nhánh không làm hở mạch của các nhánh còn lại."
            },
            "troubleshoot_q": {
                "question": "Khi bật công tắc, đèn LED trong mô hình không phát sáng dù pin còn mới 100%. Bước kiểm tra kỹ thuật đầu tiên nào cần thực hiện?",
                "options": [
                    "Kiểm tra chiều phân cực của đèn LED (chân dài cực dương Anode, chân ngắn cực âm Cathode)",
                    "Thay ngay toàn bộ dây dẫn điện bằng dây có đường kính lớn hơn",
                    "Tăng gấp ba lần số lượng pin trong mạch",
                    "Dùng kìm bóp vỡ vỏ nhựa của đèn LED"
                ],
                "answer": "Kiểm tra chiều phân cực của đèn LED (chân dài cực dương Anode, chân ngắn cực âm Cathode)",
                "explanation": "Đèn LED là linh kiện bán dẫn chỉ cho dòng điện đi qua theo một chiều duy nhất (từ Anode sang Cathode). Nếu cắm ngược cực tính, diode bị phân cực ngược và chặn hoàn toàn dòng điện."
            },
            "materials_q": {
                "question": "Tại sao lõi dây dẫn điện thường làm bằng đồng (Cu) trong khi vỏ bọc làm bằng nhựa PVC?",
                "options": [
                    "Đồng có mật độ electron tự do cao (điện trở suất cực nhỏ), còn PVC là chất cách điện bảo vệ an toàn",
                    "Đồng có giá thành rẻ nhất trong tất cả các kim loại",
                    "PVC có khả năng tự phát sinh dòng điện xoay chiều",
                    "Đồng nhẹ hơn nhôm và nhựa có khả năng tản nhiệt tức thời"
                ],
                "answer": "Đồng có mật độ electron tự do cao (điện trở suất cực nhỏ), còn PVC là chất cách điện bảo vệ an toàn",
                "explanation": "Đồng là kim loại có điện trở suất rất thấp (ρ ≈ 1.68 × 10⁻⁸ Ω·m) giúp truyền dẫn điện với hao phí nhiệt Joules tối thiểu. Nhựa PVC có liên kết ion/cộng hóa trị bền vững, không có hạt mang điện tự do nên cách điện hoàn hảo."
            },
            "data_q": {
                "question": "Một cảm biến đo được điện áp U và dòng điện I qua một điện trở: Khi U = 3V thì I = 0.15A; khi U = 6V thì I = 0.30A; khi U = 9V thì I = 0.45A. Trị số điện trở R là bao nhiêu?",
                "options": ["20 Ω", "15 Ω", "30 Ω", "10 Ω"],
                "answer": "20 Ω",
                "explanation": "Theo định luật Ohm: R = U / I. Tại U = 3V: R = 3 / 0.15 = 20 Ω. Tại U = 6V: R = 6 / 0.30 = 20 Ω. Tại U = 9V: R = 9 / 0.45 = 20 Ω. Điện trở có giá trị không đổi là 20 Ω."
            }
        },
        "eng": {
            "law": "Ohm's Law & Electrical Power Dissipation",
            "formula": "V = I · R  and  P = V · I = I² · R",
            "formula_desc": "Voltage equals current multiplied by resistance; electrical power dissipated is proportional to current squared.",
            "mech": "Single-Pole Switch & Overcurrent Circuit Breaker",
            "metric": "Parallel Equivalent Resistance R_p = (R1 · R2)/(R1 + R2)",
            "math_q": {
                "question": "A circuit contains two resistors R1 = 20 Ω and R2 = 30 Ω connected in parallel across a 12 V power supply. Calculate the total main circuit current I:",
                "options": ["1.00 A", "0.24 A", "2.50 A", "0.50 A"],
                "answer": "1.00 A",
                "explanation": "Parallel equivalent resistance: R_p = (R1 · R2) / (R1 + R2) = (20 × 30) / (20 + 30) = 600 / 50 = 12 Ω. Total current: I = V / R_p = 12 V / 12 Ω = 1.00 A."
            },
            "physics_q": {
                "question": "Why are electrical fixtures in residential and educational buildings wired in parallel rather than in series?",
                "options": [
                    "So each device operates at full nominal voltage and one failure does not interrupt remaining branches",
                    "To reduce total household power consumption to zero",
                    "To minimize the physical copper wire length required",
                    "Because parallel wiring automatically doubles total circuit resistance"
                ],
                "answer": "So each device operates at full nominal voltage and one failure does not interrupt remaining branches",
                "explanation": "In parallel circuits, every branch experiences identical potential difference (V_total = V1 = V2). Branches operate independently without disrupting parallel circuits if one opens."
            },
            "troubleshoot_q": {
                "question": "When closing the switch, an LED indicator fails to illuminate despite full battery charge. What initial diagnostic check should be performed?",
                "options": [
                    "Verify LED semiconductor polarity (longer lead is positive Anode, shorter lead is negative Cathode)",
                    "Replace all connecting wires with larger diameter cables immediately",
                    "Triple the battery supply voltage",
                    "Crush the epoxy lens with pliers"
                ],
                "answer": "Verify LED semiconductor polarity (longer lead is positive Anode, shorter lead is negative Cathode)",
                "explanation": "Light Emitting Diodes are polarized semiconductors that conduct current only in forward bias (Anode to Cathode). Reverse connection blocks current completely."
            },
            "materials_q": {
                "question": "Why is copper (Cu) standard for conductive cores while PVC polymer forms the exterior insulation?",
                "options": [
                    "Copper possesses high free-electron mobility (low resistivity), whereas PVC has tightly bound valence electrons",
                    "Copper is the least expensive element on Earth",
                    "PVC autonomously generates alternating current",
                    "Copper is lighter than aluminum and PVC cools instantly"
                ],
                "answer": "Copper possesses high free-electron mobility (low resistivity), whereas PVC has tightly bound valence electrons",
                "explanation": "Copper offers low electrical resistivity (ρ ≈ 1.68 × 10⁻⁸ Ω·m), minimizing Joule resistive losses. PVC lacks free charge carriers, serving as an outstanding dielectric insulator."
            },
            "data_q": {
                "question": "Sensor readings for voltage V and current I across an ohmic resistor show: at 3V, I = 0.15A; at 6V, I = 0.30A; at 9V, I = 0.45A. What is the resistance R?",
                "options": ["20 Ω", "15 Ω", "30 Ω", "10 Ω"],
                "answer": "20 Ω",
                "explanation": "By Ohm's Law: R = V / I. At 3V: 3 / 0.15 = 20 Ω. At 6V: 6 / 0.30 = 20 Ω. At 9V: 9 / 0.45 = 20 Ω. The resistance is constant at 20 Ω."
            }
        }
    }
}

print("Specs drafted.")
