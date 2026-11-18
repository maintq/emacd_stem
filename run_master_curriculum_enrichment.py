#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Full Master STEM Curriculum Generator with complete 12-domain specs.
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

# Load domain templates from generator
from full_master_stem_enrichment import DOMAINS

# Add computing, filtration, robotics, materials_science, biology to DOMAINS
DOMAINS["filtration"] = {
    "vie": {
        "law_name": "Định luật Thấm Darcy & Động học Dòng chảy",
        "formula": "Q = V / t  và  η = [(NTU_vào - NTU_ra) / NTU_vào] · 100%",
        "formula_unit": "L/phút, NTU (Độ đục)",
        "mech": "Cột lọc phân tầng (Sỏi, Cát thô, Cát mịn, Than hoạt tính)",
        "metric": "Hiệu suất khử độ đục η ≥ 85.0%",
        "matching": [
            {"term": "Q = V / t", "definition": "Lưu lượng dòng chảy chất lỏng qua màng lọc trên một đơn vị thời gian"},
            {"term": "Than hoạt tính", "definition": "Vật liệu xốp có diện tích bề mặt lớn hấp phụ các chất hữu cơ và độc tố"},
            {"term": "Đơn vị NTU", "definition": "Đơn vị đo độ đục của nước dựa trên hiện tượng tán xạ ánh sáng của hạt cặn"},
            {"term": "Định luật Darcy", "definition": "Tốc độ dòng chảy qua môi trường xốp tỉ lệ với độ chênh lệch áp suất"}
        ],
        "cloze": [
            {"text": "Trong cột lọc nước phân tầng, các lớp vật liệu được bố trí từ cỡ hạt [lớn đến nhỏ] theo chiều dòng nước chảy.", "answer": "lớn đến nhỏ", "options": ["lớn đến nhỏ", "nhỏ đến lớn", "ngẫu nhiên", "đồng nhất"]},
            {"text": "Than hoạt tính loại bỏ mùi và chất độc hại trong nước chủ yếu nhờ cơ chế [hấp phụ] bề mặt.", "answer": "hấp phụ", "options": ["hấp phụ", "hòa tan", "bay hơi", "kết tinh"]},
            {"text": "Hiệu suất lọc nước tỉ lệ nghịch với [vận tốc] dòng chảy; nếu nước chảy quá nhanh thì cặn bẩn sẽ bị cuốn trôi qua màng lọc.", "answer": "vận tốc", "options": ["vận tốc", "nhiệt độ", "thời gian", "áp suất"]},
            {"text": "Chỉ số [NTU] là thước đo độ trong suốt và mật độ hạt cặn lơ lửng trong mẫu nước lọc.", "answer": "NTU", "options": ["NTU", "Ohm", "Watt", "Newton"]}
        ],
        "q_physics": {
            "badge": "⚛️ Vật lý & Nguyên lý Cơ chế",
            "question": "Cơ chế vật lý nào giải thích tại sao nước đục khi chảy qua cột lọc gồm cát mịn và than hoạt tính lại trở nên trong suốt?",
            "options": [
                "Cát mịn giữ lại các hạt cặn cơ học nhờ khe rỗng vi mô, còn than hoạt tính hấp phụ các phân tử hữu cơ vào bề mặt xốp",
                "Cát mịn có khả năng tự tiêu diệt nguyên tử cặn bẩn",
                "Nước bị đun sôi tức thời khi tiếp xúc với than",
                "Lực từ trường của cát biến đổi chất bẩn thành oxy"
            ],
            "answer": "Cát mịn giữ lại các hạt cặn cơ học nhờ khe rỗng vi mô, còn than hoạt tính hấp phụ các phân tử hữu cơ vào bề mặt xốp",
            "explanation": "Lọc nước kết hợp 2 cơ chế: Lọc giữ cơ học (Mechanical filtration) giữ hạt lơ lửng theo kích thước lỗ rỗng và Hấp phụ bề mặt (Adsorption) qua mạng lưới vi xốp khổng lồ của than hoạt tính."
        },
        "q_math": {
            "badge": "📐 Toán học Ứng dụng & Tính toán",
            "question": "Nước thô đầu vào có độ đục 120 NTU. Sau khi đi qua mô hình cột lọc, nước thu được có độ đục 18 NTU. Hiệu suất lọc khử độ đục η của hệ thống là bao nhiêu?",
            "options": ["85.0%", "82.5%", "90.0%", "75.0%"],
            "answer": "85.0%",
            "explanation": "Hiệu suất lọc: η = [(NTU_vào - NTU_ra) / NTU_vào] × 100% = [(120 - 18) / 120] × 100% = (102 / 120) × 100% = 85.0%."
        },
        "q_troubleshoot": {
            "badge": "🔧 Xử lý Sự cố Kỹ thuật",
            "question": "Sau 15 phút vận hành, tốc độ nước chảy nhỏ giọt và gần như tắc nghẽn hoàn toàn. Nguyên nhân kỹ thuật nào sau đây là chuẩn xác nhất?",
            "options": [
                "Hiện tượng bít tắc lớp mặt (Surface clogging) do cặn bùn kích thước lớn phủ kín các lỗ rỗng của lớp cát trên cùng",
                "Do lực hút Trái Đất bị giảm sút",
                "Nước bị chuyển hóa thành chất khí",
                "Cát mịn tự nở ra gấp 10 lần kích thước ban đầu"
            ],
            "answer": "Hiện tượng bít tắc lớp mặt (Surface clogging) do cặn bùn kích thước lớn phủ kín các lỗ rỗng của lớp cát trên cùng",
            "explanation": "Khi không có lớp sỏi thô chặn trước, các mảng cặn kích thước lớn sẽ bịt kín bề mặt lớp cát mịn, làm giảm hệ số thấm thủy lực và gây tắc dòng chảy (cần rửa ngược - backwash)."
        },
        "q_materials": {
            "badge": "🔬 Khoa học Vật liệu & Kết cấu",
            "question": "Than hoạt tính (Activated Carbon) có đặc tính cấu trúc vật liệu nào vượt trội giúp hấp phụ độc tố trong nước?",
            "options": [
                "Diện tích bề mặt riêng cực lớn (từ 500 đến 1500 m²/gram) nhờ hệ thống lỗ rỗng vi mô chằng chịt",
                "Tính cứng giòn như kim cương",
                "Khả năng dẫn điện một chiều cao",
                "Độ trơn nhẵn bóng không ma sát"
            ],
            "answer": "Diện tích bề mặt riêng cực lớn (từ 500 đến 1500 m²/gram) nhờ hệ thống lỗ rỗng vi mô chằng chịt",
            "explanation": "Quá trình hoạt hóa nhiệt tạo ra mạng lưới lỗ xốp cực kỳ dày đặc. Chỉ 1 gram than hoạt tính có diện tích bề mặt tiếp xúc tương đương cả một sân bóng đá, bẫy giữ độc tố hiệu quả."
        },
        "q_data": {
            "badge": "📊 Phân tích Dữ liệu Thực nghiệm",
            "question": "Thử nghiệm đo thời gian lọc 500ml nước qua các cỡ hạt: Sỏi thô (t = 20s, nước còn đục); Cát hạt vừa (t = 120s, nước khá trong); Cát siêu mịn (t = 600s, nước rất trong). Kết luận tối ưu kỹ thuật là gì?",
            "options": [
                "Cần xếp nhiều tầng hạt từ thô đến mịn để kết hợp lưu lượng nước nhanh và độ trong suốt cao",
                "Chỉ dùng duy nhất lớp sỏi thô để lấy nước nhanh nhất",
                "Chỉ dùng duy nhất lớp cát siêu mịn bất chấp tốc độ lọc",
                "Cỡ hạt lọc không có ảnh hưởng gì tới chất lượng nước"
            ],
            "answer": "Cần xếp nhiều tầng hạt từ thô đến mịn để kết hợp lưu lượng nước nhanh và độ trong suốt cao",
            "explanation": "Phân tầng đa lớp (Multi-media stratification) phân phối tải lượng cặn đều khắp chiều cao cột lọc, tránh tắc bề mặt và cân bằng giữa lưu lượng dòng chảy và độ tinh khiết."
        }
    },
    "eng": {
        "law_name": "Darcy's Permeability Law & Fluid Filtration",
        "formula": "Q = V / t  and  η = [(NTU_in - NTU_out) / NTU_in] · 100%",
        "formula_unit": "L/min, NTU (Turbidity)",
        "mech": "Stratified Multi-Media Column (Gravel, Coarse Sand, Activated Carbon)",
        "metric": "Turbidity Removal Efficiency η ≥ 85.0%",
        "matching": [
            {"term": "Q = V / t", "definition": "Volumetric fluid flow rate passing through filter media per unit time"},
            {"term": "Activated Carbon", "definition": "High surface area porous carbon that adsorbs organic toxins and odor compounds"},
            {"term": "NTU Unit", "definition": "Standard turbidity unit quantifying light scattering by suspended colloids"},
            {"term": "Darcy's Law", "definition": "Fluid flow rate through porous media is proportional to hydraulic pressure gradient"}
        ],
        "cloze": [
            {"text": "In a stratified filtration column, granular layers are arranged from [coarse to fine] along the flow direction.", "answer": "coarse to fine", "options": ["coarse to fine", "fine to coarse", "randomly", "homogeneously"]},
            {"text": "Activated carbon removes volatile chemicals primarily through surface [adsorption].", "answer": "adsorption", "options": ["adsorption", "dissolution", "evaporation", "crystallization"]},
            {"text": "Filtration quality degrades when interstitial flow [velocity] is excessively high, scouring trapped particles.", "answer": "velocity", "options": ["velocity", "temperature", "mass", "volume"]},
            {"text": "The [NTU] metric measures optical cloudiness and suspended particulate concentration in filtered effluent.", "answer": "NTU", "options": ["NTU", "Ohm", "Watt", "Newton"]}
        ],
        "q_physics": {
            "badge": "⚛️ Physics Principles & Mechanisms",
            "question": "What physical mechanism explains why turbid wastewater clarifies when permeating through sand and activated carbon beds?",
            "options": [
                "Fine sand traps particulates mechanically within interstitial pores, while activated carbon adsorbs dissolved contaminants onto porous walls",
                "Sand particles destroy particulate atoms chemically",
                "Water instantaneously boils upon contacting carbon",
                "Magnetic fields in silica convert dirt into oxygen"
            ],
            "answer": "Fine sand traps particulates mechanically within interstitial pores, while activated carbon adsorbs dissolved contaminants onto porous walls",
            "explanation": "Filtration operates via mechanical sieving within pore throats and molecular surface adsorption governed by van der Waals forces within carbon micropores."
        },
        "q_math": {
            "badge": "📐 Applied Math & Calculation",
            "question": "Influent wastewater has turbidity 120 NTU. After single-pass column filtration, effluent measures 18 NTU. What is the turbidity removal efficiency η?",
            "options": ["85.0%", "82.5%", "90.0%", "75.0%"],
            "answer": "85.0%",
            "explanation": "Efficiency: η = [(120 - 18) / 120] × 100% = (102 / 120) × 100% = 85.0%."
        },
        "q_troubleshoot": {
            "badge": "🔧 Engineering Troubleshooting",
            "question": "After 15 minutes of continuous operation, filtrate flow drops to zero. What is the primary diagnosis?",
            "options": [
                "Surface cake clogging caused by macroscopic silt blinding the top sand pore throats",
                "Earth gravitational pull decayed locally",
                "Water transformed into gaseous vapor",
                "Sand grains expanded tenfold in volume"
            ],
            "answer": "Surface cake clogging caused by macroscopic silt blinding the top sand pore throats",
            "explanation": "Without upstream gravel pre-filtration, large colloids form an impermeable surface cake layer, collapsing hydraulic conductivity (requiring backwashing)."
        },
        "q_materials": {
            "badge": "🔬 Materials & Structural Mechanics",
            "question": "Which material characteristic grants activated carbon its exceptional adsorption capacity?",
            "options": [
                "Immense specific surface area (500 to 1500 m²/gram) within an intricate internal micro-pore network",
                "Diamond-like hardness and tensile modulus",
                "High direct-current electrical conductivity",
                "Mirror-smooth frictionless exterior"
            ],
            "answer": "Immense specific surface area (500 to 1500 m²/gram) within an intricate internal micro-pore network",
            "explanation": "Thermal activation creates microscopic fissures. A single gram provides up to 1500 m² of surface area to capture contaminants."
        },
        "q_data": {
            "badge": "📊 Empirical Data Analysis",
            "question": "Data for 500mL filtration times: Coarse gravel (20s, high turbidity); Medium sand (120s, clear); Fine sand (600s, pristine). What is the optimal engineering conclusion?",
            "options": [
                "A stratified multi-media column maximizes throughput velocity while maintaining high filtrate purity",
                "Deploy exclusively coarse gravel to maximize flow speed",
                "Use solely fine sand regardless of flow rate",
                "Grain sizing has zero impact on filtration quality"
            ],
            "answer": "A stratified multi-media column maximizes throughput velocity while maintaining high filtrate purity",
            "explanation": "Graded stratification distributes particulate load throughout the entire bed depth, preventing premature surface blinding while delivering low NTU effluent."
        }
    }
}

