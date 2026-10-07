import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# 1. TẠO DỮ LIỆU SINH VIÊN
# =========================

data = {
    "Họ và tên": [
       "Kieu Tran Quang Huy",
        "Huynh Tan Khanh",
        "Nguyen Tan Tai",
        "Nguyen Thanh Danh",
        "Bui Thanh Lich",
        "Ngo Dang Duy",
        "Le Tan Sang",
        "Le Mạnh Quan",
        "Do Van Minh",
        "To Binh Nguyen"
    ],

    "Chuyên cần": [9, 8, 7, 10, 6, 8, 9, 7, 5, 10],

    "Giữa kỳ": [8, 7, 6, 9, 5, 8, 8, 7, 6, 9],

    "Cuối kỳ": [9, 8, 7, 9, 6, 9, 8, 6, 5, 10]
}

df = pd.DataFrame(data)


# =========================
# 2. TÍNH ĐIỂM TỔNG KẾT
# =========================

df["Tổng kết"] = (
    df["Chuyên cần"] * 0.2
    + df["Giữa kỳ"] * 0.3
    + df["Cuối kỳ"] * 0.5
)

df["Tổng kết"] = df["Tổng kết"].round(2)


# =========================
# 3. XẾP LOẠI
# =========================

def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"


df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)


# =========================
# 4. TIÊU ĐỀ WEB APP
# =========================

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")


# =========================
# 5. HIỂN THỊ BẢNG ĐIỂM
# =========================

st.subheader("Bảng điểm sinh viên")

st.dataframe(df)


# =========================
# 6. THỐNG KÊ
# =========================

st.subheader("Thống kê")

diem_trung_binh = df["Tổng kết"].mean()

sinh_vien_cao_nhat = df.loc[df["Tổng kết"].idxmax()]

sinh_vien_thap_nhat = df.loc[df["Tổng kết"].idxmin()]

so_sinh_vien_dat = (df["Tổng kết"] >= 5).sum()

st.write(
    "Điểm trung bình của lớp:",
    round(diem_trung_binh, 2)
)

st.write(
    "Sinh viên có điểm cao nhất:",
    sinh_vien_cao_nhat["Họ và tên"],
    "-",
    sinh_vien_cao_nhat["Tổng kết"]
)

st.write(
    "Sinh viên có điểm thấp nhất:",
    sinh_vien_thap_nhat["Họ và tên"],
    "-",
    sinh_vien_thap_nhat["Tổng kết"]
)

st.write(
    "Số sinh viên đạt:",
    so_sinh_vien_dat
)


# =========================
# 7. CHỌN SINH VIÊN
# =========================

st.subheader("Thông tin sinh viên")

selected_student = st.selectbox(
    "Chọn sinh viên:",
    df["Họ và tên"]
)

student = df[
    df["Họ và tên"] == selected_student
].iloc[0]

st.write("Họ tên:", student["Họ và tên"])
st.write("Điểm chuyên cần:", student["Chuyên cần"])
st.write("Điểm giữa kỳ:", student["Giữa kỳ"])
st.write("Điểm cuối kỳ:", student["Cuối kỳ"])
st.write("Điểm tổng kết:", student["Tổng kết"])
st.write("Xếp loại:", student["Xếp loại"])


# =========================
# 8. BIỂU ĐỒ
# =========================

st.subheader("Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(
    df["Họ và tên"],
    df["Tổng kết"]
)

ax.set_title("Điểm tổng kết của 10 sinh viên")

ax.set_xlabel("Sinh viên")

ax.set_ylabel("Điểm tổng kết")

plt.xticks(rotation=45)

plt.tight_layout()

st.pyplot(fig)


# =========================
# 9. THÔNG TIN NGƯỜI TẠO
# =========================

st.markdown("---")

st.caption("Họ tên: TRƯƠNG LÊ GIA HUY")
st.caption("MSSV: 052208006781")
