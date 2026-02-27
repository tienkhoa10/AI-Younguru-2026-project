import streamlit as st
import time

st.set_page_config(page_title="PathAI 10", layout="centered")

st.title("🚀 PathAI Toán 10")
st.subheader("Đánh giá năng lực theo chuẩn chương trình Toán 10")

name = st.text_input("Nhập tên của bạn:", key="name_input")

st.markdown("## 📝 Bài test 30 câu")

# =========================
# TẠO NGÂN HÀNG CÂU HỎI
# =========================

questions = [

# ===== NHẬN BIẾT (10 câu) =====
{"question":"NB1 (Mệnh đề): Phủ định của '∀x ∈ R, x² ≥ 0' là:",
 "options":["∃x ∈ R sao cho x² < 0","∀x ∈ R, x² < 0","∃x ∈ R sao cho x² ≥ 0","Không có"],
 "answer":"∃x ∈ R sao cho x² < 0",
 "topic":"Mệnh đề","level":"Nhận biết"},

{"question":"NB2 (Hàm số): Hệ số góc của y = 3x + 2 là:",
 "options":["2","3","-3","1"],
 "answer":"3","topic":"Hàm số","level":"Nhận biết"},

{"question":"NB3 (Phương trình): 2x = 8 ⇒ x = ?",
 "options":["2","4","6","8"],
 "answer":"4","topic":"Phương trình","level":"Nhận biết"},

{"question":"NB4 (BPT): Nghiệm của x > 1 là:",
 "options":["(1,∞)","(-∞,1)","[1,∞)","(-∞,1]"],
 "answer":"(1,∞)","topic":"Bất phương trình","level":"Nhận biết"},

{"question":"NB5 (Vectơ): |a| = 5 nghĩa là:",
 "options":["Độ dài vectơ a","Tọa độ a","Góc của a","Không xác định"],
 "answer":"Độ dài vectơ a","topic":"Vectơ","level":"Nhận biết"},

{"question":"NB6 (Hình học): Tổng ba góc tam giác là:",
 "options":["180°","360°","90°","270°"],
 "answer":"180°","topic":"Hình học","level":"Nhận biết"},

{"question":"NB7 (Thống kê): Trung bình của 1,2,3 là:",
 "options":["1","2","3","4"],
 "answer":"2","topic":"Thống kê","level":"Nhận biết"},

{"question":"NB8 (Hàm số): Đỉnh y=x² là:",
 "options":["(0,0)","(1,0)","(0,1)","(-1,0)"],
 "answer":"(0,0)","topic":"Hàm số","level":"Nhận biết"},

{"question":"NB9 (PT): x²=4 có bao nhiêu nghiệm?",
 "options":["1","2","0","3"],
 "answer":"2","topic":"Phương trình","level":"Nhận biết"},

{"question":"NB10 (BPT): x² ≥ 0 đúng với:",
 "options":["Mọi x","Không x nào","x>0","x<0"],
 "answer":"Mọi x","topic":"Bất phương trình","level":"Nhận biết"},


# ===== THÔNG HIỂU (10 câu) =====
{"question":"TH1: Đỉnh của y=x²-4x+3 là:",
 "options":["(2,-1)","(1,2)","(0,3)","(4,1)"],
 "answer":"(2,-1)","topic":"Hàm số","level":"Thông hiểu"},

{"question":"TH2: Giải 3x-6=0",
 "options":["1","2","3","-2"],
 "answer":"2","topic":"Phương trình","level":"Thông hiểu"},

{"question":"TH3: Tập nghiệm x²<9",
 "options":["(-3,3)","(-∞,-3)∪(3,∞)","(-3,∞)","(-∞,3)"],
 "answer":"(-3,3)","topic":"Bất phương trình","level":"Thông hiểu"},

{"question":"TH4: |a|=3, |b|=4, a ⟂ b ⇒ |a+b|=?",
 "options":["5","7","1","12"],
 "answer":"5","topic":"Vectơ","level":"Thông hiểu"},

{"question":"TH5: Hàm y=2x+1 đồng biến khi:",
 "options":["Mọi x","x>0","x<0","Không"],
 "answer":"Mọi x","topic":"Hàm số","level":"Thông hiểu"},

{"question":"TH6: Tam giác vuông có 1 góc bằng:",
 "options":["90°","60°","45°","30°"],
 "answer":"90°","topic":"Hình học","level":"Thông hiểu"},

{"question":"TH7: Phương sai dùng để đo:",
 "options":["Mức độ phân tán","Giá trị nhỏ nhất","Trung bình","Tần số"],
 "answer":"Mức độ phân tán","topic":"Thống kê","level":"Thông hiểu"},

{"question":"TH8: Giải x²-1=0",
 "options":["±1","1","-1","0"],
 "answer":"±1","topic":"Phương trình","level":"Thông hiểu"},

{"question":"TH9: Hàm bậc hai có dạng:",
 "options":["ax²+bx+c","ax+b","a/x","log x"],
 "answer":"ax²+bx+c","topic":"Hàm số","level":"Thông hiểu"},

{"question":"TH10: Nếu a=b thì vectơ a-b:",
 "options":["=0","≠0","=1","Không xác định"],
 "answer":"=0","topic":"Vectơ","level":"Thông hiểu"},


# ===== VẬN DỤNG (10 câu) =====
{"question":"VD1: Giải hệ x+y=5; x-y=1",
 "options":["(3,2)","(2,3)","(4,1)","(1,4)"],
 "answer":"(3,2)","topic":"Hệ phương trình","level":"Vận dụng"},

{"question":"VD2: Giá trị nhỏ nhất y=x² là:",
 "options":["0","1","-1","Không có"],
 "answer":"0","topic":"Hàm số","level":"Vận dụng"},

{"question":"VD3: Diện tích tam giác vuông cạnh 3 và 4:",
 "options":["6","12","7","5"],
 "answer":"6","topic":"Hình học","level":"Vận dụng"},

{"question":"VD4: Nếu trung bình là 5 của 3 số tổng bằng:",
 "options":["15","5","10","20"],
 "answer":"15","topic":"Thống kê","level":"Vận dụng"},

{"question":"VD5: Giải x²-5x+6=0",
 "options":["2 và 3","1 và 6","-2 và -3","0"],
 "answer":"2 và 3","topic":"Phương trình","level":"Vận dụng"},

{"question":"VD6: Vectơ (1,2)+(2,3)=",
 "options":["(3,5)","(1,5)","(3,2)","(2,2)"],
 "answer":"(3,5)","topic":"Vectơ","level":"Vận dụng"},

{"question":"VD7: Nghiệm của |x|=3",
 "options":["±3","3","-3","0"],
 "answer":"±3","topic":"Phương trình","level":"Vận dụng"},

{"question":"VD8: Tập nghiệm x²-4≥0",
 "options":["(-∞,-2]∪[2,∞)","(-2,2)","(-∞,2)","(2,∞)"],
 "answer":"(-∞,-2]∪[2,∞)","topic":"Bất phương trình","level":"Vận dụng"},

{"question":"VD9: Hàm y=-x² có dạng:",
 "options":["Nghịch biến trên R","Đồng biến","Hằng số","Không xác định"],
 "answer":"Nghịch biến trên R","topic":"Hàm số","level":"Vận dụng"},

{"question":"VD10: Xác suất tung đồng xu ra mặt sấp:",
 "options":["1/2","1","0","1/4"],
 "answer":"1/2","topic":"Thống kê","level":"Vận dụng"},
]