DOMAINS["robotics"] = {
    "vie": {
        "law_name": "Tĩnh học Khớp quay & Khí nén Tự động hóa",
        "formula": "τ = F · d · sin(θ)  và  F_kẹp = p · A",
        "formula_unit": "N·m (Mô-men xoắn), N (Lực kẹp)",
        "mech": "Đầu gắp khí nén & Động cơ Servo khớp quay (Gripper & Servo Actuator)",
        "metric": "Độ lặp lại vị trí (Repeatability) ≤ ±1.0 mm",
        "matching": [
            {"term": "τ = F · d", "definition": "Mô-men xoắn bằng tích lực tác dụng và cánh tay đòn vuông góc từ tâm trục quay"},
            {"term": "F = p · A", "definition": "Lực đẩy của piston khí nén/thủy lực bằng áp suất nhân diện tích bề mặt piston"},
            {"term": "Bậc tự do (DoF)", "definition": "Số hướng chuyển động độc lập của các khớp trên cánh tay robot"},
            {"term": "Đơn vị N·m", "definition": "Đơn vị đo mô-men xoắn giữ và mô-men quay của động cơ servo trong hệ SI"}
        ],
        "cloze": [
            {"text": "Mô-men xoắn của động cơ khớp vai robot tỉ lệ thuận với khối lượng vật nâng và [khoảng cách] vươn ngang của cánh tay.", "answer": "khoảng cách", "options": ["khoảng cách", "vận tốc", "màu sắc", "nhiệt độ"]},
            {"text": "Lực kẹp của giác hút hoặc đầu gắp khí nén tỉ lệ thuận với [áp suất] khí nén cấp vào xi-lanh.", "answer": "áp suất", "options": ["áp suất", "thời gian", "chiều dài dây", "điện áp"]},
            {"text": "Một cánh tay robot có 3 khớp quay độc lập trên không gian 3 chiều có [ba] bậc tự do (Degrees of Freedom).", "answer": "ba", "options": ["ba", "sáu", "một", "mười hai"]},
            {"text": "Để tránh trượt rơi vật khi gắp, má kẹp robot cần được dán lớp đệm có hệ số ma sát [cao].", "answer": "cao", "options": ["cao", "thấp", "bằng không", "âm"]}
        ],
        "q_physics": {
            "badge": "⚛️ Vật lý & Nguyên lý Cơ chế",
            "question": "Tại sao khi cánh tay robot duỗi thẳng hết cỡ về phía trước, động cơ khớp vai phải chịu mô-men xoắn lớn hơn rất nhiều so with khi gập sát vào thân?",
            "options": [
                "Vì cánh tay đòn d từ trọng tâm vật tới trục quay vai đạt giá trị cực đại, làm mô-men uốn τ = F · d tăng vọt",
                "Vì vật thể bị nặng thêm khi đưa ra xa",
                "Vì không khí ở xa có lực hút mạnh hơn",
                "Do động cơ tự giảm dòng điện khi cánh tay duỗi dài"
            ],
            "answer": "Vì cánh tay đòn d từ trọng tâm vật tới trục quay vai đạt giá trị cực đại, làm mô-men uốn τ = F · d tăng vọt",
            "explanation": "Mô-men quay τ = F_trọng_lượng · d. Khi duỗi thẳng, khoảng cách vuông góc d lớn nhất, đòi hỏi mô-men xoắn đối kháng của servo vai phải lớn nhất để giữ cân bằng tĩnh."
        },
        "q_math": {
            "badge": "📐 Toán học Ứng dụng & Tính toán",
            "question": "Một cánh tay robot giữ một vật nặng m = 0.4 kg ở khoảng cách vươn ngang d = 0.35 m từ trục khớp vai (g = 9.8 m/s²). Mô-men xoắn giữ τ mà động cơ servo khớp vai phải sinh ra là bao nhiêu?",
            "options": ["1.372 N·m", "2.744 N·m", "0.686 N·m", "1.400 N·m"],
            "answer": "1.372 N·m",
            "explanation": "Trọng lượng vật: F = m · g = 0.4 kg × 9.8 m/s² = 3.92 N. Mô-men xoắn giữ: τ = F · d = 3.92 N × 0.35 m = 1.372 N·m."
        },
        "q_troubleshoot": {
            "badge": "🔧 Xử lý Sự cố Kỹ thuật",
            "question": "Đầu gắp robot kẹp vật thể nhưng khi nâng lên vật liên tục bị trượt rơi ra khỏi má kẹp. Giải pháp kỹ thuật nào tối ưu nhất?",
            "options": [
                "Tăng áp suất kẹp p hoặc bọc thêm lớp cao su đàn hồi có hệ số ma sát bám cao lên má kẹp",
                "Quấn thêm giấy bóng kính trơn nhẵn lên vật thể",
                "Cho cánh tay di chuyển giật cục thật nhanh",
                "Tắt nguồn điện của robot"
            ],
            "answer": "Tăng áp suất kẹp p hoặc bọc thêm lớp cao su đàn hồi có hệ số ma sát bám cao lên má kẹp",
            "explanation": "Điều kiện chống trượt: Lực ma sát nghỉ F_ms = μ · F_kẹp ≥ Trọng lượng vật P. Tăng hệ số ma sát μ và tăng lực kẹp F_kẹp sẽ ngăn hiện tượng trượt rơi."
        },
        "q_materials": {
            "badge": "🔬 Khoa học Vật liệu & Kết cấu",
            "question": "Các thanh liên kết (links) của cánh tay robot công nghiệp thường được đúc bằng hợp kim nhôm (Duralumin) hoặc sợi carbon vì lý do gì?",
            "options": [
                "Giảm tối đa mô-men quán tính quay (Rotational inertia) của cánh tay, giúp robot tăng tốc nhanh và giảm tải cho động cơ",
                "Vì nhôm có khả năng tự sản sinh từ trường",
                "Để cánh tay robot dễ bị uốn cong khi gặp va chạm",
                "Vì sợi carbon rẻ tiền hơn sắt vụn"
            ],
            "answer": "Giảm tối đa mô-men quán tính quay (Rotational inertia) của cánh tay, giúp robot tăng tốc nhanh và giảm tải cho động cơ",
                "explanation": "Mô-men quán tính I = Σm·r² cản trở gia tốc góc. Giảm khối lượng phân bố ở đầu cánh tay giúp robot chuyển động linh hoạt với sai số động học thấp."
        },
        "q_data": {
            "badge": "📊 Phân tích Dữ liệu Thực nghiệm",
            "question": "Đo độ chính xác vị trí của cánh tay robot sau 50 chu kỳ gắp đặt: Sai số trung bình là ±0.6 mm, nhưng khi tăng tải trọng từ 0.2kg lên 1.0kg, sai số tăng lên ±3.5 mm. Hiện tượng này là do đâu?",
            "options": [
                "Biến dạng uốn đàn hồi của kết cấu cơ khí và khe hở bánh răng (Backlash) dưới tác dụng của tải trọng lớn",
                "Tín hiệu lập trình bị mờ đi khi mang vật nặng",
                "Đồng hồ đo điện tử tự động chạy sai",
                "Trọng lực Trái Đất tăng lên ở vật nặng"
            ],
            "answer": "Biến dạng uốn đàn hồi của kết cấu cơ khí và khe hở bánh răng (Backlash) dưới tác dụng của tải trọng lớn",
            "explanation": "Dưới tải trọng nặng, các thanh dầm bị uốn võng cơ học và phản lực làm bộc lộ khe hở ăn khớp của các hộp giảm tốc, dẫn đến độ võng và sai lệch tọa độ điểm cuối."
        }
    },
    "eng": {
        "law_name": "Joint Statics & Pneumatic Automation",
        "formula": "τ = F · d · sin(θ)  and  F_grip = p · A",
        "formula_unit": "N·m (Torque), N (Gripping Force)",
        "mech": "Pneumatic Gripper & Closed-Loop Servo Actuator",
        "metric": "End-Effector Repeatability ≤ ±1.0 mm",
        "matching": [
            {"term": "τ = F · d", "definition": "Holding torque equals gravitational payload weight multiplied by moment arm distance"},
            {"term": "F = p · A", "definition": "Piston force equals pneumatic air pressure multiplied by active piston face area"},
            {"term": "Degrees of Freedom (DoF)", "definition": "Number of independent joint axis variables defining spatial manipulator posture"},
            {"term": "N·m (Newton-meter)", "definition": "Standard SI unit measuring actuator holding torque and rotational dynamic work"}
        ],
        "cloze": [
            {"text": "Shoulder joint actuator holding torque is directly proportional to payload mass and horizontal reach [distance].", "answer": "distance", "options": ["distance", "velocity", "color", "temperature"]},
            {"text": "Gripping force delivered by a pneumatic actuator scales linearly with supply [pressure].", "answer": "pressure", "options": ["pressure", "voltage", "ambient temperature", "wire length"]},
            {"text": "A spatial serial robotic arm with three independent rotary revolute joints possesses [three] degrees of freedom.", "answer": "three", "options": ["three", "six", "one", "twelve"]},
            {"text": "To prevent object slippage during rapid manipulation, gripper fingers require high-friction [rubber] contact pads.", "answer": "rubber", "options": ["rubber", "glass", "ice", "polished steel"]}
        ],
        "q_physics": {
            "badge": "⚛️ Physics Principles & Mechanisms",
            "question": "Why does a robotic shoulder actuator experience vastly higher torque when the arm is fully extended horizontally versus retracted close to the base?",
            "options": [
                "The perpendicular moment arm d from payload gravity to the shoulder axis is maximized, causing torque τ = F · d to surge",
                "The physical mass of the object increases at distance",
                "Ambient air exerts higher gravitational attraction far away",
                "The motor automatically drops current when extended"
            ],
            "answer": "The perpendicular moment arm d from payload gravity to the shoulder axis is maximized, causing torque τ = F · d to surge",
            "explanation": "Static torque equals gravitational force multiplied by perpendicular lever arm length d. Full horizontal extension maximizes d, requiring peak opposing motor torque."
        },
        "q_math": {
            "badge": "📐 Applied Math & Calculation",
            "question": "A robotic arm holds a payload of mass m = 0.4 kg at a horizontal reach d = 0.35 m from the shoulder joint axis (g = 9.8 m/s²). Calculate the static holding torque τ required:",
            "options": ["1.372 N·m", "2.744 N·m", "0.686 N·m", "1.400 N·m"],
            "answer": "1.372 N·m",
            "explanation": "Weight: F = m · g = 0.4 kg × 9.8 m/s² = 3.92 N. Torque: τ = F · d = 3.92 N × 0.35 m = 1.372 N·m."
        },
        "q_troubleshoot": {
            "badge": "🔧 Engineering Troubleshooting",
            "question": "A gripper grasps a cylindrical payload, but the part slips out during upward acceleration. What engineering correction should be applied?",
            "options": [
                "Increase pneumatic clamp pressure or fit high-friction elastomer pads onto finger contact jaws",
                "Wrap smooth cellophane film around the payload surface",
                "Accelerate the robot arm violently in erratic motions",
                "Disconnect electrical control power"
            ],
            "answer": "Increase pneumatic clamp pressure or fit high-friction elastomer pads onto finger contact jaws",
            "explanation": "Slip resistance requires F_friction = μ · F_clamp ≥ m · (g + a). Boosting the friction coefficient μ and clamping force F_clamp prevents dynamic slippage."
        },
        "q_materials": {
            "badge": "🔬 Materials & Structural Mechanics",
            "question": "Why are manipulator links cast from aerospace duralumin alloys or carbon fiber tubes instead of solid structural steel?",
            "options": [
                "To minimize polar mass moment of inertia, reducing motor dynamic drive torque and settling vibrations",
                "Because aluminum generates autonomous magnetic fields",
                "To allow arm links to deform permanently on impact",
                "Because carbon fiber costs less than raw iron ore"
            ],
            "answer": "To minimize polar mass moment of inertia, reducing motor dynamic drive torque and settling vibrations",
            "explanation": "Mass moment of inertia I = Σm·r² opposes angular acceleration. Minimizing outboard link mass enables rapid trajectory tracking with minimal kinetic overshoot."
        },
        "q_data": {
            "badge": "📊 Empirical Data Analysis",
            "question": "Repeatability tests show ±0.6 mm position deviation under 0.2 kg payload, degrading to ±3.5 mm under 1.0 kg payload. What causes this positional error divergence?",
            "options": [
                "Elastic mechanical beam deflection and gearbox tooth backlash under heavy cantilevered loads",
                "Software code becoming corrupted under heavy weights",
                "Digital caliper sensors malfunctioning systematically",
                "Local gravity increasing for heavier objects"
            ],
            "answer": "Elastic mechanical beam deflection and gearbox tooth backlash under heavy cantilevered loads",
            "explanation": "Cantilever flexural deflection δ = F·L³/(3EI) and elastic strain on gear reducers amplify under higher payloads, causing measurable end-effector positional droop."
        }
    }
}

