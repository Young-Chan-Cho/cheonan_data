import pandas as pd

df1 = pd.read_excel('main_dataset.xlsx')
df2 = pd.read_excel('traffic_data.xlsx')

df1.info()
df2.info()

df1["도로형태"].unique()
df1["사고유형"].unique()
df1_crossroad = df1[df1["도로형태"].str.contains("교차로", na=False)].dropna()
df1_crossroad

import matplotlib.pyplot as plt
from matplotlib import rcParams

# 폰트 설정
rcParams['font.family'] = 'Malgun Gothic'
rcParams['axes.unicode_minus'] = False

# '교차로' 데이터 필터링
df1_crossroad = df1[df1["도로형태"].str.contains("교차로", na=False)]

# 사고유형별 건수 집계
accident_counts = df1_crossroad["사고유형"].value_counts()

# 색상 리스트 생성 (최댓값만 빨강, 나머지는 하늘색)
colors = ['red' if i == accident_counts.idxmax() else 'skyblue'
          for i in accident_counts.index]

# 시각화
plt.figure(figsize=(10, 6))
accident_counts.plot(kind='bar', color=colors)
plt.title("교차로 사고유형별 건수")
plt.xlabel("사고유형")
plt.ylabel("사고 건수")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
from matplotlib import rcParams

# 한글 폰트 설정 (Windows 기준)
rcParams['font.family'] = 'Malgun Gothic'
rcParams['axes.unicode_minus'] = False

# '교차로' 데이터 필터링
df1_crossroad = df1[df1["도로형태"].str.contains("교차로", na=False)]

# 법규위반별 건수 집계
law_violation_counts = df1_crossroad["법규위반"].value_counts()

# 색상 리스트 생성 (기본 파랑, 최댓값은 빨강)
colors = ['red' if i == law_violation_counts.idxmax() else 'skyblue'
          for i in law_violation_counts.index]

# 시각화
plt.figure(figsize=(10, 6))
law_violation_counts.plot(kind='bar', color=colors)
plt.title("교차로 법규위반별 건수")
plt.xlabel("법규위반")
plt.ylabel("사고 건수")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
from matplotlib import rcParams

# 한글 폰트(Windows 기준) & 마이너스 기호 설정
rcParams['font.family'] = 'Malgun Gothic'
rcParams['axes.unicode_minus'] = False

# 1) 결측치 제거
df_clean = df1.dropna(subset=["도로형태"]).copy()

# 2) '교차로' / '단일로' / 그 외('기타')로 분류
def map_category(x: str) -> str:
    if "교차로" in x:
        return "교차로"
    elif "단일로" in x:
        return "단일로"
    else:
        return "기타"

df_clean["도로분류"] = df_clean["도로형태"].apply(map_category)

# 3) 비율(%) 계산
order = ["교차로", "단일로", "기타"]
ratio = (df_clean["도로분류"]
         .value_counts(normalize=True)
         .reindex(order)
         .fillna(0) * 100)

# 4) 파이차트 시각화
plt.figure(figsize=(6, 6))
plt.pie(ratio,
        labels=ratio.index,
        autopct="%.1f%%",
        startangle=90,
        colors=["#FF9999", "#99CCFF", "#99FF99"])
plt.title("도로형태 분류 비율(%) - 결측치 제거 후")
plt.show()

import matplotlib.pyplot as plt
from matplotlib import rcParams

# 한글 폰트 설정 (Windows 기준)
rcParams['font.family'] = 'Malgun Gothic'
rcParams['axes.unicode_minus'] = False

# 1) 도로형태, 사고유형 결측치 제거
df_clean = df1.dropna(subset=["도로형태", "사고유형"]).copy()

# 2) 도로형태 단순 분류
def map_category(x: str) -> str:
    if "교차로" in x:
        return "교차로"
    elif "단일로" in x:
        return "단일로"
    else:
        return "기타"

df_clean["도로분류"] = df_clean["도로형태"].apply(map_category)

# 3) 파이차트 비교를 위한 데이터 준비
road_types = ["교차로", "단일로"]
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

for ax, road in zip(axes, road_types):
    df_subset = df_clean[df_clean["도로분류"] == road]
    total_count = len(df_subset)
    car_to_car_count = df_subset["사고유형"].str.contains("차대차", na=False).sum()
    other_count = total_count - car_to_car_count

    sizes = [car_to_car_count, other_count]
    labels = ["차대차", "기타"]
    colors = ["#FF9999", "#99CCFF"]

    ax.pie(sizes, labels=labels, autopct="%.1f%%", startangle=90, colors=colors)
    ax.set_title(f"{road} 사고유형 비율")

plt.suptitle("교차로 vs 단일로의 '차대차' 사고 비율 비교", fontsize=14)
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
from matplotlib import rcParams

# 한글 폰트 설정 (Windows 기준)
rcParams['font.family'] = 'Malgun Gothic'
rcParams['axes.unicode_minus'] = False

# 1) 결측치 제거
df_clean = df1.dropna(subset=["도로형태", "사고유형"]).copy()

# 2) 도로형태 분류
def map_category(x: str) -> str:
    if "교차로" in x:
        return "교차로"
    elif "단일로" in x:
        return "단일로"
    else:
        return "기타"

df_clean["도로분류"] = df_clean["도로형태"].apply(map_category)

# 3) 조건별 건수 계산
교차로_차대차 = df_clean[(df_clean["도로분류"] == "교차로") &
                      (df_clean["사고유형"].str.contains("차대차", na=False))].shape[0]

교차로_기타 = df_clean[(df_clean["도로분류"] == "교차로") &
                    (~df_clean["사고유형"].str.contains("차대차", na=False))].shape[0]

차대차_기타 = df_clean[(df_clean["도로분류"] != "교차로") &
                    (df_clean["사고유형"].str.contains("차대차", na=False))].shape[0]

# 4) 데이터 구성
labels = ["교차로 차대차", "교차로 기타", "차대차 - 기타"]
sizes = [교차로_차대차, 교차로_기타, 차대차_기타]
colors = ["#FF6666", "#FFCCCC", "#66B2FF"]

# 5) 파이차트 시각화
plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct="%.1f%%", startangle=90, colors=colors)
plt.title("교차로·기타 구간의 차대차/기타 사고 비율")
plt.show()