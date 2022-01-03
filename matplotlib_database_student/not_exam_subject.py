import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# read file csv

not_exam_subject = []
df_student = pd.read_csv("./clean_data (1).csv")
a = df_student.info()
print(a)
print("các thang điểm môn toán: ", df_student.toán.unique())

clean_data_subject = [df_student.toán, df_student.ngữ_văn, df_student.khxh, df_student.khtn, df_student.lịch_sử, df_student.địa_lí, df_student.gdcd, df_student.sinh_học, df_student.vật_lí, df_student.hóa_học, df_student.tiếng_anh]

for i in range(len(clean_data_subject)):
    a = len(df_student[clean_data_subject[i] == -1])
    not_exam_subject.append(a)
print(not_exam_subject)




percent_not_exam_subject = []
for i in range(len(not_exam_subject)):
    percent = round(not_exam_subject[i] *100 / len(df_student.sbd))
    percent_not_exam_subject.append(percent)


name_subject = ["toán", "ngữ văn", "khxh", "khtn", "lịch sử", "địa lí", "gdcd", "sinh học", "vật lí", "hóa học", "tiếng anh"]

# tổng hợp lại
print("số học sinh không thi các môn: ", not_exam_subject)
print("các tên môn học: ", name_subject)
print("số học sinh không thi dưới dạng phần trăm: ", percent_not_exam_subject)

figuer, axis = plt.subplots()
y_pos = np.arange(len(name_subject))


plt.bar(y_pos, percent_not_exam_subject, align = "center")

plt.xticks(y_pos, name_subject)
axis.set_ylim(0, 100)

plt.ylabel('phần trăm')
plt.title('tỉ lệ học sinh bỏ môn')
#add value to matplotlib barchart
rects = axis.patches
for rect, label in zip(rects, not_exam_subject):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width()/2, height + 2, label,
            ha = 'center', va = 'bottom')
plt.show()