DOMAINS["materials_science"] = {
    "vie": {
        "law_name": "Định luật Hooke & Cơ học Vật liệu Biến dạng",
        "formula": "σ = E · ε  và  ε = ΔL / L0",
        "formula_unit": "MPa (Megapascal), GPa (Mô-đun Young)",
        "mech": "Cấu trúc liên kết đại phân tử polymer & Mạng tinh thể (Polymer Chain & Crystal Lattice)",
        "metric": "Độ bền kéo đứt (Tensile Yield Strength) σ_y ≥ 40 MPa",
        "matching": [
            {"term": "σ = E · ε", "definition": "Định luật Hooke: Ứng suất tỉ lệ thuận với biến dạng tương đối qua mô-đun đàn hồi Young"},
            {"term": "Biến dạng đàn hồi", "definition": "Vật liệu tự động phục hồi hoàn toàn hình dạng ban đầu sau khi loại bỏ ngoại lực"},
            {"term": "Biến dạng dẻo (Plastic)", "definition": "Biến dạng vĩnh viễn tồn tại mãi mãi sau khi vượt quá giới hạn chảy của vật liệu"},
            {"term": "Đơn vị Megapascal (MPa)", "definition": "Đơn vị đo ứng suất và độ bền vật liệu bằng 1.000.000 Pascal (N/m²)"}
        ],
        "cloze": [
            {"text": "Trong miền đàn hồi tuyến tính, ứng suất kéo tác dụng tỉ lệ thuận với [độ biến dạng] của vật liệu.", "answer": "độ biến dạng", "options": ["độ biến dạng", "nhiệt độ", "thời gian", "khối lượng"]},
            {"text": "Khi ngoại lực kéo vượt quá [giới hạn đàn hồi], vật liệu sẽ bị biến dạng dẻo vĩnh viễn và không thể tự co lại hình dạng cũ.", "answer": "giới hạn đàn hồi", "options": ["giới hạn đàn hồi", "nhiệt độ phòng", "vận tốc âm thanh", "trọng lượng"]},
            {"text": "Vật liệu composite kết hợp sợi gia cường và nhựa nền mang lại tỷ số độ bền trên [khối lượng riêng] vượt trội.", "answer": "khối lượng riêng", "options": ["khối lượng riêng", "thể tích", "chiều dài", "giá thành"]},
            {"text": "Hiện tượng mỏi vật liệu (Fatigue) xảy ra khi vật liệu bị phá hủy dưới tác dụng của tải trọng [lặp lại] chu kỳ nhiều lần.", "answer": "lặp lại", "options": ["lặp lại", "tĩnh", "không đổi", "bằng không"]}
        ],
        "q_physics": {
            "badge": "⚛️ Vật lý & Nguyên lý Cơ chế",
            "question": "Sự khác biệt bản chất giữa biến dạng đàn hồi (Elastic) và biến dạng dẻo (Plastic) của vật liệu dưới tác dụng của lực kéo là gì?",
            "options": [
                "Biến dạng đàn hồi kéo giãn khoảng cách liên kết nguyên tử tạm thời (tự hồi phục), còn biến dạng dẻo làm trượt các mặt phẳng tinh thể vĩnh viễn",
                "Biến dạng đàn hồi làm vật liệu nóng chảy thành chất lỏng",
                "Biến dạng dẻo chỉ xảy ra ở nhiệt độ không độ tuyệt đối",
                "Hai hiện tượng này hoàn toàn giống nhau không có sự khác biệt"
            ],
            "answer": "Biến dạng đàn hồi kéo giãn khoảng cách liên kết nguyên tử tạm thời (tự hồi phục), còn biến dạng dẻo làm trượt các mặt phẳng tinh thể vĩnh viễn",
            "explanation": "Trong giới hạn đàn hồi, lực kéo chỉ kéo giãn lò xo liên kết nguyên tử. Khi vượt qua giới hạn chảy (Yield point), các mặt phẳng nguyên tử trượt dịch chuyển vĩnh viễn (dislocation slip)."
        },
        "q_math": {
            "badge": "📐 Toán học Ứng dụng & Tính toán",
            "question": "Một dải vật liệu mẫu có diện tích mặt cắt ngang A = 2.0 mm² = 2.0 × 10⁻⁶ m² chịu lực kéo dọc trục F = 80 N. Ứng suất kéo σ phát sinh trong vật liệu là bao nhiêu?",
            "options": ["40.0 MPa", "160.0 MPa", "20.0 MPa", "80.0 MPa"],
            "answer": "40.0 MPa",
            "explanation": "Ứng suất kéo: σ = F / A = 80 N / (2.0 × 10⁻⁶ m²) = 40 × 10⁶ Pa = 40.0 MPa."
        },
        "q_troubleshoot": {
            "badge": "🔧 Xử lý Sự cố Kỹ thuật",
            "question": "Một chi tiết nhựa sau khi chế tạo bị giòn gãy đột ngột khi chịu lực uốn nhẹ. Nguyên nhân khoa học vật liệu nào sau đây là phổ biến nhất?",
            "options": [
                "Tập trung ứng suất tại các góc nhọn bên trong thiết kế hoặc vật liệu bị thoái hóa chuỗi polymer do tia cực tím (UV)",
                "Do chi tiết nhựa quá nhẵn bóng",
                "Do nhựa hấp thụ quá nhiều sóng âm thanh",
                "Vì màu sắc của chi tiết nhựa quá sáng"
            ],
            "answer": "Tập trung ứng suất tại các góc nhọn bên trong thiết kế hoặc vật liệu bị thoái hóa chuỗi polymer do tia cực tím (UV)",
            "explanation": "Góc nhọn bên trong (Sharp re-entrant corners) làm tăng cục bộ ứng suất gấp 3-5 lần (Stress Concentration). Kỹ sư cần bo tròn góc (fillet radius) để phân tán ứng suất."
        },
        "q_materials": {
            "badge": "🔬 Khoa học Vật liệu & Kết cấu",
            "question": "Hiện tượng một vật liệu kim loại hoặc polymer bị phá hủy gãy nứt ở mức ứng suất thấp hơn nhiều so với giới hạn bền kéo sau hàng triệu lần rung lắc chu kỳ gọi là gì?",
            "options": [
                "Hiện tượng mỏi cơ học (Fatigue failure)",
                "Hiện tượng siêu dẫn nhiệt",
                "Hiện tượng quang điện trong",
                "Hiện tượng khúc xạ ánh sáng"
            ],
            "answer": "Hiện tượng mỏi cơ học (Fatigue failure)",
            "explanation": "Tải trọng chu kỳ lặp đi lặp lại sinh ra và phát triển các vết nứt vi mô (microcracks) lan truyền dần cho đến khi mặt cắt còn lại không chịu nổi tải trọng và đứt gãy đột ngột (Fatigue)."
        },
        "q_data": {
            "badge": "📊 Phân tích Dữ liệu Thực nghiệm",
            "question": "Một mẫu thanh vật liệu dài L0 = 200 mm bị kéo dãn dài thêm ΔL = 0.8 mm dưới lực kéo. Độ biến dạng tỉ đối (Strain ε) của mẫu là bao nhiêu?",
            "options": ["0.004 (0.4%)", "0.008 (0.8%)", "0.040 (4.0%)", "0.002 (0.2%)"],
            "answer": "0.004 (0.4%)",
            "explanation": "Độ biến dạng tỉ đối: ε = ΔL / L0 = 0.8 mm / 200 mm = 0.004 (tương đương 0.4%)."
        }
    },
    "eng": {
        "law_name": "Hooke's Law & Mechanics of Materials",
        "formula": "σ = E · ε  and  ε = ΔL / L0",
        "formula_unit": "MPa (Megapascal), GPa (Young's Modulus)",
        "mech": "Macromolecular Polymer Chains & Crystal Lattice",
        "metric": "Tensile Yield Strength σ_y ≥ 40 MPa",
        "matching": [
            {"term": "σ = E · ε", "definition": "Hooke's Law: Stress is proportional to elastic strain via Young's modulus E"},
            {"term": "Elastic Deformation", "definition": "Reversible mechanical strain that recovers completely upon load removal"},
            {"term": "Plastic Deformation", "definition": "Permanent unrecoverable structural strain exceeding material yield strength"},
            {"term": "Megapascal (MPa)", "definition": "Standard SI unit of stress and tensile strength equivalent to 1,000,000 N/m²"}
        ],
        "cloze": [
            {"text": "Within the linear elastic regime, axial tensile stress is directly proportional to relative [strain].", "answer": "strain", "options": ["strain", "temperature", "time", "density"]},
            {"text": "Exceeding the material's [yield limit] induces permanent plastic deformation from which it cannot recover.", "answer": "yield limit", "options": ["yield limit", "room temperature", "speed of sound", "gravitational mass"]},
            {"text": "Fiber-reinforced composite laminates offer an exceptional strength-to-[density] ratio.", "answer": "density", "options": ["density", "volume", "length", "cost"]},
            {"text": "Structural fatigue failure propagates under sustained [cyclic] alternating stress amplitudes.", "answer": "cyclic", "options": ["cyclic", "static", "zero", "constant"]}
        ],
        "q_physics": {
            "badge": "⚛️ Physics Principles & Mechanisms",
            "question": "What fundamental physical distinction differentiates elastic deformation from plastic deformation under tension?",
            "options": [
                "Elastic strain stretches atomic bond spacing reversibly, whereas plastic strain causes irreversible crystalline dislocation glide",
                "Elastic strain liquefies the material instantaneously",
                "Plastic strain occurs only at absolute zero temperature",
                "The two deformation modes are physically identical"
            ],
            "answer": "Elastic strain stretches atomic bond spacing reversibly, whereas plastic strain causes irreversible crystalline dislocation glide",
            "explanation": "In elasticity, atomic lattice springs stretch and spring back. Plastic deformation permanently shifts atomic planes via dislocation slip."
        },
        "q_math": {
            "badge": "📐 Applied Math & Calculation",
            "question": "A test coupon with cross-sectional area A = 2.0 mm² = 2.0 × 10⁻⁶ m² sustains an axial tensile load F = 80 N. Calculate internal tensile stress σ:",
            "options": ["40.0 MPa", "160.0 MPa", "20.0 MPa", "80.0 MPa"],
            "answer": "40.0 MPa",
            "explanation": "Tensile stress: σ = F / A = 80 N / (2.0 × 10⁻⁶ m²) = 40 × 10⁶ Pa = 40.0 MPa."
        },
        "q_troubleshoot": {
            "badge": "🔧 Engineering Troubleshooting",
            "question": "A molded polymer component snaps suddenly under minor flexure. What materials science factor is the most common cause?",
            "options": [
                "Severe stress concentration at sharp internal corners or UV photodegradation of polymer molecular chains",
                "Excessive surface smoothness",
                "Acoustic audio wave absorption",
                "Overly vibrant pigment coloration"
            ],
            "answer": "Severe stress concentration at sharp internal corners or UV photodegradation of polymer molecular chains",
            "explanation": "Sharp re-entrant corners act as notch stress concentrators, multiplying local stress by factors of 3 to 5. Radiusing corners (fillets) distributes loads safely."
        },
        "q_materials": {
            "badge": "🔬 Materials & Structural Mechanics",
            "question": "What phenomenon causes structural components to crack and fail at stress levels far below ultimate yield strength after millions of vibration cycles?",
            "options": [
                "Mechanical Fatigue failure",
                "Superconducting thermal flux",
                "Internal photoelectric effect",
                "Optical refraction breakdown"
            ],
            "answer": "Mechanical Fatigue failure",
            "explanation": "Cyclic alternating loads nucleate microcracks that incrementally propagate until the residual cross-section fractures catastrophically (Fatigue)."
        },
        "q_data": {
            "badge": "📊 Empirical Data Analysis",
            "question": "A test specimen of gauge length L0 = 200 mm elongates by ΔL = 0.8 mm under tension. What is the engineering strain ε?",
            "options": ["0.004 (0.4%)", "0.008 (0.8%)", "0.040 (4.0%)", "0.002 (0.2%)"],
            "answer": "0.004 (0.4%)",
            "explanation": "Engineering strain: ε = ΔL / L0 = 0.8 mm / 200 mm = 0.004 (0.4%)."
        }
    }
}

