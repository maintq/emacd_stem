import os
import json
import base64
import streamlit as st

# ==============================================================================
# Page Configuration
# ==============================================================================
st.set_page_config(
    page_title="STEM EdTech LMS - Nền tảng Học tập & Chế tạo STEM",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# Custom CSS Styling
# ==============================================================================
st.markdown("""
<style>
    /* Main branding & typography */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    .stApp {
        background-color: #f8fafc;
    }
    
    /* Header card */
    .hero-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
        color: white;
        padding: 1.5rem 2rem;
        border-radius: 16px;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.2);
    }
    .hero-title {
        font-size: 1.75rem;
        font-weight: 800;
        margin: 0;
        color: #ffffff;
    }
    .hero-subtitle {
        font-size: 0.95rem;
        opacity: 0.9;
        margin-top: 0.35rem;
        color: #e0f2fe;
    }
    
    /* Meta Pills */
    .meta-pills-row {
        display: flex;
        flex-wrap: wrap;
        gap: 0.6rem;
        margin: 0.8rem 0;
    }
    .meta-pill {
        display: inline-block;
        padding: 0.35rem 0.85rem;
        border-radius: 9999px;
        font-size: 0.8rem;
        font-weight: 700;
    }
    .pill-blue { background-color: #dbeafe; color: #1e40af; }
    .pill-amber { background-color: #fef3c7; color: #92400e; }
    .pill-green { background-color: #d1fae5; color: #065f46; }
    .pill-purple { background-color: #ede9fe; color: #5b21b6; }
    
    /* PDF Callout Box */
    .pdf-container-card {
        background-color: #ffffff;
        border: 1.5px dashed #3b82f6;
        border-radius: 12px;
        padding: 1rem 1.25rem;
        margin: 1rem 0;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    
    /* Flashcard presentation */
    .flashcard-box {
        background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 100%);
        border: 2px solid #cbd5e1;
        border-radius: 16px;
        padding: 2.5rem 1.5rem;
        text-align: center;
        min-height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        margin: 1rem 0;
    }
    .flashcard-term {
        font-size: 1.6rem;
        font-weight: 800;
        color: #1e3a8a;
    }
    .flashcard-def {
        font-size: 1.15rem;
        color: #334155;
        font-weight: 500;
        line-height: 1.6;
        margin-top: 0.75rem;
    }
    
    /* EDP Principle Card */
    .principle-box {
        background: #ffffff;
        border-left: 4px solid #2563eb;
        border-radius: 8px;
        padding: 1rem 1.25rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# Data Loader
# ==============================================================================
@st.cache_data
def load_curriculum():
    data_path = os.path.join(os.path.dirname(__file__), "data.json")
    if not os.path.exists(data_path):
        st.error(f"Không tìm thấy file dữ liệu {data_path}!")
        return []
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)

curriculum = load_curriculum()

if not curriculum:
    st.warning("Hệ thống chưa có dữ liệu bài học. Vui lòng kiểm tra lại file data.json.")
    st.stop()

# ==============================================================================
# Sidebar Navigation & Filter Hierarchy
# ==============================================================================
with st.sidebar:
    st.markdown("### 🎓 **STEM EdTech LMS**")
    st.caption("Hệ thống Bài giảng • Thực hành • Kiểm tra")
    st.divider()

    # 1. Level Filter
    level_names = [f"{lvl.get('icon', '📚')} {lvl.get('levelFullName', lvl.get('level'))}" for lvl in curriculum]
    selected_lvl_idx = st.selectbox("1. Cấp học (Education Level):", range(len(level_names)), format_func=lambda i: level_names[i])
    current_level = curriculum[selected_lvl_idx]

    # 2. Language Filter
    available_languages = current_level.get("languages", [])
    lang_labels = ["Tiếng Việt (VIE)" if lg.get("lang") == "VIE" else "English (ENG)" for lg in available_languages]
    selected_lang_idx = st.radio("2. Ngôn ngữ (Language):", range(len(available_languages)), format_func=lambda i: lang_labels[i], horizontal=True)
    current_lang_obj = available_languages[selected_lang_idx]
    current_lang = current_lang_obj.get("lang", "VIE")
    is_eng = (current_lang == "ENG")

    # 3. Topic Filter
    topics = current_lang_obj.get("topics", [])
    topic_titles = [f"{t.get('icon', '📂')} {t.get('topic', 'Chủ đề')}" for t in topics]
    selected_topic_idx = st.selectbox("3. Chủ đề (Topic):", range(len(topic_titles)), format_func=lambda i: topic_titles[i])
    current_topic = topics[selected_topic_idx]

    # 4. Lecture Filter
    lectures = current_topic.get("lectures", [])
    lec_titles = [f"{idx+1}. {lec.get('title', 'Bài học')}" for idx, lec in enumerate(lectures)]
    selected_lec_idx = st.selectbox("4. Bài học (Lecture):", range(len(lec_titles)), format_func=lambda i: lec_titles[i])
    current_lecture = lectures[selected_lec_idx]

    st.divider()
    # Sidebar stats
    total_lectures = sum(
        len(top.get("lectures", []))
        for lvl in curriculum
        for lg in lvl.get("languages", [])
        for top in lg.get("topics", [])
    )
    st.info(f"📊 **Tổng số bài giảng hệ thống:** {total_lectures} bài\n\n📌 **Cấp học:** {current_level.get('ageGroup', '')}")

# ==============================================================================
# Helper: PDF Document Handling
# ==============================================================================
def get_pdf_bytes_and_filename(lec):
    content_url = lec.get("contentUrl", "")
    file_name = lec.get("fileName") or (os.path.basename(content_url) if content_url else "bai-giang.pdf")
    
    clean_path = content_url.lstrip("./") if content_url.startswith("./") else content_url
    full_path = os.path.join(os.path.dirname(__file__), clean_path)
    
    if os.path.exists(full_path):
        try:
            with open(full_path, "rb") as f:
                return f.read(), file_name, full_path
        except Exception:
            return None, file_name, full_path
    return None, file_name, full_path

# ==============================================================================
# Main Content Area
# ==============================================================================
lp = current_lecture.get("lessonPlan", {})
overview = lp.get("overview", {})
title = current_lecture.get("title", "Bài học STEM")
discipline = overview.get("discipline", "Khoa học STEM")
age_group = overview.get("ageGroup", current_level.get("ageGroup", "8 - 18 tuổi"))
duration = overview.get("duration", "90 phút")
summary = overview.get("summary") or current_lecture.get("theoryNotes", "")

# Header Block
st.markdown(f"""
<div class="hero-header">
    <h1 class="hero-title">🔬 {title}</h1>
    <div class="hero-subtitle">{current_level.get('levelFullName', '')} • {current_topic.get('topic', '')}</div>
    <div class="meta-pills-row">
        <span class="meta-pill pill-blue">📚 {discipline}</span>
        <span class="meta-pill pill-amber">👶 {age_group}</span>
        <span class="meta-pill pill-green">⏱️ {duration}</span>
        <span class="meta-pill pill-purple">⚙️ Quy trình Kỹ thuật EDP</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Overview summary text
st.markdown(f"**📖 {'Overview' if is_eng else 'Tổng quan bài giảng'}:** {summary}")

# PDF Attachment Row
pdf_data, pdf_filename, pdf_full_path = get_pdf_bytes_and_filename(current_lecture)
col_pdf_info, col_pdf_btn = st.columns([3, 1])

with col_pdf_info:
    st.markdown(f"""
    📄 **{'Original Lesson Plan PDF File' if is_eng else 'Tài liệu Kế hoạch Bài giảng (File PDF Gốc)'}:**  
    `{pdf_filename}`
    """)

with col_pdf_btn:
    if pdf_data:
        st.download_button(
            label=f"⬇️ {'Download PDF' if is_eng else 'Tải file PDF'}",
            data=pdf_data,
            file_name=pdf_filename,
            mime="application/pdf",
            use_container_width=True
        )
    else:
        st.button(f"⚠️ {'PDF not found' if is_eng else 'Chưa có file PDF'}", disabled=True, use_container_width=True)

st.write("")

# ==============================================================================
# Tabs Structure: 1. Lesson Plan | 2. Practice | 3. Test
# ==============================================================================
tab_labels = [
    "📖 Kế hoạch Bài học" if not is_eng else "📖 Lesson Plan",
    "🛠️ Thực hành Đa dạng" if not is_eng else "🛠️ Interactive Practice",
    "✍️ Kiểm tra Đánh giá" if not is_eng else "✍️ Assessments & Quiz"
]
tab_learn, tab_practice, tab_quiz = st.tabs(tab_labels)

# ==============================================================================
# TAB 1: LESSON PLAN
# ==============================================================================
with tab_learn:
    col_obj, col_mat = st.columns([1, 1])
    
    with col_obj:
        st.subheader("🎯 " + ("Mục tiêu bài học" if not is_eng else "Learning Objectives"))
        objectives = lp.get("objectives", [
            "Nắm vững các nguyên lý khoa học và kỹ thuật nền tảng.",
            "Áp dụng quy trình thiết kế kỹ thuật EDP để chế tạo mô hình.",
            "Đo lường, kiểm tra và tối ưu hóa giải pháp thực tế."
        ])
        for obj in objectives:
            st.markdown(f"- {obj}")

    with col_mat:
        st.subheader("📦 " + ("Tủ Vật liệu & Dụng cụ" if not is_eng else "Materials & Tools Checklist"))
        materials = lp.get("materials", {})
        req_mat = materials.get("required", [])
        opt_mat = materials.get("optional", [])
        tools_mat = materials.get("tools", [])
        
        lec_id = current_lecture.get("lectureId", "L0")
        mat_key_prefix = f"mat_{selected_lvl_idx}_{selected_lang_idx}_{selected_topic_idx}_{selected_lec_idx}"
        
        checked_count = 0
        total_mat = len(req_mat) + len(opt_mat) + len(tools_mat)
        
        st.markdown(f"**{'Vật liệu bắt buộc' if not is_eng else 'Required Materials'}:**")
        for i, m in enumerate(req_mat):
            if st.checkbox(m, key=f"{mat_key_prefix}_req_{i}"):
                checked_count += 1
                
        if opt_mat:
            st.markdown(f"**{'Vật liệu tái chế / Thay thế' if not is_eng else 'Recycled / Optional Materials'}:**")
            for i, m in enumerate(opt_mat):
                if st.checkbox(m, key=f"{mat_key_prefix}_opt_{i}"):
                    checked_count += 1
                    
        if tools_mat:
            st.markdown(f"**{'Dụng cụ chế tạo' if not is_eng else 'Tools & Equipment'}:**")
            for i, m in enumerate(tools_mat):
                if st.checkbox(m, key=f"{mat_key_prefix}_tool_{i}"):
                    checked_count += 1
                    
        if total_mat > 0:
            st.progress(checked_count / total_mat, text=f"Đã chuẩn bị: {checked_count}/{total_mat} món đồ")

    st.divider()

    # Engineering Challenge EDP
    challenge = lp.get("challenge", {})
    st.subheader("🏆 " + ("Thử thách Kỹ thuật EDP" if not is_eng else "Engineering Design Challenge"))
    st.info(f"**{'Tình huống bài toán' if not is_eng else 'Mission Scenario'}:** {challenge.get('scenario', 'Chế tạo giải pháp kỹ thuật theo yêu cầu.')}")
    
    col_crit, col_cons = st.columns(2)
    with col_crit:
        st.markdown(f"**✅ {'Tiêu chí thành công' if not is_eng else 'Success Criteria'}:**")
        for c in challenge.get("criteria", ["Mô hình hoạt động ổn định"]):
            st.markdown(f"- {c}")
    with col_cons:
        st.markdown(f"**⚠️ {'Ràng buộc kỹ thuật' if not is_eng else 'Design Constraints'}:**")
        for c in challenge.get("constraints", ["Tuân thủ thời gian và vật liệu an toàn"]):
            st.markdown(f"- {c}")

    st.divider()

    # Scientific Principles
    st.subheader("🔬 " + ("Nguyên lý Khoa học Cốt lõi" if not is_eng else "Core Scientific Principles"))
    principles = lp.get("scientificPrinciples", [])
    if principles:
        for p in principles:
            st.markdown(f"""
            <div class="principle-box">
                <h4 style="color:#1e40af; margin-bottom:0.25rem;">🔍 {p.get('title', 'Nguyên lý')}</h4>
                <p style="margin:0.25rem 0; color:#334155;">{p.get('explanation', '')}</p>
                {f"<p style='color:#b45309; font-weight:600; margin:0.2rem 0;'>📐 Công thức: {p.get('formula')}</p>" if p.get('formula') else ""}
                {f"<p style='color:#065f46; font-size:0.9rem; margin:0.2rem 0;'>🌍 Ứng dụng: {p.get('realWorldApp')}</p>" if p.get('realWorldApp') else ""}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.write(current_lecture.get("theoryNotes", "Tìm hiểu nguyên lý khoa học áp dụng."))

    st.divider()

    # Engineering Steps
    st.subheader("⚙️ " + ("Quy trình Thiết kế & Chế tạo (EDP)" if not is_eng else "Engineering Design Process Steps"))
    steps = lp.get("engineeringSteps", [])
    for idx, s in enumerate(steps):
        phase_num = s.get("phase", idx + 1)
        phase_title = s.get("title", f"Bước {phase_num}")
        with st.expander(f"Bước {phase_num}: {phase_title}", expanded=(idx == 0)):
            st.markdown(f"**{'Hướng dẫn thực hiện' if not is_eng else 'Instructions'}:** {s.get('instructions', '')}")
            if s.get("checkpoint"):
                st.success(f"🎯 **{'Điểm kiểm tra kỹ thuật' if not is_eng else 'Quality Checkpoint'}:** {s.get('checkpoint')}")
            if s.get("teacherTips"):
                st.info(f"💡 **{'Gợi ý cho giáo viên' if not is_eng else 'Educator Tip'}:** {s.get('teacherTips')}")

    st.divider()

    # Interactive Lab Calculator
    lab_calc = lp.get("labCalculator", {})
    if lab_calc and lab_calc.get("title"):
        st.subheader("🧮 " + ("Phòng Thí nghiệm Tính toán Kỹ thuật" if not is_eng else "Engineering Lab Calculator"))
        st.caption(lab_calc.get("formulaDescription", "Tính toán thông số kỹ thuật thực nghiệm."))
        
        in1_meta = lab_calc.get("input1", {})
        in2_meta = lab_calc.get("input2", {})
        
        col_c1, col_c2, col_c3 = st.columns([1, 1, 1])
        with col_c1:
            val1 = st.number_input(
                f"{in1_meta.get('label', 'Thông số 1')} ({in1_meta.get('unit', '')})",
                value=float(in1_meta.get("default", 10.0)),
                step=1.0,
                key=f"calc_{mat_key_prefix}_in1"
            )
        with col_c2:
            val2 = st.number_input(
                f"{in2_meta.get('label', 'Thông số 2')} ({in2_meta.get('unit', '')})",
                value=float(in2_meta.get("default", 5.0)),
                step=1.0,
                key=f"calc_{mat_key_prefix}_in2"
            )
        with col_c3:
            st.write("")
            st.write("")
            compute_type = lab_calc.get("compute", "multiply")
            if compute_type == "product" or compute_type == "multiply":
                calc_result = val1 * val2
            elif compute_type == "ratio" or compute_type == "divide":
                calc_result = (val1 / val2) if val2 != 0 else 0
            elif compute_type == "add":
                calc_result = val1 + val2
            elif compute_type == "difference":
                calc_result = abs(val1 - val2)
            else:
                calc_result = val1 * val2
                
            st.metric(
                label=("Kết quả tính toán" if not is_eng else "Computed Result"),
                value=f"{calc_result:.2f} {lab_calc.get('formulaDescription', '').split('=')[-1].strip()}"
            )

    st.divider()

    # Discussion Questions
    discussions = lp.get("discussionQuestions", [])
    if discussions:
        st.subheader("💬 " + ("Câu hỏi Đào sâu & Thảo luận" if not is_eng else "Deep Dive & Discussion Questions"))
        for idx, q_item in enumerate(discussions):
            q_text = q_item.get("question", "")
            ans_text = q_item.get("guidingAnswer", "")
            with st.expander(f"❓ Câu hỏi {idx+1}: {q_text}"):
                st.markdown(f"💡 **{'Hướng dẫn trả lời' if not is_eng else 'Guiding Answer'}:** {ans_text}")

# ==============================================================================
# TAB 2: INTERACTIVE PRACTICE
# ==============================================================================
with tab_practice:
    practice = current_lecture.get("practiceData", {})
    practice_modes = [
        "📇 Flashcards 3D" if not is_eng else "📇 3D Flashcards",
        "🧩 Nối từ kỹ thuật" if not is_eng else "🧩 Matching Game",
        "🔢 Sắp xếp quy trình" if not is_eng else "🔢 Step Sequencing",
        "✍️ Điền từ khuyết" if not is_eng else "✍️ Cloze Fill-in"
    ]
    p_mode = st.radio("Chọn hình thức thực hành:", practice_modes, horizontal=True)

    # 1. Flashcards Mode
    if "Flashcard" in p_mode:
        fc_list = practice.get("flashcards", [])
        if fc_list:
            fc_key = f"fc_idx_{selected_lvl_idx}_{selected_lang_idx}_{selected_topic_idx}_{selected_lec_idx}"
            if fc_key not in st.session_state:
                st.session_state[fc_key] = 0
            flip_key = f"fc_flip_{selected_lvl_idx}_{selected_lang_idx}_{selected_topic_idx}_{selected_lec_idx}"
            if flip_key not in st.session_state:
                st.session_state[flip_key] = False

            cur_idx = st.session_state[fc_key]
            card = fc_list[cur_idx]
            front_text = card.get("term") or card.get("front", "Thuật ngữ")
            back_text = card.get("definition") or card.get("back", "Định nghĩa")
            phonetic = card.get("phonetic", "")
            example = card.get("example", "")

            # Display Flashcard
            is_flipped = st.session_state[flip_key]
            if not is_flipped:
                card_html = f"""
                <div class="flashcard-box">
                    <span style="font-size:0.85rem; font-weight:700; color:#3b82f6; text-transform:uppercase;">Thẻ mặt trước (Thuật ngữ)</span>
                    <div class="flashcard-term">{front_text}</div>
                    {f"<div style='color:#64748b; font-style:italic;'>{phonetic}</div>" if phonetic else ""}
                    <div style="font-size:0.85rem; color:#94a3b8; margin-top:1rem;">(Bấm 'Lật mặt thẻ' bên dưới để xem định nghĩa)</div>
                </div>
                """
            else:
                card_html = f"""
                <div class="flashcard-box" style="background: linear-gradient(135deg, #eff6ff 0%, #ffffff 100%); border-color:#3b82f6;">
                    <span style="font-size:0.85rem; font-weight:700; color:#16a34a; text-transform:uppercase;">Thẻ mặt sau (Định nghĩa)</span>
                    <div class="flashcard-term" style="font-size:1.25rem; color:#1e40af;">{front_text}</div>
                    <div class="flashcard-def">{back_text}</div>
                    {f"<div style='font-size:0.9rem; color:#475569; margin-top:0.75rem; font-style:italic;'>Ví dụ: {example}</div>" if example else ""}
                </div>
                """
            st.markdown(card_html, unsafe_allow_html=True)

            col_prev, col_flip, col_next = st.columns([1, 2, 1])
            with col_prev:
                if st.button("◀️ " + ("Trước" if not is_eng else "Prev"), use_container_width=True):
                    if st.session_state[fc_key] > 0:
                        st.session_state[fc_key] -= 1
                        st.session_state[flip_key] = False
                        st.rerun()
            with col_flip:
                if st.button("🔄 " + ("Lật mặt thẻ" if not is_eng else "Flip Card"), use_container_width=True):
                    st.session_state[flip_key] = not st.session_state[flip_key]
                    st.rerun()
            with col_next:
                if st.button(("Tiếp" if not is_eng else "Next") + " ▶️", use_container_width=True):
                    if st.session_state[fc_key] < len(fc_list) - 1:
                        st.session_state[fc_key] += 1
                        st.session_state[flip_key] = False
                        st.rerun()

            st.caption(f"Thẻ số: {cur_idx + 1} / {len(fc_list)}")
        else:
            st.info("Chưa có flashcard cho bài học này.")

    # 2. Matching Mode
    elif "Nối từ" in p_mode or "Matching" in p_mode:
        mp_list = practice.get("matchingPairs") or practice.get("matching", [])
        if mp_list:
            st.markdown(f"**{'Nhiệm vụ' if not is_eng else 'Task'}:** Ghép cặp thuật ngữ ở cột trái với định nghĩa tương ứng ở cột phải.")
            
            terms = [m.get("term") or m.get("left", "") for m in mp_list]
            defs = [m.get("definition") or m.get("right", "") for m in mp_list]
            
            user_matches = {}
            for idx, term in enumerate(terms):
                st.write(f"**{idx+1}. {term}**")
                choice = st.selectbox(
                    f"Chọn định nghĩa cho '{term}':",
                    ["-- Chọn định nghĩa phù hợp --"] + defs,
                    key=f"match_{selected_lvl_idx}_{selected_lec_idx}_{idx}"
                )
                user_matches[term] = choice
                
            if st.button("🔍 " + ("Kiểm tra kết quả nối từ" if not is_eng else "Check Matches"), type="primary"):
                correct_count = 0
                for idx, m in enumerate(mp_list):
                    t = m.get("term") or m.get("left", "")
                    d = m.get("definition") or m.get("right", "")
                    user_val = user_matches.get(t)
                    if user_val == d:
                        correct_count += 1
                        st.success(f"✅ Đúng: **{t}** ➔ {d}")
                    else:
                        st.error(f"❌ Chưa đúng với **{t}**. Đáp án đúng là: *{d}*")
                st.metric("Tổng điểm ghép cặp:", f"{correct_count} / {len(mp_list)}")
        else:
            st.info("Chưa có dữ liệu nối từ cho bài học này.")

    # 3. Sequencing Mode
    elif "Sắp xếp" in p_mode or "Sequencing" in p_mode:
        seq_list = practice.get("sequencing", [])
        if seq_list:
            st.markdown(f"**{'Nhiệm vụ' if not is_eng else 'Task'}:** Đọc kỹ và ghi nhớ thứ tự đúng của quy trình kỹ thuật:")
            for idx, item in enumerate(seq_list):
                txt = item.get("text") if isinstance(item, dict) else str(item)
                st.markdown(f"""
                <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:8px; padding:0.75rem 1rem; margin-bottom:0.5rem;">
                    <strong>Bước {idx+1}:</strong> {txt}
                </div>
                """, unsafe_allow_html=True)
            st.success("💡 Hãy thực hành quy trình trên khi chế tạo mô hình thực tế!")
        else:
            st.info("Chưa có quy trình sắp xếp cho bài học này.")

    # 4. Cloze Mode
    elif "Điền từ" in p_mode or "Cloze" in p_mode:
        cloze_list = practice.get("cloze", [])
        if cloze_list:
            st.markdown(f"**{'Nhiệm vụ' if not is_eng else 'Task'}:** Chọn từ thích hợp điền vào chỗ trống:")
            cloze_user_answers = {}
            for idx, item in enumerate(cloze_list):
                sentence = item.get("sentence", "")
                opts = item.get("options", [])
                ans = item.get("answer", "")
                st.markdown(f"**Câu {idx+1}:** {sentence}")
                choice = st.selectbox(
                    f"Từ cần điền (Câu {idx+1}):",
                    ["-- Chọn từ --"] + opts,
                    key=f"cloze_{selected_lvl_idx}_{selected_lec_idx}_{idx}"
                )
                cloze_user_answers[idx] = (choice, ans, item.get("explanation", ""))

            if st.button("📝 " + ("Kiểm tra điền từ" if not is_eng else "Check Answers"), type="primary"):
                score = 0
                for idx, (choice, ans, expl) in cloze_user_answers.items():
                    if choice.strip().lower() == ans.strip().lower():
                        score += 1
                        st.success(f"✅ Câu {idx+1}: Đúng! ({choice})")
                    else:
                        st.error(f"❌ Câu {idx+1}: Chưa đúng. Đáp án đúng: **{ans}**. {expl}")
                st.metric("Điểm điền từ:", f"{score} / {len(cloze_list)}")
        else:
            st.info("Chưa có bài tập điền từ cho bài học này.")

# ==============================================================================
# TAB 3: ASSESSMENTS & QUIZ
# ==============================================================================
with tab_quiz:
    quiz_data = current_lecture.get("quizData", [])
    if quiz_data:
        st.subheader("🎯 " + ("Bài Kiểm tra Đánh giá Năng lực STEM" if not is_eng else "STEM Assessment Quiz"))
        st.write(f"{'Hãy chọn phương án đúng nhất cho mỗi câu hỏi bên dưới:' if not is_eng else 'Select the best answer for each question:'}")

        quiz_form_key = f"quiz_form_{selected_lvl_idx}_{selected_lang_idx}_{selected_topic_idx}_{selected_lec_idx}"
        
        user_quiz_answers = {}
        for idx, q_item in enumerate(quiz_data):
            st.markdown(f"**Câu hỏi {idx+1}:** {q_item.get('question', '')}")
            opts = q_item.get("options", [])
            selected_opt = st.radio(
                f"Lựa chọn cho câu {idx+1}:",
                opts,
                index=None,
                key=f"q_{selected_lvl_idx}_{selected_lec_idx}_{idx}",
                label_visibility="collapsed"
            )
            user_quiz_answers[idx] = selected_opt
            st.write("")

        if st.button("🚀 " + ("Nộp bài kiểm tra" if not is_eng else "Submit Quiz"), type="primary", use_container_width=True):
            unanswered = [idx+1 for idx, opt in user_quiz_answers.items() if opt is None]
            if unanswered:
                st.warning(f"⚠️ Bạn chưa trả lời các câu hỏi số: {', '.join(map(str, unanswered))}. Hãy hoàn thành tất cả các câu trước khi nộp bài nhé!")
            else:
                correct_count = 0
                st.divider()
                st.subheader("📊 " + ("Kết quả bài làm chi tiết" if not is_eng else "Detailed Quiz Results"))
                
                for idx, q_item in enumerate(quiz_data):
                    user_ans = user_quiz_answers.get(idx)
                    correct_ans = q_item.get("answer", "")
                    expl = q_item.get("explanation", "")
                    
                    if user_ans == correct_ans:
                        correct_count += 1
                        st.success(f"**Câu {idx+1}: Chính xác!**\n\n- Câu trả lời của bạn: *{user_ans}*\n- 💡 **Giải thích:** {expl}")
                    else:
                        st.error(f"**Câu {idx+1}: Chưa chính xác!**\n\n- Câu trả lời của bạn: *{user_ans}*\n- ✅ **Đáp án đúng:** *{correct_ans}*\n- 💡 **Giải thích:** {expl}")
                        
                total_q = len(quiz_data)
                percentage = int((correct_count / total_q) * 100)
                st.metric("🏆 Tổng điểm của bạn:", f"{correct_count}/{total_q} ({percentage}%)")
                
                if percentage >= 80:
                    st.balloons()
                    st.success("🎉 Xuất sắc! Bạn đã nắm rất vững kiến thức và kỹ năng kỹ thuật của bài học này!")
                elif percentage >= 50:
                    st.info("👍 Khá tốt! Hãy đọc lại các phần giải thích chi tiết để hoàn thiện hơn nhé.")
                else:
                    st.warning("💪 Hãy ôn tập lại kế hoạch bài giảng và thử thách lại bài kiểm tra nhé!")
    else:
        st.info("Chưa có bộ câu hỏi kiểm tra cho bài học này.")
