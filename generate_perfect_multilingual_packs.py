#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Curriculum Master Orchestrator:
- Generates 100% synchronized multilingual content for all 4 educational levels.
- Fixes practice card empty data by providing front/back, left/right, term/definition, stepNumber/text, and cloze options.
- Fixes Vietnamese orthography and enforces NFC Unicode.
- Ensures ENG lessons have 100% English quiz and practice.
"""

import json
import os
import copy
import unicodedata

def clean_text(text):
    if not isinstance(text, str):
        return text
    text = unicodedata.normalize('NFC', text)
    replacements = {
        'Thiết kế': 'Thiết kế',
        'thiết kế': 'thiết kế',
        'thủy điện': 'thủy điện',
        'thuỷ điện': 'thủy điện',
        'Cứu hộ': 'Cứu hộ',
        'cứu hộ': 'cứu hộ',
        'Kỹ thuật': 'Kỹ thuật',
        'kỹ thuật': 'kỹ thuật',
        'cáp tr eo': 'cáp treo',
        'đê đập': 'đê đập',
        'đập thủy': 'đập thủy',
        'lặp đặt': 'lắp đặt',
        'dây chuyền lắp ráp': 'Dây chuyền lắp ráp'
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text

def normalize_object(obj):
    if isinstance(obj, str):
        return clean_text(obj)
    elif isinstance(obj, list):
        return [normalize_object(item) for item in obj]
    elif isinstance(obj, dict):
        return {clean_text(k): normalize_object(v) for k, v in obj.items()}
    return obj

from packs.kindergarten_pack import KINDERGARTEN_PACK
from packs.primary_pack import PRIMARY_PACK

# Load base packs
KIND_VIE = KINDERGARTEN_PACK['VIE']
KIND_ENG = KINDERGARTEN_PACK['ENG']
PRIM_VIE = PRIMARY_PACK['VIE']
PRIM_ENG = PRIMARY_PACK['ENG']

# Build Middle VIE & ENG
MID_VIE = copy.deepcopy(PRIM_VIE)
MID_ENG = copy.deepcopy(PRIM_ENG)

# Aerospace THCS
MID_VIE['aerospace']['quiz'][0] = {
    'question': "🎯 Trong dự án kỹ thuật không gian THCS '{title}', điều kiện để tên lửa nước hoặc máy bay giữ được quỹ đạo ổn định là gì?",
    'options': ["Tâm áp suất khí động (CP) phải nằm lùi về phía sau so với Trọng tâm (CG)", "Tâm áp suất phải nằm phía trước trọng tâm", "Không cần cánh đuôi", "Đầu mũi tên lửa phải dẹt phẳng"],
    'answer': "Tâm áp suất khí động (CP) phải nằm lùi về phía sau so với Trọng tâm (CG)",
    'explanation': "Tâm áp suất (CP) nằm sau trọng tâm (CG) tạo mô-men hồi phục khí động giúp phương tiện tự ổn định hướng bay."
}
MID_VIE['aerospace']['quiz'][1] = {
    'question': "⚛️ Định luật III Newton giải thích lực đẩy phản lực của tên lửa nước như thế nào?",
    'options': ["Khí nén tống nước phụt xuống dưới sinh phản lực hướng lên trên đẩy tên lửa bay lên", "Không khí hút tên lửa lên", "Nước tự biến thành xăng", "Trái Đất mất trọng lực"],
    'answer': "Khí nén tống nước phụt xuống dưới sinh phản lực hướng lên trên đẩy tên lửa bay lên",
    'explanation': "Theo định luật III Newton, lực tác dụng và phản lực bằng nhau về độ lớn và ngược chiều: F_tên_lửa = - F_nước."
}
MID_VIE['aerospace']['quiz'][2] = {
    'question': "📐 Tên lửa nước khối lượng m = 0.2 kg đạt tới độ cao cực đại h = 45 mét (g = 10 m/s²). Thế năng hấp dẫn của tên lửa tại đỉnh quỹ đạo là bao nhiêu?",
    'options': ["90 J (Joule)", "450 J", "9 J", "150 J"],
    'answer': "90 J (Joule)",
    'explanation': "Thế năng hấp dẫn THCS: W_t = m x g x h = 0.2 x 10 x 45 = 90 J."
}

MID_ENG['aerospace']['quiz'][0] = {
    'question': "🎯 In the middle school aerospace challenge '{title}', what condition ensures passive aerodynamic flight stability?",
    'options': ["Center of Pressure (CP) must lie behind the Center of Gravity (CG)", "CP must be in front of CG", "Fins are not required", "Flat nose cone"],
    'answer': "Center of Pressure (CP) must lie behind the Center of Gravity (CG)",
    'explanation': "Placing CP behind CG creates an aerodynamic restoring torque that keeps the rocket pointed straight."
}
MID_ENG['aerospace']['quiz'][1] = {
    'question': "⚛️ How does Newton's Third Law explain water rocket reaction thrust?",
    'options': ["Expelling water downward generates an equal and opposite reaction force pushing the rocket upward", "Air pulls the rocket up", "Water turns to fuel", "Gravity turns off"],
    'answer': "Expelling water downward generates an equal and opposite reaction force pushing the rocket upward",
    'explanation': "For every action force there is an equal and opposite reaction force: F_rocket = - F_water."
}
MID_ENG['aerospace']['quiz'][2] = {
    'question': "📐 A water rocket (m = 0.2 kg) reaches peak altitude h = 45 m (g = 10 m/s²). What is its gravitational potential energy at apogee?",
    'options': ["90 Joules (J)", "450 Joules (J)", "9 Joules (J)", "150 Joules (J)"],
    'answer': "90 Joules (J)",
    'explanation': "PE = m x g x h = 0.2 x 10 x 45 = 90 J."
}

# Marine THCS
MID_VIE['marine']['quiz'][0] = {
    'question': "🎯 Trong bài toán đóng tàu THCS '{title}', điều kiện để con tàu nổi cân bằng trên mặt nước theo định luật Ác-si-mét là gì?",
    'options': ["Trọng lượng P của con tàu bằng với Lực đẩy Ác-si-mét F_A: P = F_A", "Trọng lượng P lớn hơn lực đẩy F_A", "Tàu phải có khối lượng bằng 0", "Lực đẩy hướng sang ngang"],
    'answer': "Trọng lượng P của con tàu bằng với Lực đẩy Ác-si-mét F_A: P = F_A",
    'explanation': "Khi nổi cân bằng trên mặt thoáng, hai lực trực đối triệt tiêu nhau: Trọng lực P cân bằng với Lực đẩy Ác-si-mét F_A."
}
MID_VIE['marine']['quiz'][1] = {
    'question': "⚛️ Lực đẩy Ác-si-mét tác dụng lên phần chìm của vật trong chất lỏng được tính theo công thức nào?",
    'options': ["F_A = d x V (với d là trọng lượng riêng của chất lỏng, V là thể tích phần chìm)", "F_A = m x v", "F_A = P : S", "F_A = I x U"],
    'answer': "F_A = d x V (với d là trọng lượng riêng của chất lỏng, V là thể tích phần chìm)",
    'explanation': "F_A = d x V, trong đó d tính bằng N/m³ và V tính bằng m³."
}
MID_VIE['marine']['quiz'][2] = {
    'question': "📐 Mô hình tàu có thể tích phần chìm V = 0.003 m³ trong nước ngọt (d = 10.000 N/m³). Lực đẩy Ác-si-mét tác dụng lên mô hình là:",
    'options': ["30 N (Newton)", "300 N", "3 N", "0.3 N"],
    'answer': "30 N (Newton)",
    'explanation': "F_A = d x V = 10.000 x 0.003 = 30 N."
}

MID_ENG['marine']['quiz'][0] = {
    'question': "🎯 In the vessel design project '{title}', what is the condition for static floating equilibrium under Archimedes' principle?",
    'options': ["Total vessel weight P equals buoyant force F_A: P = F_A", "Weight exceeds buoyant force", "Vessel mass equals zero", "Buoyancy pushes horizontally"],
    'answer': "Total vessel weight P equals buoyant force F_A: P = F_A",
    'explanation': "When floating in static equilibrium, downward weight equals upward buoyant force (P = F_A)."
}
MID_ENG['marine']['quiz'][1] = {
    'question': "⚛️ What formula calculates buoyant force acting on the submerged volume of a floating body?",
    'options': ["F_A = d x V (where d is fluid specific weight and V is submerged volume)", "F_A = m x v", "F_A = P : S", "F_A = I x U"],
    'answer': "F_A = d x V (where d is fluid specific weight and V is submerged volume)",
    'explanation': "Archimedes' principle: F_A = d x V, where d is in N/m³ and V is in m³."
}
MID_ENG['marine']['quiz'][2] = {
    'question': "📐 A model boat has submerged volume V = 0.003 m³ in fresh water (d = 10,000 N/m³). What buoyant force acts on the hull?",
    'options': ["30 N (Newtons)", "300 N", "3 N", "0.3 N"],
    'answer': "30 N (Newtons)",
    'explanation': "F_A = d x V = 10,000 x 0.003 = 30 N."
}

# Circuit THCS
MID_VIE['circuit']['quiz'][0] = {
    'question': "🎯 Trong thiết kế mạch điện THCS '{title}', định luật Ôm cho đoạn mạch được phát biểu bằng công thức nào?",
    'options': ["I = U / R (Cường độ dòng điện tỷ lệ thuận với hiệu điện thế U và tỷ lệ nghịch với điện trở R)", "I = U x R", "I = R / U", "I = U + R"],
    'answer': "I = U / R (Cường độ dòng điện tỷ lệ thuận với hiệu điện thế U và tỷ lệ nghịch với điện trở R)",
    'explanation': "Định luật Ôm: I = U / R (A = V / Ω)."
}
MID_VIE['circuit']['quiz'][1] = {
    'question': "⚛️ Hai điện trở R1 = 20 Ω và R2 = 30 Ω mắc song song. Điện trở tương đương R_td của đoạn mạch là:",
    'options': ["12 Ω", "50 Ω", "600 Ω", "10 Ω"],
    'answer': "12 Ω",
    'explanation': "R_td = (R1 x R2) / (R1 + R2) = (20 x 30) / (20 + 30) = 600 / 50 = 12 Ω."
}
MID_VIE['circuit']['quiz'][2] = {
    'question': "📐 Mắc đoạn mạch song song trên vào hiệu điện thế nguồn U = 12V. Cường độ dòng điện mạch chính I = U / R_td là:",
    'options': ["1.0 A (Ampere)", "144 A", "0.5 A", "2.0 A"],
    'answer': "1.0 A (Ampere)",
    'explanation': "I = 12 / 12 = 1.0 A."
}

MID_ENG['circuit']['quiz'][0] = {
    'question': "🎯 In the middle school circuit lab '{title}', what formula expresses Ohm's Law for a circuit branch?",
    'options': ["I = U / R (Current is directly proportional to voltage and inversely proportional to resistance)", "I = U x R", "I = R / U", "I = U + R"],
    'answer': "I = U / R (Current is directly proportional to voltage and inversely proportional to resistance)",
    'explanation': "Ohm's Law: I = U / R."
}
MID_ENG['circuit']['quiz'][1] = {
    'question': "⚛️ Two resistors R1 = 20 Ω and R2 = 30 Ω are wired in parallel. What is the equivalent resistance R_eq?",
    'options': ["12 Ω", "50 Ω", "600 Ω", "10 Ω"],
    'answer': "12 Ω",
    'explanation': "Parallel equivalent resistance: R_eq = (20 x 30) / (20 + 30) = 600 / 50 = 12 Ω."
}
MID_ENG['circuit']['quiz'][2] = {
    'question': "📐 Connecting the parallel branch across a 12V source, what is the main line current I = U / R_eq?",
    'options': ["1.0 A (Ampere)", "144 A", "0.5 A", "2.0 A"],
    'answer': "1.0 A (Ampere)",
    'explanation': "I = 12 / 12 = 1.0 A."
}

# Mechanism THCS
MID_VIE['mechanism']['quiz'][0] = {
    'question': "🎯 Trong bài toán đòn bẩy THCS '{title}', điều kiện cân bằng khi có hai lực F1 và F2 tác dụng là:",
    'options': ["F1 x l1 = F2 x l2 (với l1, l2 là cánh tay đòn của các lực tương ứng)", "F1 + l1 = F2 + l2", "F1 = F2", "l1 = l2"],
    'answer': "F1 x l1 = F2 x l2 (với l1, l2 là cánh tay đòn của các lực tương ứng)",
    'explanation': "Quy tắc đòn bẩy: Mô-men lực hai phía điểm tựa phải cân bằng nhau: F1 x l1 = F2 x l2."
}
MID_VIE['mechanism']['quiz'][1] = {
    'question': "⚛️ Định luật về công khẳng định điều gì khi sử dụng các máy cơ đơn giản?",
    'options': ["Không máy cơ đơn giản nào cho ta lợi về công: Được lợi bao nhiêu lần về lực thì thiệt bấy nhiêu lần về đường đi", "Máy cơ tăng công lên 2 lần", "Máy cơ triệt tiêu công", "Lợi cả lực và đường đi"],
    'answer': "Không máy cơ đơn giản nào cho ta lợi về công: Được lợi bao nhiêu lần về lực thì thiệt bấy nhiêu lần về đường đi",
    'explanation': "Định luật bảo toàn công cơ học: A = F x s luôn được bảo toàn (bỏ qua ma sát)."
}
MID_VIE['mechanism']['quiz'][2] = {
    'question': "📐 Nâng vật nặng P = 600 N bằng đòn bẩy. Cánh tay đòn tải l2 = 0.2 m, cánh tay đòn lực ấn l1 = 1.2 m. Lực ấn F1 tối thiểu là:",
    'options': ["100 N (Newton)", "3600 N", "600 N", "50 N"],
    'answer': "100 N (Newton)",
    'explanation': "F1 = P x (l2 / l1) = 600 x (0.2 / 1.2) = 100 N."
}

MID_ENG['mechanism']['quiz'][0] = {
    'question': "🎯 In the middle school lever challenge '{title}', what is the rotational equilibrium condition for two applied forces?",
    'options': ["F1 x l1 = F2 x l2 (where l1 and l2 are lever arm distances)", "F1 + l1 = F2 + l2", "F1 = F2", "l1 = l2"],
    'answer': "F1 x l1 = F2 x l2 (where l1 and l2 are lever arm distances)",
    'explanation': "Lever law requires opposing torque moments around the pivot to balance: F1 x l1 = F2 x l2."
}
MID_ENG['mechanism']['quiz'][1] = {
    'question': "⚛️ What fundamental principle of work applies to all simple machines?",
    'options': ["No simple machine provides a work advantage: A gain in force corresponds to an equal loss in distance", "Machines multiply work done", "Machines destroy work", "Gain in both force and distance"],
    'answer': "No simple machine provides a work advantage: A gain in force corresponds to an equal loss in distance",
    'explanation': "Conservation of mechanical work: Work input equals work output (neglecting friction): W = F x d."
}
MID_ENG['mechanism']['quiz'][2] = {
    'question': "📐 Lifting a 600 N load with a lever where load arm l2 = 0.2 m and effort arm l1 = 1.2 m. What is minimum effort F1?",
    'options': ["100 N (Newtons)", "3600 N", "600 N", "50 N"],
    'answer': "100 N (Newtons)",
    'explanation': "F1 = 600 x (0.2 / 1.2) = 100 N."
}

# Biology THCS
MID_VIE['biology']['quiz'][0] = {
    'question': "🎯 Trong dự án cáp treo cứu hộ Rover vượt hẻm núi '{title}', cơ cấu ròng rọc động giúp giảm lực kéo như thế nào?",
    'options': ["Lực kéo giảm một nửa (F = P / 2), đổi lại quãng đường kéo dây tăng gấp đôi", "Lực kéo tăng gấp đôi", "Không làm thay đổi lực", "Lực kéo giảm về 0"],
    'answer': "Lực kéo giảm một nửa (F = P / 2), đổi lại quãng đường kéo dây tăng gấp đôi",
    'explanation': "Ròng rọc động chia đôi tải trọng lên hai nhánh dây, mang lại lợi thế cơ học 2:1 theo định luật về công."
}
MID_VIE['biology']['quiz'][1] = {
    'question': "⚛️ Khi căng dây cáp qua hẻm núi, tại sao không thể kéo dây căng thẳng tắp tuyệt đối (góc chùng θ = 0)?",
    'options': ["Vì lực căng dây cáp T = P / (2 sin θ), khi θ tiến về 0 thì lực căng T tiến tới vô cùng làm đứt dây cáp", "Vì dây cáp bị bay lên trời", "Vì dây cáp tự động co ngắn lại", "Vì gió thổi ngược"],
    'answer': "Vì lực căng dây cáp T = P / (2 sin θ), khi θ tiến về 0 thì lực căng T tiến tới vô cùng làm đứt dây cáp",
    'explanation': "Cân bằng tĩnh học: 2T sin θ = P => T = P / (2 sin θ). Để triệt tiêu hoàn toàn góc chùng (θ = 0), lực căng cần thiết là vô hạn."
}
MID_VIE['biology']['quiz'][2] = {
    'question': "📐 Chú chó Rover cùng cáng có tổng trọng lượng P = 160 N. Dùng 1 ròng rọc động để kéo cáng lên cao h = 3 mét. Lực kéo F và quãng đường kéo dây s là:",
    'options': ["F = 80 N và s = 6 mét", "F = 160 N và s = 3 mét", "F = 40 N và s = 12 mét", "F = 320 N và s = 1.5 mét"],
    'answer': "F = 80 N và s = 6 mét",
    'explanation': "Lợi 2 lần về lực (F = 160 / 2 = 80 N) thì thiệt 2 lần về đường đi (s = 3 x 2 = 6 m)."
}

MID_ENG['biology']['quiz'][0] = {
    'question': "🎯 In the rescue rover aerial cable challenge '{title}', how does a movable pulley reduce the effort force?",
    'options': ["Effort force is halved (F = P / 2) while rope haul distance doubles", "Effort force doubles", "No change in force", "Force drops to zero"],
    'answer': "Effort force is halved (F = P / 2) while rope haul distance doubles",
    'explanation': "A movable pulley splits the payload weight across two supporting rope strands, yielding 2:1 mechanical advantage."
}
MID_ENG['biology']['quiz'][1] = {
    'question': "⚛️ Why can a suspended cable across a gorge never be pulled perfectly horizontal (sag angle θ = 0)?",
    'options': ["Cable tension T = P / (2 sin θ); as θ approaches 0, tension approaches infinity causing cable failure", "Cable floats into space", "Cable shrinks automatically", "Wind prevents it"],
    'answer': "Cable tension T = P / (2 sin θ); as θ approaches 0, tension approaches infinity causing cable failure",
    'explanation': "Vertical equilibrium 2T sin θ = P requires infinite tension to balance downward weight if sag angle θ is zero."
}
MID_ENG['biology']['quiz'][2] = {
    'question': "📐 Rover and carrier have combined weight P = 160 N. Using a single movable pulley to lift height h = 3 m, what are effort F and haul distance s?",
    'options': ["Effort F = 80 N and haul distance s = 6 meters", "F = 160 N and s = 3 m", "F = 40 N and s = 12 m", "F = 320 N and s = 1.5 m"],
    'answer': "Effort F = 80 N and haul distance s = 6 meters",
    'explanation': "Effort is halved: 160 / 2 = 80 N. Haul distance doubles: 3 x 2 = 6 m."
}

# Build High School VIE & ENG
HIGH_VIE = copy.deepcopy(MID_VIE)
HIGH_ENG = copy.deepcopy(MID_ENG)

# Aerospace THPT
HIGH_VIE['aerospace']['quiz'][0] = {
    'question': "🎯 Trong bài toán tối ưu hóa khí động học THPT '{title}', phương trình lực nâng Kutta-Joukowski cánh máy bay được tính bằng công thức nào?",
    'options': ["L = 0.5 x ρ x v² x S x C_L (với ρ là mật độ không khí, v là vận tốc, S là diện tích cánh, C_L là hệ số nâng)", "L = m x g", "L = p x V", "L = I² x R"],
    'answer': "L = 0.5 x ρ x v² x S x C_L (với ρ là mật độ không khí, v là vận tốc, S là diện tích cánh, C_L là hệ số nâng)",
    'explanation': "Lực nâng khí động học tỷ lệ thuận với bình phương vận tốc v², diện tích cánh S và hệ số C_L."
}
HIGH_VIE['aerospace']['quiz'][1] = {
    'question': "⚛️ Phương trình Bernoulli cho dòng chất lưu dừng dọc theo một đường dòng được viết là:",
    'options': ["p + 0.5 x ρ x v² + ρ x g x h = const", "p x V = const", "F = m x a", "E = m x c²"],
    'answer': "p + 0.5 x ρ x v² + ρ x g x h = const",
    'explanation': "Định luật bảo toàn năng lượng cho chất lưu: tổng áp suất tĩnh, áp suất động và áp suất thế là hằng số."
}
HIGH_VIE['aerospace']['quiz'][2] = {
    'question': "📐 Cánh máy bay diện tích S = 0.2 m², C_L = 0.8 bay trong không khí (ρ = 1.25 kg/m³) với vận tốc v = 20 m/s. Lực nâng L sinh ra là:",
    'options': ["40 N (Newton)", "20 N", "400 N", "8 N"],
    'answer': "40 N (Newton)",
    'explanation': "L = 0.5 x 1.25 x 20² x 0.2 x 0.8 = 0.5 x 1.25 x 400 x 0.16 = 40 N."
}

HIGH_ENG['aerospace']['quiz'][0] = {
    'question': "🎯 In the high school aerodynamics project '{title}', what analytical equation calculates total aerodynamic lift?",
    'options': ["L = 0.5 x ρ x v² x S x C_L", "L = m x g", "L = p x V", "L = I² x R"],
    'answer': "L = 0.5 x ρ x v² x S x C_L",
    'explanation': "Lift is proportional to air density, square of velocity, reference wing area, and lift coefficient."
}
HIGH_ENG['aerospace']['quiz'][1] = {
    'question': "⚛️ Which form expresses Bernoulli's equation for steady incompressible flow along a streamline?",
    'options': ["p + 0.5 x ρ x v² + ρ x g x h = const", "p x V = const", "F = m x a", "E = m x c²"],
    'answer': "p + 0.5 x ρ x v² + ρ x g x h = const",
    'explanation': "Conservation of mechanical energy along a streamline equates static, dynamic, and hydrostatic pressure terms."
}
HIGH_ENG['aerospace']['quiz'][2] = {
    'question': "📐 A model wing (S = 0.2 m², C_L = 0.8) flies through air (ρ = 1.25 kg/m³) at speed v = 20 m/s. What is generated lift L?",
    'options': ["40 N (Newtons)", "20 N", "400 N", "8 N"],
    'answer': "40 N (Newtons)",
    'explanation': "L = 0.5 x 1.25 x 20² x 0.2 x 0.8 = 40 N."
}

# Energy Renewable THPT
HIGH_VIE['energy_renewable']['quiz'][0] = {
    'question': "🎯 Theo định luật khí động học Betz, giới hạn lý thuyết tối đa về hiệu suất khí động (C_p) của turbine gió là:",
    'options': ["16/27 (khoảng 59.3%)", "100%", "85.5%", "25%"],
    'answer': "16/27 (khoảng 59.3%)",
    'explanation': "Giới hạn Betz chứng minh không turbine gió nào chuyển đổi quá 16/27 (≈ 59.3%) động năng gió thành công."
}
HIGH_VIE['energy_renewable']['quiz'][1] = {
    'question': "⚛️ Công suất khả dụng trong luồng gió thổi qua diện tích quét A phụ thuộc vào vận tốc gió v theo hàm số bậc mấy?",
    'options': ["Bậc ba của vận tốc gió: P = 0.5 x ρ x A x v³", "Bậc nhất theo v", "Bậc hai theo v²", "Không phụ thuộc v"],
    'answer': "Bậc ba của vận tốc gió: P = 0.5 x ρ x A x v³",
    'explanation': "P = 0.5 x ρ x A x v³. Khi vận tốc gió tăng gấp đôi (2v), công suất gió tăng gấp 2³ = 8 lần."
}
HIGH_VIE['energy_renewable']['quiz'][2] = {
    'question': "📐 Turbine gió có diện tích quét A = 10 m², gió thổi v = 10 m/s (ρ = 1.2 kg/m³). Công suất gió toàn phần là:",
    'options': ["6.000 W hay 6 kW", "1.200 W", "600 W", "120 W"],
    'answer': "6.000 W hay 6 kW",
    'explanation': "P = 0.5 x 1.2 x 10 x 10³ = 6 x 1000 = 6.000 W = 6 kW."
}

HIGH_ENG['energy_renewable']['quiz'][0] = {
    'question': "🎯 According to Betz's aerodynamic limit, what is the theoretical maximum power coefficient C_p for an ideal wind turbine?",
    'options': ["16/27 (approximately 59.3%)", "100%", "85.5%", "25%"],
    'answer': "16/27 (approximately 59.3%)",
    'explanation': "Betz's Law proves that no wind turbine can capture more than 16/27 (59.3%) of incoming kinetic wind energy."
}
HIGH_ENG['energy_renewable']['quiz'][1] = {
    'question': "⚛️ Power available in an airflow passing rotor swept area A varies with wind speed v according to which power relationship?",
    'options': ["Cubic power of velocity: P = 0.5 x ρ x A x v³", "Linear with v", "Square of v", "Independent of v"],
    'answer': "Cubic power of velocity: P = 0.5 x ρ x A x v³",
    'explanation': "P = 0.5 x ρ x A x v³. Doubling wind velocity (2v) increases available power by 2³ = 8 times."
}
HIGH_ENG['energy_renewable']['quiz'][2] = {
    'question': "📐 A wind turbine has rotor swept area A = 10 m² in v = 10 m/s airflow (ρ = 1.2 kg/m³). What is total wind power?",
    'options': ["6,000 W (6 kW)", "1,200 W", "600 W", "120 W"],
    'answer': "6,000 W (6 kW)",
    'explanation': "P = 0.5 x 1.2 x 10 x 10³ = 6,000 W = 6 kW."
}

# Complete circuit THPT
HIGH_VIE['circuit']['quiz'][0] = {
    'question': "🎯 Định luật Ôm cho toàn mạch kín chứa nguồn điện có suất điện động E và điện trở trong r được biểu diễn bằng công thức nào?",
    'options': ["I = E / (R_N + r) (Cường độ dòng điện bằng suất điện động chia cho tổng trở toàn mạch)", "I = U / R_N", "I = E x r", "I = R_N / E"],
    'answer': "I = E / (R_N + r) (Cường độ dòng điện bằng suất điện động chia cho tổng trở toàn mạch)",
    'explanation': "Định luật Ôm cho toàn mạch THPT: I = E / (R_N + r)."
}
HIGH_VIE['circuit']['quiz'][1] = {
    'question': "⚛️ Định lý truyền công suất cực đại khẳng định công suất tiêu thụ trên mạch ngoài R_N đạt giá trị lớn nhất khi nào?",
    'options': ["Điện trở mạch ngoài bằng đúng điện trở trong của nguồn: R_N = r", "R_N = 0", "R_N tiến tới vô cùng", "Không bao giờ đạt cực đại"],
    'answer': "Điện trở mạch ngoài bằng đúng điện trở trong của nguồn: R_N = r",
    'explanation': "Khảo sát hàm P_ngoài = E²R_N / (R_N + r)², áp dụng bất đẳng thức Cauchy cực đại xảy ra khi R_N = r."
}
HIGH_VIE['circuit']['quiz'][2] = {
    'question': "📐 Nguồn điện có E = 12V, r = 2Ω nối với mạch ngoài R_N = 4Ω. Cường độ dòng điện I chạy qua toàn mạch là:",
    'options': ["2.0 A (Ampere)", "3.0 A", "6.0 A", "1.0 A"],
    'answer': "2.0 A (Ampere)",
    'explanation': "I = E / (R_N + r) = 12 / (4 + 2) = 12 / 6 = 2.0 A."
}

HIGH_ENG['circuit']['quiz'][0] = {
    'question': "🎯 What equation expresses Ohm's Law for a complete closed circuit with EMF E and internal resistance r?",
    'options': ["I = E / (R_N + r)", "I = U / R", "I = E x r", "I = R / E"],
    'answer': "I = E / (R_N + r)",
    'explanation': "Complete circuit Ohm's Law: I = E / (R_load + r_internal)."
}
HIGH_ENG['circuit']['quiz'][1] = {
    'question': "⚛️ The maximum power transfer theorem states that external load power P_load is maximized when:",
    'options': ["Load resistance matches source internal resistance: R_load = r", "R_load = 0", "R_load approaches infinity", "Never maximized"],
    'answer': "Load resistance matches source internal resistance: R_load = r",
    'explanation': "Setting dP/dR_load = 0 demonstrates maximum power transfer occurs when R_load equals internal resistance r."
}
HIGH_ENG['circuit']['quiz'][2] = {
    'question': "📐 A DC source with EMF E = 12V and r = 2Ω connects to external load R_load = 4Ω. What is circuit current I?",
    'options': ["2.0 A (Amperes)", "3.0 A", "6.0 A", "1.0 A"],
    'answer': "2.0 A (Amperes)",
    'explanation': "I = 12 / (4 + 2) = 12 / 6 = 2.0 A."
}

# Bridge THPT
HIGH_VIE['bridge']['quiz'][0] = {
    'question': "🎯 Theo công thức uốn dọc Euler (Euler's Buckling Formula), tải trọng nén tới hạn P_cr của một thanh thẳng chịu nén là:",
    'options': ["P_cr = (π² x E x I) / (K x L)²", "P_cr = m x g", "P_cr = F x S", "P_cr = E x ε"],
    'answer': "P_cr = (π² x E x I) / (K x L)²",
    'explanation': "Tải trọng tới hạn Euler: P_cr = π²EI / (KL)², với E là mô-đun Young, I là mô-men quán tính, L là chiều dài."
}
HIGH_ENG['bridge']['quiz'][0] = {
    'question': "🎯 In structural engineering, what equation gives the Euler critical buckling load P_cr of a slender column?",
    'options': ["P_cr = (π² x E x I) / (K x L)²", "P_cr = m x g", "P_cr = F x S", "P_cr = E x ε"],
    'answer': "P_cr = (π² x E x I) / (K x L)²",
    'explanation': "Euler buckling formula: P_cr = π²EI / (KL)², defining elastic instability threshold under compressive axial load."
}

# Biology THPT
HIGH_VIE['biology']['quiz'][0] = {
    'question': "🎯 Trong dự án cáp treo cứu hộ khẩn cấp '{title}', điều kiện cân bằng tĩnh học nút treo cáp được thiết lập theo định luật nào?",
    'options': ["Điều kiện cân bằng tĩnh học: Tổng hợp lực tác dụng lên nút treo bằng 0 (∑F = 0) với lực căng dây T = mg / (2 sin θ)", "Lực căng dây luôn bằng 0", "Không có lực căng", "Dây cáp không chịu lực"],
    'answer': "Điều kiện cân bằng tĩnh học: Tổng hợp lực tác dụng lên nút treo bằng 0 (∑F = 0) với lực căng dây T = mg / (2 sin θ)",
    'explanation': "Chiếu phương trình cân bằng lên trục thẳng đứng: 2T sin θ - mg = 0 => T = mg / (2 sin θ)."
}
HIGH_VIE['biology']['quiz'][1] = {
    'question': "⚛️ Trong sinh thái học bảo tồn, hiện tượng phân mảnh sinh cảnh (Habitat Fragmentation) do đường cao tốc ảnh hưởng thế nào đến quần thể?",
    'options': ["Làm giảm dòng gen (Gene flow) giữa các tiểu quần thể, làm gia tăng giao phối cận huyết và suy giảm biến dị di truyền theo định luật Hardy-Weinberg", "Làm tăng đa dạng di truyền", "Tạo ra loài mới ngay lập tức", "Không ảnh hưởng di truyền"],
    'answer': "Làm giảm dòng gen (Gene flow) giữa các tiểu quần thể, làm gia tăng giao phối cận huyết và suy giảm biến dị di truyền theo định luật Hardy-Weinberg",
    'explanation': "Phân mảnh sinh cảnh cô lập quần thể, phá vỡ thế cân bằng Hardy-Weinberg và làm trôi dạt di truyền (genetic drift) làm mất alen có lợi."
}
HIGH_VIE['biology']['quiz'][2] = {
    'question': "📐 Chú chó Rover và cáng có khối lượng m = 20 kg (P = 200 N). Góc chùng cáp so với phương ngang là θ = 30°. Lực căng dây cáp treo T là bao nhiêu?",
    'options': ["200 N (Newton)", "400 N", "100 N", "50 N"],
    'answer': "200 N (Newton)",
    'explanation': "T = P / (2 sin 30°) = 200 / (2 x 0.5) = 200 N."
}

HIGH_ENG['biology']['quiz'][0] = {
    'question': "🎯 In the rescue rover aerial rigging challenge '{title}', what static equilibrium equation calculates cable tension T?",
    'options': ["Static equilibrium node sum ∑F = 0: Cable tension T = mg / (2 sin θ)", "Cable tension is zero", "No tension", "Cable carries no load"],
    'answer': "Static equilibrium node sum ∑F = 0: Cable tension T = mg / (2 sin θ)",
    'explanation': "Resolving vertical equilibrium at central suspension point: 2T sin θ - mg = 0, giving T = mg / (2 sin θ)."
}
HIGH_ENG['biology']['quiz'][1] = {
    'question': "⚛️ In conservation biology, how does highway habitat fragmentation disrupt demographic genetics according to Hardy-Weinberg principles?",
    'options': ["Restricts gene flow between sub-populations, accelerating inbreeding depression and genetic drift", "Increases genetic diversity", "Generates new species instantly", "Has zero impact"],
    'answer': "Restricts gene flow between sub-populations, accelerating inbreeding depression and genetic drift",
    'explanation': "Barrier effects isolate gene pools, violating Hardy-Weinberg random mating conditions and eroding genetic heterozygosity."
}
HIGH_ENG['biology']['quiz'][2] = {
    'question': "📐 Rover and rescue basket have combined mass m = 20 kg (P = 200 N). At sag angle θ = 30°, what is cable tension T?",
    'options': ["200 N (Newtons)", "400 N", "100 N", "50 N"],
    'answer': "200 N (Newtons)",
    'explanation': "T = 200 / (2 x sin 30°) = 200 / (2 x 0.5) = 200 N."
}

MASTER_PACKS = {
    'kindergarten': {'VIE': KIND_VIE, 'ENG': KIND_ENG},
    'primary': {'VIE': PRIM_VIE, 'ENG': PRIM_ENG},
    'middle': {'VIE': MID_VIE, 'ENG': MID_ENG},
    'high': {'VIE': HIGH_VIE, 'ENG': HIGH_ENG}
}

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

def run():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Normalize entire data tree
    data = normalize_object(data)

    total_lectures = 0
    mismatch_count = 0

    for lvl in data:
        level_name = lvl.get('level', '')
        age_tier = get_age_tier(level_name)
        tier_packs = MASTER_PACKS[age_tier]

        for lg in lvl.get('languages', []):
            lang_code = lg.get('lang', 'VIE')
            lang_pack = tier_packs.get(lang_code, tier_packs['VIE'])

            for topic in lg.get('topics', []):
                topic_name = topic.get('topicName', '')
                for lecture in topic.get('lectures', []):
                    title = lecture.get('title', '')
                    dom_key = detect_domain(title, topic_name)

                    dom_data = lang_pack.get(dom_key)
                    if not dom_data:
                        dom_data = lang_pack.get('bridge', list(lang_pack.values())[0])

                    # 1. Build Quiz Data (strictly matching language)
                    quiz_source = copy.deepcopy(dom_data['quiz'])
                    for q in quiz_source:
                        q['question'] = clean_text(q['question'].replace('{title}', title))
                        q['options'] = [clean_text(opt) for opt in q['options']]
                        q['answer'] = clean_text(q['answer'])
                        q['explanation'] = clean_text(q.get('explanation', '').replace('{title}', title))

                    # 2. Build Practice Data with all redundant fields populated
                    # Flashcards: front, back, term, definition
                    fc_list = []
                    for it in dom_data['flashcards']:
                        front_text = clean_text(it.get('front') or it.get('term') or '')
                        back_text = clean_text(it.get('back') or it.get('definition') or '')
                        fc_list.append({
                            'front': front_text,
                            'back': back_text,
                            'term': front_text,
                            'definition': back_text,
                            'phonetic': clean_text(it.get('phonetic', '')),
                            'example': clean_text(it.get('example', ''))
                        })

                    # Matching: left, right, term, definition
                    matching_list = []
                    for it in dom_data['matching']:
                        left_text = clean_text(it.get('left') or it.get('term') or '')
                        right_text = clean_text(it.get('right') or it.get('definition') or '')
                        matching_list.append({
                            'left': left_text,
                            'right': right_text,
                            'term': left_text,
                            'definition': right_text
                        })

                    # Sequencing: [{ stepNumber, text }] and ["1. ..."]
                    seq_list = []
                    for idx, step in enumerate(dom_data['sequencing']):
                        if isinstance(step, dict):
                            s_num = step.get('stepNumber', idx + 1)
                            s_text = clean_text(step.get('text', ''))
                        else:
                            s_text = clean_text(str(step))
                            s_num = idx + 1
                        seq_list.append({
                            'stepNumber': s_num,
                            'text': s_text
                        })

                    # Cloze: [{ sentence, answer, options, explanation }]
                    cloze_list = []
                    for it in dom_data['cloze']:
                        sent = clean_text(it.get('sentence', ''))
                        ans = clean_text(it.get('answer', ''))
                        opts = [clean_text(o) for o in it.get('options', [ans, 'tiêu chí', 'mẫu thử', 'giới hạn'] if lang_code == 'VIE' else [ans, 'criteria', 'prototype', 'constraint'])]
                        if ans not in opts:
                            opts[0] = ans
                        cloze_list.append({
                            'sentence': sent,
                            'answer': ans,
                            'options': opts,
                            'explanation': clean_text(it.get('explanation', f'Thuật ngữ chính xác là: {ans}' if lang_code == 'VIE' else f'The correct term is: {ans}'))
                        })

                    lecture['quizData'] = quiz_source
                    lecture['practiceData'] = {
                        'flashcards': fc_list,
                        'matching': matching_list,
                        'matchingPairs': matching_list,
                        'sequencing': seq_list,
                        'cloze': cloze_list
                    }

                    total_lectures += 1

    print(f"Total processed: {total_lectures} lectures.")

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Saved updated data.json")

    with open('data.js', 'w', encoding='utf-8') as f:
        f.write("// STEM LMS Global Curriculum Dataset (Perfect Multilingual & Calibrated)\n")
        f.write("window.APP_DATA = ")
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print("Saved updated data.js")

if __name__ == '__main__':
    run()