DOMAINS["computing"] = {
    "vie": {
        "law_name": "Toán học Nhị phân & Độ phức tạp Thuật toán",
        "formula": "N_trạng thái = 2^b  và  Độ phức tạp O(log n), O(n), O(n²)",
        "formula_unit": "Bit, Byte, Checksum Modulo 10",
        "mech": "Mã vạch quang học UPC & Cấu trúc Dữ liệu Cây nhị phân",
        "metric": "Độ chính xác thuật toán kiểm tra lỗi Checksum = 100%",
        "matching": [
            {"term": "Hệ nhị phân (Binary)", "definition": "Hệ đếm cơ số 2 chỉ gồm các chữ số 0 và 1 tương ứng với trạng thái tắt/bật của bóng bán dẫn"},
            {"term": "Độ phức tạp O(log n)", "definition": "Tốc độ tìm kiếm nhị phân chia đôi dữ liệu sau mỗi bước, cực kỳ tối ưu cho tập dữ liệu lớn"},
            {"term": "Chữ số kiểm tra (Check digit)", "definition": "Chữ số cuối cùng trong mã vạch UPC tính theo modulo 10 để phát hiện sai sót khi quét"},
            {"term": "Byte (8 bit)", "definition": "Đơn vị đo dung lượng thông tin cơ bản biểu diễn được 256 trạng thái ký tự khác nhau"}
        ],
        "cloze": [
            {"text": "Trong máy tính kỹ thuật số, dữ liệu được biểu diễn dưới dạng các bit nhị phân gồm hai chữ số [0 và 1].", "answer": "0 và 1", "options": ["0 và 1", "1 và 2", "0 đến 9", "A và B"]},
            {"text": "Thuật toán tìm kiếm nhị phân có độ phức tạp thời gian là [O(log n)], nhanh hơn rất nhiều so với tìm kiếm tuyến tính O(n).", "answer": "O(log n)", "options": ["O(log n)", "O(n²)", "O(2^n)", "O(1)"]},
            {"text": "Mã vạch UPC sử dụng phép chia lấy dư [modulo 10] để tính chữ số kiểm tra lỗi quét quang học.", "answer": "modulo 10", "options": ["modulo 10", "modulo 2", "căn bậc hai", "tích phân"]},
            {"text": "Với một chuỗi n bit nhị phân, số lượng trạng thái phân biệt có thể mã hóa được bằng [2^n].", "answer": "2^n", "options": ["2^n", "n²", "2·n", "n!"]}
        ],
        "q_physics": {
            "badge": "⚛️ Vật lý & Nguyên lý Cơ chế",
            "question": "Về mặt vật lý bán dẫn, tại sao máy tính hiện đại lại sử dụng hệ đếm nhị phân (0 và 1) thay vì hệ thập phân (0 đến 9)?",
            "options": [
                "Bóng bán dẫn transistor hoạt động ổn định nhất ở 2 trạng thái vật lý rõ ràng: Bão hòa dẫn điện (Bật - 1) và Ngắt dòng điện (Tắt - 0)",
                "Vì hệ đếm nhị phân tiết kiệm giấy in hơn",
                "Vì điện áp trong tự nhiên chỉ có 2 mức",
                "Do định luật vạn vật hấp dẫn quy định"
            ],
            "answer": "Bóng bán dẫn transistor hoạt động ổn định nhất ở 2 trạng thái vật lý rõ ràng: Bão hòa dẫn điện (Bật - 1) và Ngắt dòng điện (Tắt - 0)",
            "explanation": "Hai mức điện áp (High/Low) cho biên độ chống nhiễu (noise margin) tối đa. Nếu chia thành 10 mức điện áp thập phân, sai số nhiễu nhiệt sẽ lập tức gây sai lệch dữ liệu."
        },
        "q_math": {
            "badge": "📐 Toán học Ứng dụng & Tính toán",
            "question": "Thực hiện tìm kiếm một phần tử trong danh sách đã sắp xếp gồm n = 1024 phần tử. Số bước so sánh tối đa trong trường hợp xấu nhất của thuật toán Tìm kiếm Nhị phân (Binary Search) là bao nhiêu?",
            "options": ["10 bước", "512 bước", "1024 bước", "100 bước"],
            "answer": "10 bước",
            "explanation": "Độ phức tạp tìm kiếm nhị phân là O(log₂ n). Với n = 1024: log₂(1024) = 10 bước (vì 2¹⁰ = 1024). Tìm kiếm tuyến tính sẽ mất tới 1024 bước."
        },
        "q_troubleshoot": {
            "badge": "🔧 Xử lý Sự cố Kỹ thuật",
            "question": "Máy quét laser mã vạch tại siêu thị phát tiếng bíp báo lỗi không đọc được mã sản phẩm. Nguyên nhân kỹ thuật nào sau đây là chuẩn xác nhất?",
            "options": [
                "Độ tương phản quang học giữa vạch đen và khoảng trắng không đủ lớn, hoặc tổng trọng số checksum không thỏa mãn điều kiện Modulo 10",
                "Do bóng đèn laze bị đổi màu theo cảm xúc",
                "Mã vạch bị hết pin bên trong",
                "Do máy tính đang bận suy nghĩ bài toán khác"
            ],
            "answer": "Độ tương phản quang học giữa vạch đen và khoảng trắng không đủ lớn, hoặc tổng trọng số checksum không thỏa mãn điều kiện Modulo 10",
            "explanation": "Máy quét quang học đo cường độ ánh sáng phản xạ để nhận diện vạch đen/trắng. Nếu in mờ, nhòe hoặc sai chữ số checksum, bộ giải mã firmware sẽ từ chối dữ liệu để tránh tính sai giá tiền."
        },
        "q_materials": {
            "badge": "🔬 Khoa học Vật liệu & Kết cấu",
            "question": "Tại sao các bộ vi xử lý (CPU) máy tính hiện đại lại được chế tạo trên các phiến tinh thể Silic siêu tinh khiết (Silicon Wafer)?",
            "options": [
                "Silic là chất bán dẫn có dải năng lượng vùng cấm (Bandgap ≈ 1.1 eV) lý tưởng và oxit Silic (SiO2) là chất cách điện hoàn hảo để khắc mạch nano",
                "Vì silic là kim loại dẫn điện nhanh nhất hành tinh",
                "Vì cát silic có thể tự do biến thành vàng khi có dòng điện",
                "Do silic hoàn toàn trong suốt với mắt người"
            ],
            "answer": "Silic là chất bán dẫn có dải năng lượng vùng cấm (Bandgap ≈ 1.1 eV) lý tưởng và oxit Silic (SiO2) là chất cách điện hoàn hảo để khắc mạch nano",
            "explanation": "Đặc tính bán dẫn cho phép pha tạp ion (doping) để tạo tiếp giáp P-N. Lớp SiO2 đóng vai trò màng cách điện cổng (gate dielectric) cực kỳ ổn định trong quy trình quang khắc nano."
        },
        "q_data": {
            "badge": "📊 Phân tích Dữ liệu Thực nghiệm",
            "question": "Một bài toán tăng trưởng dữ liệu: Ban đầu có 1 hoa súng, sau mỗi tuần số lượng tăng gấp đôi (hàm mũ 2^n). Nếu ở tuần thứ 9 ao phủ được một nửa (50%), thì đến tuần thứ mấy cả ao sẽ bị phủ kín 100%?",
            "options": ["Tuần thứ 10", "Tuần thứ 18", "Tuần thứ 14", "Tuần thứ 12"],
            "answer": "Tuần thứ 10",
            "explanation": "Đặc trưng bùng nổ của hàm mũ cơ số 2: N(t+1) = 2 · N(t). Nếu ở tuần 9 ao đã đầy 50%, thì sang tuần 10 số lượng tăng gấp đôi: 50% × 2 = 100% diện tích ao."
        }
    },
    "eng": {
        "law_name": "Binary Mathematics & Algorithmic Complexity",
        "formula": "N_states = 2^b  and  Time Complexity O(log n), O(n), O(n²)",
        "formula_unit": "Bit, Byte, Modulo 10 Checksum",
        "mech": "Optical Barcode Scanner & Binary Search Tree",
        "metric": "Error Detection Accuracy = 100% via Checksum",
        "matching": [
            {"term": "Binary System (Base-2)", "definition": "Positional numeral system using bits 0 and 1 representing transistor switching states"},
            {"term": "O(log n) Complexity", "definition": "Logarithmic search halving candidate space at each step, optimal for large datasets"},
            {"term": "Checksum Digit", "definition": "Final digit in optical codes computed via modulo 10 to detect data entry errors"},
            {"term": "Byte (8 bits)", "definition": "Fundamental unit of digital data representation encoding 256 unique characters"}
        ],
        "cloze": [
            {"text": "Digital computers represent discrete information as binary bits comprised solely of [0 and 1].", "answer": "0 and 1", "options": ["0 and 1", "1 and 2", "0 through 9", "A and B"]},
            {"text": "Binary search exhibits a time complexity of [O(log n)], outperforming linear O(n) scanning.", "answer": "O(log n)", "options": ["O(log n)", "O(n²)", "O(2^n)", "O(1)"]},
            {"text": "Standard UPC barcodes apply [modulo 10] arithmetic to verify checksum validity.", "answer": "modulo 10", "options": ["modulo 10", "modulo 2", "square root", "integral"]},
            {"text": "A string of n binary bits encodes exactly [2^n] distinct discrete information states.", "answer": "2^n", "options": ["2^n", "n²", "2·n", "n!"]}
        ],
        "q_physics": {
            "badge": "⚛️ Physics Principles & Mechanisms",
            "question": "In semiconductor physics, why do digital computers rely on binary logic (0 and 1) instead of decimal (0 to 9)?",
            "options": [
                "Transistors operate most robustly at two distinct physical states: fully saturated (ON - 1) and cutoff (OFF - 0)",
                "Binary saves printing paper",
                "Voltage in nature exists only in two levels",
                "Governed by Newton's law of gravitation"
            ],
            "answer": "Transistors operate most robustly at two distinct physical states: fully saturated (ON - 1) and cutoff (OFF - 0)",
            "explanation": "Bistable operation provides maximum noise immunity margins against thermal fluctuations and voltage ripple."
        },
        "q_math": {
            "badge": "📐 Applied Math & Calculation",
            "question": "Searching for an item within a sorted array of n = 1024 elements: What is the maximum number of comparisons in worst case using Binary Search?",
            "options": ["10 steps", "512 steps", "1024 steps", "100 steps"],
            "answer": "10 steps",
            "explanation": "Binary search operates in O(log₂ n) time. For n = 1024: log₂(1024) = 10 steps (since 2¹⁰ = 1024). Linear scan would require up to 1024 steps."
        },
        "q_troubleshoot": {
            "badge": "🔧 Engineering Troubleshooting",
            "question": "An optical barcode scanner emits a failure beep when reading a product label. What is the most probable engineering cause?",
            "options": [
                "Insufficient optical reflectivity contrast between dark bars and white spaces, or a mismatched modulo 10 checksum",
                "The laser diode changed color emotionally",
                "The printed barcode ran out of internal battery",
                "The host computer is preoccupied with another calculation"
            ],
            "answer": "Insufficient optical reflectivity contrast between dark bars and white spaces, or a mismatched modulo 10 checksum",
            "explanation": "Optical readers rely on distinct photodiode reflection differentials. Low contrast or a corrupted check digit forces firmware to abort data entry."
        },
        "q_materials": {
            "badge": "🔬 Materials & Structural Mechanics",
            "question": "Why are integrated circuit microprocessors fabricated upon hyper-pure monocrystalline silicon wafers?",
            "options": [
                "Silicon provides an optimal semiconductor bandgap (≈1.1 eV) and native oxide (SiO2) serves as an outstanding nano-dielectric gate insulator",
                "Silicon conducts electricity faster than all metals",
                "Quartz sand converts into gold under current",
                "Silicon is completely transparent to human eyes"
            ],
            "answer": "Silicon provides an optimal semiconductor bandgap (≈1.1 eV) and native oxide (SiO2) serves as an outstanding nano-dielectric gate insulator",
            "explanation": "Silicon's bandgap allows controlled thermal switching at room temperature, while thermally grown SiO2 provides ideal dielectric isolation."
        },
        "q_data": {
            "badge": "📊 Empirical Data Analysis",
            "question": "Exponential pond lily growth: Population doubles each week (2^n). If at week 9 the pond is 50% covered, at what week will the pond be 100% full?",
            "options": ["Week 10", "Week 18", "Week 14", "Week 12"],
            "answer": "Week 10",
            "explanation": "In geometric progression with ratio 2: N(t+1) = 2 · N(t). If week 9 is 50%, week 10 doubles to 100%."
        }
    }
}