# =========================
# CHẤM ĐIỂM
# =========================

score = 0
level_score = {"Nhận biết":0,"Thông hiểu":0,"Vận dụng":0}

for i,q in enumerate(questions):
    ans = st.radio(q["question"], q["options"], key=f"q{i}")
    if ans == q["answer"]:
        score += 1
        level_score[q["level"]] += 1

# =========================
# PHÂN TÍCH AI NÂNG CAO
# =========================

if st.button("Phân tích AI & Tạo lộ trình học"):

    with st.spinner("AI đang phân tích chuyên sâu..."):
        time.sleep(2)

    percent = int(score/30*100)

    st.success(f"{name}, bạn đạt {score}/30 câu ({percent}%)")

    # =========================
    # PHÂN TÍCH THEO TƯ DUY
    # =========================
    st.markdown("## 📊 Phân tích theo tư duy")

    for lv in level_score:
        st.write(f"{lv}: {level_score[lv]}/10")

    # =========================
    # PHÂN TÍCH THEO CHỦ ĐỀ
    # =========================
    topic_score = {}
    for q in questions:
        topic_score[q["topic"]] = 0

    for i, q in enumerate(questions):
        if st.session_state.get(f"q{i}") == q["answer"]:
            topic_score[q["topic"]] += 1

    st.markdown("## 📚 Phân tích theo chuyên đề")

    weak_topics = []

    for t in topic_score:
        total_topic = len([q for q in questions if q["topic"] == t])
        correct = topic_score[t]
        st.write(f"{t}: {correct}/{total_topic}")

        if correct / total_topic < 0.6:
            weak_topics.append(t)

    # =========================
    # NHẬN ĐỊNH AI
    # =========================
    st.markdown("## 🧠 Nhận định chuyên sâu")

    if level_score["Nhận biết"] < 6:
        st.error("Bạn đang hổng kiến thức nền tảng. Cần củng cố lý thuyết trước khi làm bài nâng cao.")
    elif level_score["Thông hiểu"] < 6:
        st.warning("Bạn hiểu lý thuyết nhưng yếu kỹ năng biến đổi và lập luận.")
    elif level_score["Vận dụng"] < 6:
        st.warning("Bạn thiếu kỹ năng xử lý bài tổng hợp và bài dài.")
    else:
        st.success("Bạn có nền tảng tốt để hướng tới 8.5+ trở lên.")

    # =========================
    # LỘ TRÌNH HỌC 4 TUẦN
    # =========================
    st.markdown("## 🎯 Lộ trình cải thiện trong 4 tuần")

    if weak_topics:

        st.subheader("Tuần 1–2: Củng cố nền tảng")
        for t in weak_topics:
            st.write(f"- Ôn lại toàn bộ lý thuyết chuyên đề {t}")
            st.write(f"  + Làm 30–50 bài cơ bản {t}")
            st.write(f"  + Ghi lại công thức và dạng bài hay sai")

        st.subheader("Tuần 3: Nâng mức Thông hiểu")
        st.write("- Làm bài tổng hợp mức trung bình")
        st.write("- Luyện kỹ năng biến đổi, trình bày rõ ràng")

        st.subheader("Tuần 4: Luyện đề & Vận dụng")
        st.write("- Làm 3 đề full 50 câu")
        st.write("- Sau mỗi đề phân tích lỗi sai")
        st.write("- Tập trung câu vận dụng và bài dài")

    else:
        st.success("Không có chuyên đề yếu rõ rệt.")
        st.write("Tập trung luyện đề tổng hợp và tăng tốc độ làm bài.")

    # =========================
    # DỰ ĐOÁN NÂNG CAO
    # =========================
    st.markdown("## 🎯 Dự đoán năng lực sau 4 tuần")

    if percent >= 85:
        st.success("Nếu giữ phong độ và luyện đề đều, có thể đạt 9–9.5.")
    elif percent >= 70:
        st.info("Có thể đạt 8–8.5 nếu cải thiện vận dụng.")
    else:
        st.error("Cần nghiêm túc theo lộ trình trên để vượt mức 7 điểm.")