DOMAINS["biology"] = {
    "vie": {
        "law_name": "Định luật Chiếu sáng Nghịch đảo Bình phương & Cân bằng Sinh thái",
        "formula": "I = P / (4π · d²)  và  Tỉ số SA/V = Diện tích / Thể tích",
        "formula_unit": "Lux (Độ rọi), cm²/cm³ (Tỉ số bề mặt)",
        "mech": "Khí khổng điều hòa thoát hơi nước & Quang hợp (Stomata & Photosynthesis)",
        "metric": "Cường độ chiếu sáng sinh trưởng tối ưu I ≥ 500 Lux",
        "matching": [
            {"term": "I = P / (4π · d²)", "definition": "Định luật nghịch đảo bình phương: Cường độ ánh sáng tỉ lệ nghịch với bình phương khoảng cách"},
            {"term": "Tỉ số diện tích / thể tích (SA/V)", "definition": "Quyết định tốc độ trao đổi nhiệt và thoát hơi nước của sinh vật với môi trường"},
            {"term": "Quang hợp (Photosynthesis)", "definition": "Quá trình biến đổi quang năng và CO2 thành năng lượng hóa học glucose và khí oxy"},
            {"term": "Đơn vị Lux (lx)", "definition": "Đơn vị đo độ rọi chiếu sáng bề mặt sinh trưởng của thực vật trong hệ đo lường SI"}
        ],
        "cloze": [
            {"text": "Cường độ ánh sáng nhận được từ nguồn đèn tỉ lệ nghịch với [bình phương] khoảng cách từ đèn tới chậu cây.", "answer": "bình phương", "options": ["bình phương", "căn bậc hai", "tỉ lệ thuận", "lập phương"]},
            {"text": "Sinh vật có kích thước càng nhỏ thì tỉ số diện tích bề mặt trên thể tích (SA/V) càng [lớn], dẫn đến mất nhiệt nhanh hơn.", "answer": "lớn", "options": ["lớn", "nhỏ", "bằng không", "không đổi"]},
            {"text": "Khí khổng trên bề mặt lá cây đóng lại khi thời tiết khô nóng để ngăn ngừa sự [thoát hơi nước].", "answer": "thoát hơi nước", "options": ["thoát hơi nước", "quang hợp", "hấp thụ khoáng", "nở hoa"]},
            {"text": "Phương trình quang hợp chuyển hóa khí carbonic (CO2) và nước dưới ánh sáng thành đường glucose và khí [oxy].", "answer": "oxy", "options": ["oxy", "nito", "hydro", "cacbonic"]}
        ],
        "q_physics": {
            "badge": "⚛️ Vật lý & Nguyên lý Cơ chế",
            "question": "Theo định luật vật lý nghịch đảo bình phương khoảng cách (Inverse Square Law), khi ta tăng khoảng cách từ đèn trồng cây tới chậu lá lên gấp 3 lần, cường độ ánh sáng chiếu tới lá sẽ thay đổi thế nào?",
            "options": [
                "Giảm đi 9 lần (chỉ còn 1/9 so với ban đầu)",
                "Giảm đi 3 lần",
                "Tăng lên 3 lần",
                "Không đổi vì công suất bóng đèn giữ nguyên"
            ],
            "answer": "Giảm đi 9 lần (chỉ còn 1/9 so với ban đầu)",
            "explanation": "Quang thông lan tỏa đều trên bề mặt hình cầu diện tích S = 4π·d². Khi khoảng cách d tăng 3 lần, diện tích hình cầu tăng 3² = 9 lần, do đó cường độ rọi I = P / (4π·d²) giảm đi 9 lần."
        },
        "q_math": {
            "badge": "📐 Toán học Ứng dụng & Tính toán",
            "question": "Một chậu cây đặt cách đèn sinh học d1 = 0.5 m nhận được độ rọi I1 = 900 Lux. Nếu dời chậu cây ra xa tới khoảng cách d2 = 1.5 m (gấp 3 lần), độ rọi I2 đo được bằng cảm biến ánh sáng là bao nhiêu?",
            "options": ["100.0 Lux", "300.0 Lux", "450.0 Lux", "50.0 Lux"],
            "answer": "100.0 Lux",
            "explanation": "Theo định luật nghịch đảo bình phương: I2 / I1 = (d1 / d2)² = (0.5 / 1.5)² = (1/3)² = 1/9. Do đó I2 = 900 Lux / 9 = 100.0 Lux."
        },
        "q_troubleshoot": {
            "badge": "🔧 Xử lý Sự cố Kỹ thuật",
            "question": "Trong mô hình nhà kính tự động, cảm biến phát hiện lá cây bị héo úa và vàng mép dù đất vẫn ẩm ướt. Bước chuẩn đoán kỹ thuật nào sau đây là chuẩn xác nhất?",
            "options": [
                "Hệ thống thông gió bị tắt làm độ ẩm không khí đạt 100% bão hòa, ngăn cản cây thoát hơi nước để hút khoáng chất từ rễ",
                "Do cây bị chiếu quá nhiều ánh sáng màu xanh lục",
                "Do nước trong đất bị đông cứng ở 25 độ C",
                "Vì giun đất ăn hết rễ cây"
            ],
            "answer": "Hệ thống thông gió bị tắt làm độ ẩm không khí đạt 100% bão hòa, ngăn cản cây thoát hơi nước để hút khoáng chất từ rễ",
            "explanation": "Thoát hơi nước tạo áp suất âm (lực kéo hút) vận chuyển nước và khoáng chất từ rễ lên lá. Nếu độ ẩm không khí bão hòa 100% (không có thông gió đối lưu), sự thoát hơi nước ngừng trệ gây thiếu dinh dưỡng."
        },
        "q_materials": {
            "badge": "🔬 Khoa học Vật liệu & Kết cấu",
            "question": "Màng phủ nhà kính thông minh nông nghiệp công nghệ cao thường được chế tạo bằng vật liệu màng polymer ETFE hoặc Polycarbonate có ưu thế quang học nào?",
            "options": [
                "Độ truyền dẫn quang phổ ánh sáng khả dụng (PAR) cho quang hợp trên 90%, đồng thời giữ lại bức xạ hồng ngoại nhiệt sóng dài để chống rét",
                "Khả năng hấp thụ toàn bộ ánh sáng khả kiến và chỉ cho tia tử ngoại đi qua",
                "Vật liệu hoàn toàn phản xạ 100% ánh sáng mặt trời",
                "Vật liệu tự động chuyển hóa thành đất mùn sau 2 ngày"
            ],
            "answer": "Độ truyền dẫn quang phổ ánh sáng khả dụng (PAR) cho quang hợp trên 90%, đồng thời giữ lại bức xạ hồng ngoại nhiệt sóng dài để chống rét",
            "explanation": "Vật liệu nhà kính tối ưu cho dải bức xạ quang hợp PAR (400-700nm) đi qua tối đa, đồng thời cản tia hồng ngoại nhiệt bức xạ ngược ra ngoài tạo hiệu ứng giữ nhiệt ấm ban đêm."
        },
        "q_data": {
            "badge": "📊 Phân tích Dữ liệu Thực nghiệm",
            "question": "Một khối lập phương kích thước cạnh a = 2 cm có diện tích toàn phần SA = 24 cm² và thể tích V = 8 cm³ (tỉ số SA/V = 3.0 cm⁻¹). Khối lập phương lớn có cạnh a = 4 cm có tỉ số SA/V là bao nhiêu?",
            "options": ["1.5 cm⁻¹", "3.0 cm⁻¹", "6.0 cm⁻¹", "0.75 cm⁻¹"],
            "answer": "1.5 cm⁻¹",
            "explanation": "Với lập phương cạnh 4 cm: Diện tích SA = 6 × (4)² = 96 cm²; Thể tích V = (4)³ = 64 cm³. Tỉ số SA/V = 96 / 64 = 1.5 cm⁻¹ (giảm đi một nửa so với khối nhỏ)."
        }
    },
    "eng": {
        "law_name": "Inverse-Square Law & Ecological Equilibrium",
        "formula": "I = P / (4π · d²)  and  SA/V = Surface Area / Volume",
        "formula_unit": "Lux, cm⁻¹ (Surface-to-Volume Ratio)",
        "mech": "Stomatal Regulation & Photosynthetic Chloroplasts",
        "metric": "Optimal Photosynthetic Growth Irradiance I ≥ 500 Lux",
        "matching": [
            {"term": "I = P / (4π · d²)", "definition": "Inverse-Square Law: Light intensity decays inversely with distance squared"},
            {"term": "Surface-Area-to-Volume (SA/V)", "definition": "Governs rates of thermal dissipation and moisture transpiration with the environment"},
            {"term": "Photosynthesis", "definition": "Biochemical pathway converting light photons and CO2 into chemical glucose and O2"},
            {"term": "Lux (lx)", "definition": "Standard SI metric measuring surface illuminance incident upon botanical canopies"}
        ],
        "cloze": [
            {"text": "Illuminance incident upon a plant canopy decays with the [square] of distance from the grow light.", "answer": "square", "options": ["square", "square root", "direct proportion", "cube"]},
            {"text": "Smaller organisms exhibit a significantly [higher] Surface-Area-to-Volume ratio, losing body heat faster.", "answer": "higher", "options": ["higher", "lower", "zero", "constant"]},
            {"text": "Leaf stomata close during arid heat to inhibit excessive moisture [transpiration].", "answer": "transpiration", "options": ["transpiration", "photosynthesis", "mineral uptake", "flowering"]},
            {"text": "Photosynthesis combines water and atmospheric carbon dioxide into carbohydrates and gaseous [oxygen].", "answer": "oxygen", "options": ["oxygen", "nitrogen", "hydrogen", "carbon monoxide"]}
        ],
        "q_physics": {
            "badge": "⚛️ Physics Principles & Mechanisms",
            "question": "According to the physical Inverse-Square Law, tripling the distance from a grow lamp to a plant reduces incident light intensity by what factor?",
            "options": [
                "Decreases by a factor of 9 (down to 1/9 of initial illuminance)",
                "Decreases by a factor of 3",
                "Increases threefold",
                "Remains constant because lamp power is fixed"
            ],
            "answer": "Decreases by a factor of 9 (down to 1/9 of initial illuminance)",
            "explanation": "Luminous flux radiates isotropically over a sphere of area S = 4π·d². Tripling distance d multiplies spherical area by 3² = 9, reducing illuminance I = P / (4π·d²) to 1/9."
        },
        "q_math": {
            "badge": "📐 Applied Math & Calculation",
            "question": "A specimen at d1 = 0.5 m receives illuminance I1 = 900 Lux. If moved to d2 = 1.5 m (triple distance), what is the new illuminance I2 measured by a light sensor?",
            "options": ["100.0 Lux", "300.0 Lux", "450.0 Lux", "50.0 Lux"],
            "answer": "100.0 Lux",
            "explanation": "By the inverse-square law: I2 / I1 = (d1 / d2)² = (0.5 / 1.5)² = (1/3)² = 1/9. Therefore I2 = 900 Lux / 9 = 100.0 Lux."
        },
        "q_troubleshoot": {
            "badge": "🔧 Engineering Troubleshooting",
            "question": "In an automated greenhouse, plants wilt despite moist soil. What is the root environmental diagnosis?",
            "options": [
                "Ventilation fans failed, causing 100% relative humidity saturation that halts transpirational xylem nutrient pull",
                "Plants received excess green photons",
                "Soil moisture froze solid at 25 degrees Celsius",
                "Earthworms consumed the root network"
            ],
            "answer": "Ventilation fans failed, causing 100% relative humidity saturation that halts transpirational xylem nutrient pull",
            "explanation": "Transpiration generates negative pressure pulling water and dissolved nutrients from roots. At 100% relative humidity without convective air exchange, transpiration stalls."
        },
        "q_materials": {
            "badge": "🔬 Materials & Structural Mechanics",
            "question": "Why do modern horticultural enclosures employ ETFE fluoropolymer or twin-wall polycarbonate glazing?",
            "options": [
                "They transmit >90% of Photosynthetically Active Radiation (PAR) while trapping thermal longwave infrared radiation",
                "They absorb all visible light while transmitting only ultraviolet rays",
                "They reflect 100% of solar radiation",
                "They biodegrade into soil within 2 days"
            ],
            "answer": "They transmit >90% of Photosynthetically Active Radiation (PAR) while trapping thermal longwave infrared radiation",
            "explanation": "Optimal glazing permits high transmission of PAR wavelengths (400-700nm) while maintaining high thermal emissivity barriers to prevent nocturnal radiative cooling."
        },
        "q_data": {
            "badge": "📊 Empirical Data Analysis",
            "question": "A small cubic organism with side a = 2 cm has surface area 24 cm² and volume 8 cm³ (SA/V = 3.0 cm⁻¹). What is the SA/V ratio for a larger cube with side a = 4 cm?",
            "options": ["1.5 cm⁻¹", "3.0 cm⁻¹", "6.0 cm⁻¹", "0.75 cm⁻¹"],
            "answer": "1.5 cm⁻¹",
            "explanation": "For a = 4 cm: Surface Area = 6 × (4)² = 96 cm²; Volume = (4)³ = 64 cm³. Ratio SA/V = 96 / 64 = 1.5 cm⁻¹ (halved compared to the small cube)."
        }
    }
}

import enrich_all_stem_practice_and_quiz as m1
DOMAINS["bridge"] = m1.MASTER_SPECS["bridge"]
DOMAINS["mechanism"] = {
    "vie": m1.get_domain_spec("mechanism", True),
    "eng": m1.get_domain_spec("mechanism", False)
}
DOMAINS["vehicle"] = {
    "vie": m1.get_domain_spec("vehicle", True),
    "eng": m1.get_domain_spec("vehicle", False)
}

print(f"Loaded {len(DOMAINS)} dedicated domains.")

# Master Enrichment Procedure
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

total_processed = 0

for lvl in data:
    for lang in lvl.get("languages", []):
        lang_code = lang.get("lang", "VIE")
        is_vie = (lang_code == "VIE")
        for t in lang.get("topics", []):
            topic_name = t.get("topicName", "")
            for lec in t.get("lectures", []):
                title = lec.get("title", "")
                cat = detect_category(title, topic_name)
                spec = DOMAINS[cat]["vie" if is_vie else "eng"]
                
                lp = lec.get("lessonPlan", {})
                crits = lp.get("challenge", {}).get("criteria", [])
                constrs = lp.get("challenge", {}).get("constraints", [])
                crit_str = crits[0] if crits else ("Hoàn thành mô hình đúng thông số kỹ thuật" if is_vie else "Complete model to technical specifications")
                const_str = constrs[0] if constrs else ("Chỉ sử dụng các vật tư trong danh mục" if is_vie else "Use only permitted materials")
                
                # Q1 EDP
                q1 = {
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
                
                lec["quizData"] = [
                    q1,
                    {
                        "type": "multiple_choice",
                        "badge": spec["q_physics"]["badge"],
                        "question": spec["q_physics"]["question"],
                        "options": spec["q_physics"]["options"],
                        "answer": spec["q_physics"]["answer"],
                        "explanation": spec["q_physics"]["explanation"]
                    },
                    {
                        "type": "multiple_choice",
                        "badge": spec["q_math"]["badge"],
                        "question": spec["q_math"]["question"],
                        "options": spec["q_math"]["options"],
                        "answer": spec["q_math"]["answer"],
                        "explanation": spec["q_math"]["explanation"]
                    },
                    {
                        "type": "multiple_choice",
                        "badge": spec["q_troubleshoot"]["badge"],
                        "question": spec["q_troubleshoot"]["question"],
                        "options": spec["q_troubleshoot"]["options"],
                        "answer": spec["q_troubleshoot"]["answer"],
                        "explanation": spec["q_troubleshoot"]["explanation"]
                    },
                    {
                        "type": "multiple_choice",
                        "badge": spec["q_materials"]["badge"],
                        "question": spec["q_materials"]["question"],
                        "options": spec["q_materials"]["options"],
                        "answer": spec["q_materials"]["answer"],
                        "explanation": spec["q_materials"]["explanation"]
                    },
                    {
                        "type": "multiple_choice",
                        "badge": spec["q_data"]["badge"],
                        "question": spec["q_data"]["question"],
                        "options": spec["q_data"]["options"],
                        "answer": spec["q_data"]["answer"],
                        "explanation": spec["q_data"]["explanation"]
                    }
                ]
                
                # Practice Data
                lec["practiceData"] = {
                    "flashcards": [
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
                    ],
                    "matching": spec["matching"],
                    "sequencing": [
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
                    ],
                    "cloze": spec["cloze"]
                }
                
                total_processed += 1

print(f"Master processing complete for all {total_processed} lessons.")

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("data.js", "w", encoding="utf-8") as f:
    f.write("// STEM LMS Global Curriculum Dataset (Enriched Math & Physics)\n")
    f.write("window.APP_DATA = ")
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print("Saved to data.json and mirrored to data.js successfully!")
